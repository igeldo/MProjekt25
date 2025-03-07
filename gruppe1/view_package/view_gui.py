from model_package.model import Model
import tkinter as tk

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

        # Status Label (First Row)
        self.status_label = tk.Label(self.root, bg="lightgray")
        self.status_label.pack(expand=True, fill=tk.X)

        self.form_frame = tk.Frame(self.root)
        self.display_frame = tk.Frame(self.root)

        self.create_form_widgets()
        self.create_display_widgets()

        self.show_form_frame()

    def create_form_widgets(self):
        # opening disclaimer
        label = tk.Label(self.form_frame, text="Willkommen zum Ihrem Risikorechner! "
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
        self.sex_var.set(None)  # Setze auf None, um keine Vorauswahl zu haben
        for sex in ["w", "m"]:
            radio = tk.Radiobutton(self.form_frame, text=sex, variable=self.sex_var, value=sex)
            radio.pack(anchor=tk.CENTER)

        # pre existing conditions
        self.pre_conditions_label = tk.Label(self.form_frame, text="Vorerkrankungen:")
        self.pre_conditions_label.pack()
        self.pre_conditions_var = tk.StringVar()
        self.pre_conditions_var.set(None)  # Setze auf None, um keine Vorauswahl zu haben
        # for condition in ["ja", "nein"]:
        #     radio = tk.Radiobutton(self.form_frame, text=condition, variable=self.pre_conditions_var,
        #                            value=condition, command= lambda: self.handle_pre_conditions(self.pre_conditions_var))
        #     radio.pack(anchor=tk.CENTER)

        radio_yes = tk.Radiobutton(self.form_frame, text="ja", variable=self.pre_conditions_var,
                                value="ja", command= self.show_pre_conditions_options)
        radio_yes.pack(anchor=tk.CENTER)
        radio_no = tk.Radiobutton(self.form_frame, text="nein", variable=self.pre_conditions_var,
                                value="nein", command = self.hide_pre_conditions_options)
        radio_no.pack(anchor=tk.CENTER)

        self.condition_options_frame = tk.Frame(self.form_frame)
        self.condition_options_frame.pack()

        # fitness level
        self.fitness_level_label = tk.Label(self.form_frame, text="Fitnesslevel:")
        self.fitness_level_label.pack()
        self.fitness_var = tk.StringVar()
        self.fitness_var.set(None)  # Setze auf None, um keine Vorauswahl zu haben

        for level in ["wenig aktiv (weniger als 150 min Sport/Woche)",
                      "aktiv (mind. 150 min Sport/Woche)",
                      "sehr aktiv (deutlich mehr als 150 min Sport/Woche)"]:
            radio = tk.Radiobutton(self.form_frame, text=level, variable=self.fitness_var, value=level)
            radio.pack(anchor=tk.CENTER)

        # diet
        self.diet_level_label = tk.Label(self.form_frame, text="Ernährung:")
        self.diet_level_label.pack()
        self.diet_var = tk.StringVar()
        self.diet_var.set(None)  # Setze auf None, um keine Vorauswahl zu haben
        for level in ["wenig ausgewogen", "ausgewogen", "sehr ausgewogen"]:
            radio = tk.Radiobutton(self.form_frame, text=level, variable=self.diet_var, value=level)
            radio.pack(anchor=tk.CENTER)

        # Add person button
        self.add_person_button = tk.Button(self.form_frame, text="Hinzufügen")
        self.add_person_button.pack()

        self.button_switch_to_display = tk.Button(self.form_frame, text="Zur Auswertung")
        self.button_switch_to_display.pack()

    def create_display_widgets(self):
        close_label = tk.Label(self.display_frame, text="Zum Hinzufügen einer weiteren Person"
                                                        " klicken Sie auf den Button 'Zur Dateneingabe'. Zum Beenden des Risikorechners"
                                                        " schließen Sie das Fenster mit dem Klicken auf X oben rechts",
                               anchor=tk.CENTER, wraplength=400)
        close_label.pack()

        risk_label = tk.Label(self.display_frame, text="Ihr geschätztes Risiko:", anchor=tk.CENTER)
        risk_label.pack()

        self.data_display = tk.Listbox(self.display_frame, height=15, width=80)
        self.data_display.pack()



        self.button_switch_to_form = tk.Button(self.display_frame, text="Zur Dateneingabe")
        self.button_switch_to_form.pack()

        disclaimer_label = tk.Label(self.display_frame, text="Bitte beachten Sie: "
            "Auch Personen mit einem geringen Risiko können an Diabetes erkranken. "
            "Dagegen können Personen mit einem hohen Risiko gesund bleiben. "
            "Der Test kann eine ärztliche Diagnose daher nicht ersetzen. "
            "Bitte sprechen Sie auch mit Ihrem Arzt über das Thema Diabetes. ", anchor=tk.CENTER, wraplength=400)
        disclaimer_label.pack()

    def show_form_frame(self):
        self.display_frame.pack_forget()
        self.form_frame.pack(fill="both", expand=True)

    def show_display_frame(self):
        self.form_frame.pack_forget()
        self.display_frame.pack(fill="both", expand=True)

    def get_inputs(self):
        pre_conditions = "nein"     # Vorauswahl = "nein"
        if "ja" == self.pre_conditions_var.get():
            pre_conditions = ", ".join([pre_condition.get() for pre_condition in self.selected_pre_conditions
                                        if ("" != pre_condition.get() and "None" != pre_condition.get())])
        return {
            'name': self.name_entry.get(),
            'age': self.age_var.get(),
            'biological_sex': self.sex_var.get(),
            'pre_conditions': pre_conditions,
            'fitness_level': self.fitness_var.get(),
            'diet_level': self.diet_var.get()
        }

    # def handle_pre_conditions(self, value):
    #     if value.get() == "ja":
    #         self.show_pre_conditions_options()
    #     else:
    #         self.hide_pre_conditions_options()

    def show_pre_conditions_options(self):
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

    def set_status(self, message, status_type="info"):
        self.status_label.config(text=f"Status: {message}")
        if status_type == "success":
            self.status_label.config(bg="green", fg="white")
        elif status_type == "error":
            self.status_label.config(bg="red", fg="white")
        else:
            self.status_label.config(bg="lightgray", fg="black")

    def clear_data_display(self):
        self.data_display.delete(0, tk.END)

    def show_all_results(self):
        self.clear_data_display()

        data = [f"{person._name}: {person._risk: .6f}%" for person in self.model.get_person_list()]
        for entry in data:
            self.data_display.insert(tk.END, entry)


    #TODO: werden 'set(None)'s gebraucht?