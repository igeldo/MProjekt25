import customtkinter
from datenbank import add_person, get_all_people
from sqlalchemy.exc import SQLAlchemyError

# CustomTkinter-Einstellungen
customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):  # App erbt von customtkinter.CTk
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Kalorien Tracker")
        width = 150

        # 1 Eingabefeld für Vorname
        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="Vorname:", width=width, height=30)
        self.entry1.pack(padx=20, pady=10)

        # 2 Eingabefeld für Alter
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Alter:", width=width, height=30)
        self.entry2.pack(padx=20, pady=10)

        # 3 Dropdown für Geschlecht
        self.gender_var = customtkinter.StringVar(value="Geschlecht auswählen")
        self.gender_menu = customtkinter.CTkOptionMenu(self, values=["Männlich", "Weiblich"], variable=self.gender_var)
        self.gender_menu.pack(padx=20, pady=10)

        # 4 Eingabefeld für Gewicht
        self.entry4 = customtkinter.CTkEntry(self, placeholder_text="Gewicht in Kg:", width=width, height=30)
        self.entry4.pack(padx=20, pady=10)

        # 5 Eingabefeld für Größe
        self.entry5 = customtkinter.CTkEntry(self, placeholder_text="Größe in cm:", width=width, height=30)
        self.entry5.pack(padx=20, pady=10)

        # Button zur Verarbeitung der Eingaben
        self.submit_button = customtkinter.CTkButton(self,
            text="Eingaben speichern",
            command=self.submit_callback,
            fg_color="#27ae60",  # Grün (Hintergrundfarbe)
            hover_color="#2ecc71"  # Hellgrün (Hover-Farbe)
        )
        self.submit_button.pack(padx=20, pady=10)

        # Ergebnisanzeige
        self.result_label = customtkinter.CTkLabel(self, text="")
        self.result_label.pack(padx=20, pady=10)

    def submit_callback(self):
        """Verarbeitet die Eingaben und speichert sie in der Datenbank."""
        vorname = self.entry1.get()
        age = self.entry2.get()
        geschlecht = self.gender_var.get()
        gewicht = self.entry4.get()
        groeße = self.entry5.get()

        # Eingaben validieren
        if not vorname or not age or not geschlecht or not gewicht or not groeße:
            self.result_label.configure(text="Bitte alle Felder ausfüllen!", text_color="red")
            return

        # Daten in der Datenbank speichern
        try:
            age = int(age)
            gewicht = float(gewicht)
            groeße = float(groeße)
        except ValueError:
            self.result_label.configure(text="Ungültige Werte!", text_color="red")
            return

        # Grundumsatz berechnen
        grundumsatz = self.calculate_bmr(geschlecht, gewicht, groeße, age)

        if grundumsatz is None:
            self.result_label.configure(text="Ungültiges Geschlecht!", text_color="red")
            return

        # Datenbank speichern
        try:
            add_person(vorname, age, geschlecht, gewicht, groeße)
            self.result_label.configure(
                text=f"{vorname}, Ihr Grundumsatz: {grundumsatz:.2f} Kalorien/Tag.",
                text_color="green"
            )
            self.clear_inputs()
        except SQLAlchemyError as e:
            self.result_label.configure(text=f"Datenbankfehler: {e}", text_color="red")

    def clear_inputs(self):
        """Löscht die Eingabefelder."""
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry4.delete(0, "end")
        self.entry5.delete(0, "end")
        self.gender_var.set("Geschlecht auswählen")

    @staticmethod
    def calculate_bmr(geschlecht, gewicht, groeße, age):
        """Berechnet den Grundumsatz (BMR)."""
        if geschlecht == "Männlich":
            return 88.362 + (13.397 * gewicht) + (4.799 * groeße) - (5.677 * age)
        elif geschlecht == "Weiblich":
            return 447.593 + (9.247 * gewicht) + (3.098 * groeße) - (4.330 * age)
        return None




# Anwendung starten
app = App()
app.mainloop()
