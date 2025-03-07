from model_package.model import Model
import tkinter as tk
from tkinter import messagebox

class ViewGUI:
    def __init__(self, model: Model, root: tk.Tk):
        if not isinstance(model, Model):
            raise ValueError("Model nicht valide.")
        elif not isinstance(root, tk.Tk):
            raise ValueError("Hauptfenster nicht vorhanden.")

        # dependency injection
        self.model = model
        self.root = root

        self.setup_window()
        self.pre_conditions_options_hidden = True

    def setup_window(self):
        self.root.title("Diabetes-II-Risikorechner")
        self.root.minsize(400, 650)

        self.form_frame = tk.Frame(self.root)
        self.display_frame = tk.Frame(self.root)

        self.create_form_widgets()
        self.create_display_widgets()

        self.show_form_frame()

    def create_form_widgets(self):
        # opening disclaimer
        label = tk.Label(self.form_frame, text="Willkommen zum Ihrem Risikorechner! Disclaimer!!!!!!!!!!!!!!!!!!!!!!!! "
                                         "Falls Sie fortfahren, erklären Sie sich einverstanden.",
                         anchor=tk.CENTER, wraplength=400)
        label.pack()

        # name
        self.name_label = tk.Label(self.form_frame, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.pack()

        # age
        self.age_label = tk.Label(self.form_frame, text="Altersspanne:")
        self.age_label.pack()
        self.age_var = tk.StringVar()
        self.age_var.set(None)  # Setze auf None, um keine Vorauswahl zu haben
        age_options = ["18 bis 44", "45 bis 64", "65 bis 79"]
        for option in age_options:
            radio = tk.Radiobutton(self.form_frame, text=option, variable=self.age_var, value=option)
            radio.pack(anchor=tk.CENTER)

        # biological sex
        self.biological_sex_label = tk.Label(self.form_frame, text="Biologisches Geschlecht:")
        self.biological_sex_label.pack()
        self.sex_var = tk.StringVar()
        self.sex_var.set(None)  # Setze auf None
        for sex in ["w", "m"]:
            radio = tk.Radiobutton(self.form_frame, text=sex, variable=self.sex_var, value=sex)
            radio.pack(anchor=tk.CENTER)

        # pre existing conditions
        self.pre_conditions_label = tk.Label(self.form_frame, text="Vorerkrankungen:")
        self.pre_conditions_label.pack()
        self.pre_conditions_var = tk.StringVar()
        self.pre_conditions_var.set(None)  # Setze auf None
        for condition in ["ja", "nein"]:
            radio = tk.Radiobutton(self.form_frame, text=condition, variable=self.pre_conditions_var,
                                   value=condition, command= lambda: self.handle_pre_conditions(self.pre_conditions_var))
            radio.pack(anchor=tk.CENTER)

        self.condition_options_frame = tk.Frame(self.form_frame)
        self.condition_options_frame.pack()

        # fitness level
        self.fitness_level_label = tk.Label(self.form_frame, text="Fitnesslevel:")
        self.fitness_level_label.pack()
        self.fitness_var = tk.StringVar()
        self.fitness_var.set(None)  # Setze auf None

        for level in ["wenig aktiv (weniger als 150 min Sport/Woche)",
                      "aktiv (mind. 150 min Sport/Woche)",
                      "sehr aktiv (deutlich mehr als 150 min Sport/Woche)"]:
            radio = tk.Radiobutton(self.form_frame, text=level, variable=self.fitness_var, value=level)
            radio.pack(anchor=tk.CENTER)

        # diet
        self.diet_level_label = tk.Label(self.form_frame, text="Ernährung:")
        self.diet_level_label.pack()
        self.diet_var = tk.StringVar()
        self.diet_var.set(None)  # Setze auf None
        for level in ["unausgewogene Ernährung", "ausgewogenere Ernährung", "ausgewogene Ernährung"]:
            radio = tk.Radiobutton(self.form_frame, text=level, variable=self.diet_var, value=level)
            radio.pack(anchor=tk.CENTER)

        # Submit Button
        self.add_person_button = tk.Button(self.form_frame, text="Hinzufügen")
        self.add_person_button.pack()

        # clear button


        self.button_switch_to_display = tk.Button(self.form_frame, text="Zur Auswertung",
                                                  command=self.show_display_frame)
        self.button_switch_to_display.pack()

    def create_display_widgets(self):
        self.data_display = tk.Listbox(self.display_frame, height=15, width=80)
        self.data_display.pack()

        self.button_switch_to_form = tk.Button(self.display_frame, text="Zur Dateneingabe",
                                               command=self.show_form_frame)
        self.button_switch_to_form.pack()

    def show_form_frame(self):
        self.display_frame.pack_forget()
        self.form_frame.pack(fill="both", expand=True)

    def show_display_frame(self):
        self.form_frame.pack_forget()
        self.display_frame.pack(fill="both", expand=True)

    def get_inputs(self):
        # Hier sammeln wir die Daten und informieren die Control-Klasse
        pre_conditions = "nein"     # Vorauswahl = "nein"
        if "ja" == self.pre_conditions_var.get():
            pre_conditions = ", ".join([pre_condition.get() for pre_condition in self.selected_pre_conditions if ("" != pre_condition.get() and "None" != pre_condition.get())])
        return {
            'name': self.name_entry.get(),
            'age': self.age_var.get(),
            'biological_sex': self.sex_var.get(),
            'pre_conditions': pre_conditions,
            'fitness_level': self.fitness_var.get(),
            'diet_level': self.diet_var.get()
        }

    def handle_pre_conditions(self, value):
        if value.get() == "ja":
            self.show_pre_conditions_options()
        else:
            self.hide_pre_conditions_options()

    def show_pre_conditions_options(self):
        # Zeige zusätzliche Optionen für Vorerkrankungen an
        # Hier können weitere Widgets hinzugefügt werden, um spezifische Bedingungen auszuwählen
        if False == self.pre_conditions_options_hidden:
            return
        self.pre_conditions_options_hidden = False
        tk.Label(self.condition_options_frame, text="Wählen Sie eine Vorerkrankung:").pack(anchor=tk.W)
        condition_options = ["Bluthochdruck", "Schilddrüsenüberfunktion", "andere"]
        self.selected_pre_conditions = []
        for option in condition_options:
            condition_option_var = tk.StringVar()
            condition_option_var.set(None)  # Setze auf None
            self.selected_pre_conditions.append(condition_option_var)
            tk.Checkbutton(self.condition_options_frame, text=option, variable=condition_option_var, onvalue=option, offvalue="").pack(anchor=tk.W)

    def hide_pre_conditions_options(self):
        # Verstecke die zusätzlichen Optionen
        self.pre_conditions_options_hidden = True
        for widget in self.condition_options_frame.winfo_children():
            widget.destroy()



    #TODO: werden 'set(None)'s gebraucht?