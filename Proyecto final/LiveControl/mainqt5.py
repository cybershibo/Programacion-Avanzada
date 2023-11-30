import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt

import serial.tools.list_ports
import serial
import json


class ArduinoGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arduino Control")

        self.com_label = QLabel("Select COM Port:")
        self.com_entry = QComboBox()

        self.refresh_button = QPushButton("Refresh Ports", clicked=self.refresh_serial_ports)
        self.connect_button = QPushButton("Connect", clicked=self.connect_to_arduino)
        self.get_inputs_button = QPushButton("Get Inputs", clicked=self.get_inputs)

        self.pin_states = ["LOW"] * 8
        self.programmable_states = [False] * 12

        self.init_ui()

        self.ser = None

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.com_label)
        layout.addWidget(self.com_entry)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.get_inputs_button)

        for i in range(8):
            btn_text = f"Output Pin {i}"
            btn = QPushButton(btn_text, clicked=lambda _, index=i: self.toggle_output_pin(index))
            layout.addWidget(btn)

        for i in range(8, 20):
            btn_text = f"Programmable Pin {i - 8}"
            btn = QPushButton(btn_text, clicked=lambda _, index=i: self.toggle_programmable_pin(index - 8))
            layout.addWidget(btn)

        self.entry_labels = []
        self.entry_vars = []

        for i in range(8):
            label_text = f"Input {i} Value:"
            label = QLabel(label_text)
            entry_var = QLineEdit()
            entry_var.setReadOnly(True)
            self.entry_labels.append(label)
            self.entry_vars.append(entry_var)

            layout.addWidget(label)
            layout.addWidget(entry_var)

        self.terminal_label = QLabel("Terminal:")
        self.terminal_text = QTextEdit()
        self.terminal_text.setReadOnly(True)

        layout.addWidget(self.terminal_label)
        layout.addWidget(self.terminal_text)

        self.setLayout(layout)

    def refresh_serial_ports(self):
        available_ports = [port.device for port in serial.tools.list_ports.comports()]
        self.com_entry.clear()
        self.com_entry.addItems(available_ports)

    def connect_to_arduino(self):
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()

            port = self.com_entry.currentText()
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
        self.terminal_text.append(message)

    def auto_refresh_serial_ports(self):
        self.refresh_serial_ports()
        self.read_input_states()
        self.startTimer(1000)  # Refresh every 5 seconds

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
                                self.entry_vars[i].setText(str(input_state))
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ArduinoGUI()
    window.show()
    sys.exit(app.exec_())
