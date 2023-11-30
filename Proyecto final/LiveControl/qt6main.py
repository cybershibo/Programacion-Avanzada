from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QComboBox, QTextEdit, QWidget, QLineEdit, QGridLayout
import serial.tools.list_ports
import serial
import json

class ArduinoGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arduino Control")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        # Group: COM Port
        com_group = QVBoxLayout()

        self.com_label = QLabel("Select COM Port:")
        com_group.addWidget(self.com_label)

        self.com_entry = QComboBox()
        com_group.addWidget(self.com_entry)

        self.refresh_button = QPushButton("Refresh Ports", self)
        self.refresh_button.clicked.connect(self.refresh_serial_ports)
        com_group.addWidget(self.refresh_button)

        self.connect_button = QPushButton("Connect", self)
        self.connect_button.clicked.connect(self.connect_to_arduino)
        com_group.addWidget(self.connect_button)

        layout.addLayout(com_group, 0, 0, 2, 1)

        # Group: Digital Outputs
        outputs_group = QVBoxLayout()
        outputs_group.addWidget(QLabel("Digital Outputs"))

        self.pin_states = ["LOW"] * 8

        for i in range(8):
            btn_text = f"Output Pin {i}"
            btn = QPushButton(btn_text, self)
            btn.clicked.connect(lambda _, index=i: self.toggle_output_pin(index))
            outputs_group.addWidget(btn)

        layout.addLayout(outputs_group, 0, 1)

        # Group: Programmable Outputs
        prog_group = QVBoxLayout()
        prog_group.addWidget(QLabel("Programmable Outputs"))

        self.programmable_states = [False] * 12

        for i in range(8, 20):
            btn_text = f"Programmable Pin {i - 8}"
            btn = QPushButton(btn_text, self)
            btn.clicked.connect(lambda _, index=i: self.toggle_programmable_pin(index - 8))
            prog_group.addWidget(btn)

        layout.addLayout(prog_group, 0, 2)

        # Group: Inputs
        inputs_group = QVBoxLayout()
        inputs_group.addWidget(QLabel("Inputs"))

        self.entry_labels = []
        self.entry_vars = []

        for i in range(8):
            label_text = f"Input {i} Value:"
            entry_label = QLabel(label_text)
            inputs_group.addWidget(entry_label)
            self.entry_labels.append(entry_label)

            entry_var = QLineEdit(self)
            entry_var.setReadOnly(True)
            inputs_group.addWidget(entry_var)
            self.entry_vars.append(entry_var)

        layout.addLayout(inputs_group, 1, 1, 1, 2)

        # Terminal
        self.terminal_label = QLabel("Terminal:")
        layout.addWidget(self.terminal_label, 2, 0)

        self.terminal_text = QTextEdit(self)
        self.terminal_text.setReadOnly(True)
        layout.addWidget(self.terminal_text, 3, 0, 1, 3)

        self.ser = None

        self.refresh_serial_ports()

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
        self.start_timer(1000)  # Refresh every 5 seconds

    def start_timer(self, interval):
        timer = self.startTimer(interval)
        timer.timeout.connect(self.auto_refresh_serial_ports)

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

if __name__ == "__main__":
    app = QApplication([])
    window = ArduinoGUI()
    window.show()
    app.exec()
