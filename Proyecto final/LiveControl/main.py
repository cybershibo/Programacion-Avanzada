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

        self.pin_states = ["LOW"] * 8
        self.programmable_states = [False] * 12

        for i in range(8):
            btn_text = f"Output Pin {i}"
            btn = ttk.Button(self.master, text=btn_text, command=lambda index=i: self.toggle_output_pin(index))
            btn.grid(row=i + 1, column=0, pady=5, padx=10)

        for i in range(8, 20):
            btn_text = f"Programmable Pin {i - 8}"
            btn = ttk.Button(self.master, text=btn_text, command=lambda index=i: self.toggle_programmable_pin(index - 8))
            btn.grid(row=i - 7, column=1, pady=5, padx=10)

        self.terminal_label = ttk.Label(self.master, text="Terminal:")
        self.terminal_label.grid(row=21, column=0, pady=5, padx=10)

        self.terminal_text = scrolledtext.ScrolledText(self.master, height=10, width=40, wrap=tk.WORD)
        self.terminal_text.grid(row=22, column=0, pady=5, padx=10, columnspan=4)

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
        except Exception as e:
            self.log_to_terminal(f"Error connecting to Arduino: {str(e)}")

    def toggle_output_pin(self, pin_index):
        current_state = self.pin_states[pin_index]
        new_state = "HIGH" if current_state == "LOW" else "LOW"
        command = {"command": "digital_outputs", "pin": pin_index, "message": new_state}
        self.send_command(command)
        self.pin_states[pin_index] = new_state

    def toggle_programmable_pin(self, pin_index):
        current_state = self.programmable_states[pin_index]
        new_state = "HIGH" if current_state == "LOW" else "LOW"
        command = {"command": "digital_prog", "pin": pin_index, "message": new_state}
        self.send_command(command)
        self.programmable_states[pin_index] = new_state

    def send_command(self, command):
        if self.ser:
            command_str = json.dumps(command) + "\n"
            self.ser.write(command_str.encode())
            self.log_to_terminal(f"Sent command: {command_str}")

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
