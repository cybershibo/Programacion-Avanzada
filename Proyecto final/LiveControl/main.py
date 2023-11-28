import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import serial.tools.list_ports
import serial
import json

class ArduinoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Arduino Control")

        self.com_label = ttk.Label(self.master, text="Select COM Port:")
        self.com_label.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        self.com_var = tk.StringVar()
        self.com_entry = ttk.Combobox(self.master, textvariable=self.com_var)
        self.com_entry.grid(row=0, column=1, pady=5, padx=10)

        self.refresh_button = ttk.Button(self.master, text="Refresh Ports", command=self.refresh_serial_ports)
        self.refresh_button.grid(row=0, column=2, pady=5, padx=10)

        self.connect_button = ttk.Button(self.master, text="Connect", command=self.connect_to_arduino)
        self.connect_button.grid(row=0, column=3, pady=5, padx=10)

        self.output_buttons = []
        for i in range(8):
            btn = ttk.Button(self.master, text=f"Pin {i}", command=lambda index=i: self.toggle_pin(index))
            btn.grid(row=2 + i, column=0, pady=5, padx=10)
            self.output_buttons.append(btn)

        self.device_status_label = ttk.Label(self.master, text="Device Status:")
        self.device_status_label.grid(row=10, column=0, pady=5, padx=10)

        self.device_status_var = tk.StringVar()
        self.device_status_entry = ttk.Entry(self.master, textvariable=self.device_status_var, state="readonly")
        self.device_status_entry.grid(row=11, column=0, pady=5, padx=10)

        self.terminal_label = ttk.Label(self.master, text="Terminal:")
        self.terminal_label.grid(row=12, column=0, pady=5, padx=10)

        self.terminal_text = scrolledtext.ScrolledText(self.master, height=10, width=40, wrap=tk.WORD)
        self.terminal_text.grid(row=13, column=0, pady=5, padx=10, columnspan=4)

        self.refresh_serial_ports()  # Initial refresh
        self.auto_refresh_serial_ports()  # Start automatic refresh

        self.ser = None

    def refresh_serial_ports(self):
        available_ports = [port.device for port in serial.tools.list_ports.comports()]
        self.com_entry["values"] = available_ports

    def connect_to_arduino(self):
        try:
            self.ser = serial.Serial(self.com_var.get(), 9600, timeout=2)
            self.log_to_terminal("Connected to Arduino")
            self.update_device_status()
        except Exception as e:
            self.log_to_terminal(f"Error connecting to Arduino: {str(e)}")

    def toggle_pin(self, pin_index):
        command = {"command": 1, "pinIndex": pin_index}
        self.send_command(command)
        self.update_device_status()

    def send_command(self, command):
        if self.ser:
            command_str = json.dumps(command) + "\n"
            self.ser.write(command_str.encode())
            self.log_to_terminal(f"Sent command: {command_str}")

    def update_device_status(self):
        if self.ser:
            device_status_str = self.ser.readline().decode('utf-8')
            device_status = json.loads(device_status_str)
            self.device_status_var.set(f"Pin States: {device_status['pinStates']}")
            self.log_to_terminal(f"Received response: {device_status_str}")

    def log_to_terminal(self, message):
        self.terminal_text.insert(tk.END, f"{message}\n")
        self.terminal_text.see(tk.END)  # Scroll to the end

    def auto_refresh_serial_ports(self):
        self.refresh_serial_ports()
        self.master.after(5000, self.auto_refresh_serial_ports)  # Refresh every 5 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoGUI(root)
    root.mainloop()
