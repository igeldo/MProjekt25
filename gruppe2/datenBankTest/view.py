import customtkinter
customtkinter.set_appearance_mode("light")
from datenbank import create_table, add_person, get_all_persons  # Import der Datenbank-Funktion

# Daten abrufen
personen = get_all_persons()

# Daten im Terminal ausgeben
print("Inhalt der Tabelle 'person':")
for person in personen:
    print(f"Vorname: {person[0]}, Alter: {person[1]}, Geschlecht: {person[2]}, Gewicht: {person[3]}, Groeße: {person[4]}")

class App(customtkinter.CTk): # App erbt von customtkinter.CTk

    def __init__(self):
        super().__init__() # super().__init__(): Ruft den Konstruktor der übergeordneten Klasse (customtkinter.CTk) auf, um sicherzustellen, dass die grundlegenden Initialisierungen vorgenommen werden.
        self.geometry("400x350")
        width = 100
        # Datenbank initialisieren
        create_table()

        # 1 Eingabefeld
        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="Vorname:", width=width, height=30)
        self.entry1.pack(padx=20, pady=10)

        # 2 Eingabefeld
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Alter:", width=width, height=30)
        self.entry2.pack(padx=20, pady=10)

        # 3 Eingabefeld
        self.entry3 = customtkinter.CTkEntry(self, placeholder_text="Geschlecht:", width=width, height=30)
        self.entry3.pack(padx=20, pady=10)

        # 4 Eingabefeld
        self.entry4 = customtkinter.CTkEntry(self, placeholder_text="Gewicht in Kg:", width=width, height=30)
        self.entry4.pack(padx=20, pady=10)

        # 5 Eingabefeld
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

    def submit_callback(self):
        # Werte aus den Eingabefeldern abrufen
        vorname = self.entry1.get()
        age = self.entry2.get()
        geschlecht = self.entry3.get()
        gewicht = self.entry4.get()
        groeße = self.entry5.get()

        # Daten in der Datenbank speichern
        try:
            add_person(vorname, int(age), geschlecht, float(gewicht), float(groeße))
            print("Daten wurden erfolgreich angelegt")
            self.entry1.delete(0, "end") # von index 0 bis zum ende wird alles gelöscht
            self.entry2.delete(0, "end")
            self.entry3.delete(0, "end")
            self.entry4.delete(0, "end")
            self.entry5.delete(0, "end")
        except ValueError:
            print("Fehler: Bitte überprüfen sie ihren Angaben")
        # Nach dem Speichern die Eingabefelder leeren

        # Grundumsatz berechnen (bei absoluter körperlicher Ruhe)
        if geschlecht == "männlich":
            grundumsatz = 88.362 + (13.397 * gewicht) + (4.799 * groeße * 100) - (5.677 * age)
        elif geschlecht == "weiblich":
            grundumsatz = 447.593 + (9.247 * gewicht) + (3.098 * groeße * 100) - (4.330 * age)
        else:
            grundumsatz = None # Ungültige Eingabe für Geschlecht
            # Ergebnisse anzeigen
        if grundumsatz is not None:
            print(f"{vorname}, Ihr Grundumsatz beträgt {grundumsatz:.2f} Kalorien pro Tag.")
        else:
            print("Ungültige Eingabe für das Geschlecht. Bitte geben Sie 'männlich' oder 'weiblich' ein.")


app = App()
app.mainloop()
