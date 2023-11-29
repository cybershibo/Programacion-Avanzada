import tkinter as tk
from tkinter import ttk
import json

class ArduinoSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Arduino Simulator")

        self.toolbar = ttk.Frame(self.master)
        self.toolbar.pack(side="top", fill="x")

        self.simulate_button = ttk.Button(self.toolbar, text="Simulate JSON", command=self.simulate_json)
        self.simulate_button.pack(side="left", padx=5, pady=5)

        self.json_slider = ttk.Scale(self.toolbar, from_=0, to=100, orient="horizontal")
        self.json_slider.pack(side="left", padx=5, pady=5)

        self.json_text = tk.Text(self.master, height=10, width=40)
        self.json_text.pack(padx=10, pady=10)

    def simulate_json(self):
        json_value = {"pinState": self.json_slider.get()}  # Modify this based on your actual JSON structure
        json_str = json.dumps(json_value, indent=2)
        self.json_text.delete(1.0, tk.END)
        self.json_text.insert(tk.END, json_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoSimulator(root)
    root.mainloop()
