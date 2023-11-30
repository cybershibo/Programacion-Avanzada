import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Entry
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

        self.get_inputs_button = ttk.Button(self.master, text="Get Inputs", command=self.get_inputs)
        self.get_inputs_button.grid(row=0, column=4, pady=5, padx=10)

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

        self.entry_labels = []
        self.entry_vars = []

        for i in range(8):
            label_text = f"Input {i} Value:"
            entry_label = ttk.Label(self.master, text=label_text)
            entry_label.grid(row=15 + i, column=0, pady=5, padx=10, sticky="w")
            self.entry_labels.append(entry_label)

            entry_var = tk.StringVar()
            entry = Entry(self.master, textvariable=entry_var, state='readonly')
            entry.grid(row=15 + i, column=1, pady=5, padx=10)
            self.entry_vars.append(entry_var)

        self.terminal_label = ttk.Label(self.master, text="Terminal:")
        self.terminal_label.grid(row=23, column=0, pady=5, padx=10)

        self.terminal_text = scrolledtext.ScrolledText(self.master, height=10, width=40, wrap=tk.WORD)
        self.terminal_text.grid(row=24, column=0, pady=5, padx=10, columnspan=4)

        self.ser = None

    def refresh_serial_ports(self):
        available_ports = [port.device for port in serial.tools.list_ports.comports()]
        self.com_entry["values"] = available_ports

    def connect_to_arduino(self):
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()

            port = self.com_var.get()
            if port:
                self.ser = serial.Serial(port, 9600, timeout=2)
                self.log_to_terminal("Connected to Arduino")
                self.auto_refresh_serial_ports()  # Start automatic refresh
            else:
                self.log_to_terminal("Please select a valid COM port.")
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
        try:
            if self.ser and self.ser.is_open:
                command_str = json.dumps(command) + "\n"
                self.ser.write(command_str.encode())
                self.log_to_terminal(f"Sent command: {command_str}")
            else:
                self.log_to_terminal("Not connected to Arduino. Please connect first.")
        except Exception as e:
            self.log_to_terminal(f"Error sending command: {str(e)}")

    def get_inputs(self):
        try:
            command = {"command": "digital_inputs"}
            self.send_command(command)
        except Exception as e:
            self.log_to_terminal(f"Error getting inputs: {str(e)}")

    def log_to_terminal(self, message):
        self.terminal_text.insert(tk.END, f"{message}\n")
        self.terminal_text.see(tk.END)  # Scroll to the end

    def auto_refresh_serial_ports(self):
        self.refresh_serial_ports()
        self.read_input_states()
        self.master.after(1000, self.auto_refresh_serial_ports)  # Refresh every 5 seconds

    def read_input_states(self):
        try:
            if self.ser and self.ser.is_open:
                buffer = ""
                while True:
                    char = self.ser.read().decode()
                    if char == '\n':
                        try:
                            inputs_data = json.loads(buffer)
                            for i in range(8):
                                input_state = inputs_data.get(f"Input_{i}", False)
                                self.entry_vars[i].set(str(input_state))
                            break  # Salimos del bucle al recibir un mensaje completo
                        except json.JSONDecodeError as e:
                            self.log_to_terminal(f"Error decoding input states: {str(e)}")
                            break  # Salimos del bucle si hay un error en la decodificación
                    else:
                        buffer += char
            else:
                self.log_to_terminal("Not connected to Arduino. Please connect first.")
        except Exception as e:
            self.log_to_terminal(f"Error reading input states: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoGUI(root)
    root.mainloop()
