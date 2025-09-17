import tkinter as tk
from tkinter import ttk, messagebox
from src.converters import LengthConverter, MassConverter, TemperatureConverter
from src.history import add_record, load_history, clear_history


class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("500x450")

        self.category = tk.StringVar(value="Length")
        self.value = tk.StringVar()
        self.from_unit = tk.StringVar()
        self.to_unit = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()
        self.update_units()
        self.load_history()

    def create_widgets(self):
        ttk.Label(self.root, text="Category").pack()
        categories = ["Length", "Mass", "Temperature"]
        category_menu = ttk.Combobox(
            self.root, textvariable=self.category, values=categories
        )
        category_menu.bind("<<ComboboxSelected>>", lambda e: self.update_units())
        category_menu.pack()

        ttk.Label(self.root, text="Value").pack()
        ttk.Entry(self.root, textvariable=self.value).pack()

        ttk.Label(self.root, text="From").pack()
        self.from_menu = ttk.Combobox(self.root, textvariable=self.from_unit)
        self.from_menu.pack()

        ttk.Label(self.root, text="To").pack()
        self.to_menu = ttk.Combobox(self.root, textvariable=self.to_unit)
        self.to_menu.pack()

        ttk.Button(self.root, text="Convert", command=self.convert).pack(pady=10)

        ttk.Label(self.root, text="Result").pack()
        ttk.Label(self.root, textvariable=self.result).pack()

        ttk.Label(self.root, text="History").pack()
        self.history_listbox = tk.Listbox(self.root, height=10)
        self.history_listbox.pack(fill="both", expand=True)

        ttk.Button(self.root, text="Clear History", command=self.clear_history).pack(
            pady=5
        )