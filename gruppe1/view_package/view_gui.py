from model_package.model import Model
import tkinter as tk
from tkinter import messagebox

class ViewGUI:
    def __init__(self, model: Model, root: tk.Tk):
        if not isinstance(model, Model) or not isinstance(root, tk.Tk):
            raise ValueError("Model nicht valide.")
        else:
            self.model = model
            self.root = root
            self.root.title("Umfrage")
            self.root.geometry("400x400")

        self.create_widgets()
        self.callbacks = {}

    def create_widgets(self):
        # Name
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        # Altersgruppe
        self.age_label = tk.Label(self.root, text="Altersspanne:")
        self.age_label.pack()
        self.age_var = tk.StringVar()
        self.age_var.set(None)  # Setze auf None, um keine Vorauswahl zu haben
        age_options = ["18 bis 27", "28 bis 37", "38 bis 47", "48 bis 57", "58 bis 67", "68 bis 77", "anderes"]
        for option in age_options:
            radio = tk.Radiobutton(self.root, text=option, variable=self.age_var, value=option)
            radio.pack(anchor=tk.CENTER)

        # Biologisches Geschlecht
        self.biological_sex_label = tk.Label(self.root, text="Biologisches Geschlecht:")
        self.biological_sex_label.pack()
        self.sex_var = tk.StringVar()
        self.sex_var.set(None)  # Setze auf None
        for sex in ["w", "m"]:
            radio = tk.Radiobutton(self.root, text=sex, variable=self.sex_var, value=sex)
            radio.pack(anchor=tk.CENTER)

        # Vorerkrankungen
        self.pre_existing_conditions_label = tk.Label(self.root, text="Vorerkrankungen:")
        self.pre_existing_conditions_label.pack()
        self.pre_conditions_var = tk.StringVar()
        self.pre_conditions_var.set(None)  # Setze auf None
        for condition in ["ja", "nein"]:
            radio = tk.Radiobutton(self.root, text=condition, variable=self.pre_conditions_var, value=condition,
                                   command=self.notify_pre_conditions)
            radio.pack(anchor=tk.CENTER)

        self.condition_options_frame = tk.Frame(self.root)
        self.condition_options_frame.pack()

        # Fitnesslevel
        self.fitness_level_label = tk.Label(self.root, text="Fitnesslevel:")
        self.fitness_level_label.pack()
        self.fitness_var = tk.StringVar()
        self.fitness_var.set(None)  # Setze auf None

        for level in ["wenig aktiv", "aktiv", "sehr aktiv"]:
            radio = tk.Radiobutton(self.root, text=level, variable=self.fitness_var, value=level)
            radio.pack(anchor=tk.CENTER)

        # Ernährung
        self.diet_level_label = tk.Label(self.root, text="Ernährung:")
        self.diet_level_label.pack()
        self.diet_var = tk.StringVar()
        self.diet_var.set(None)  # Setze auf None
        for level in ["unausgewogene Ernährung", "ausgewogenere Ernährung", "ausgewogene Ernährung"]:
            radio = tk.Radiobutton(self.root, text=level, variable=self.diet_var, value=level)
            radio.pack(anchor=tk.CENTER)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Absenden", command=self.submit)
        self.submit_button.pack()

    def notify_pre_conditions(self):
        # Informiere die Control-Klasse über Änderungen
        pre_existing_condition = self.pre_conditions_var.get()
        if 'pre_existing_conditions' in self.callbacks:
            self.callbacks['pre_existing_conditions'](pre_existing_condition)

    def submit(self):
        # Hier sammeln wir die Daten und informieren die Control-Klasse
        data = {
            'name': self.name_entry.get(),
            'age': self.age_var.get(),
            'biological_sex': self.sex_var.get(),
            'pre_existing_conditions': self.pre_conditions_var.get(),
            'fitness_level': self.fitness_var.get(),
            'diet_level': self.diet_var.get()
        }
        if 'submit' in self.callbacks:
            self.callbacks['submit'](data)

    def set_callbacks(self, callbacks):
        self.callbacks = callbacks

    def show_pre_existing_conditions_options(self):
        # Zeige zusätzliche Optionen für Vorerkrankungen an
        # Hier können weitere Widgets hinzugefügt werden, um spezifische Bedingungen auszuwählen
        tk.Label(self.condition_options_frame, text="Wählen Sie eine Vorerkrankung:").pack(anchor=tk.W)
        condition_options = ["Bluthochdruck", "Schilddrüsenüberfunktion", "andere"]
        for option in condition_options:
            tk.Checkbutton(self.condition_options_frame, text=option).pack(anchor=tk.W)

    def hide_pre_existing_conditions_options(self):
        # Verstecke die zusätzlichen Optionen
        for widget in self.condition_options_frame.winfo_children():
            widget.destroy()