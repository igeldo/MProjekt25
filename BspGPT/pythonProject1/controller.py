from model import Person  # Importieren der Klasse Person

class PersonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Buttons hinzufügen
        self.view.add_button("Hinzufügen", row=7, column=0, command=self.add_person)
        self.view.add_button("Entfernen", row=7, column=1, command=self.remove_person)
        self.view.add_button("Speichern in JSON", row=8, column=0, command=self.save_to_file)
        self.view.add_button("Laden aus JSON", row=8, column=1, command=self.load_from_file)

    def add_person(self):
        """Fügt eine Person hinzu, nachdem die Eingaben geprüft wurden."""
        try:
            name = self.view.name_entry.get()
            age = self.view.age_entry.get()
            height = self.view.height_entry.get()
            weight = self.view.weight_entry.get()
            blood_type = self.view.blood_type_entry.get()

            # Eingabeprüfung
            if not name or not age or not height or not weight or not blood_type:
                raise ValueError("Alle Felder müssen ausgefüllt werden!")

            try:
                age = int(age)
                height = float(height)
                weight = float(weight)
            except ValueError:
                raise ValueError("Alter, Größe und Gewicht müssen numerisch sein!")

            # Person erstellen und dem Model hinzufügen
            person = Person(name, age, height, weight, blood_type)  # Direkt die Klasse verwenden
            self.model.add_person(person)

            # View anstoßen, sich selbst zu aktualisieren
            self.view.update_person_list()
            self.view.show_message("Erfolg", f"Person '{name}' wurde hinzugefügt.")
        except ValueError as e:
            self.view.show_error("Fehler", str(e))

    # Rest des Codes bleibt unverändert

    def remove_person(self):
        """Entfernt eine ausgewählte Person."""
        try:
            index = self.view.person_listbox.curselection()
            if not index:
                raise ValueError("Bitte wählen Sie eine Person aus!")

            self.model.remove_person(index[0])

            # View anstoßen, sich selbst zu aktualisieren
            self.view.update_person_list()
            self.view.show_message("Erfolg", "Person wurde entfernt.")
        except ValueError as e:
            self.view.show_error("Fehler", str(e))

    def save_to_file(self):
        """Speichert die Personenliste in einer JSON-Datei."""
        try:
            filename = self.view.filename_entry.get()
            if not filename:
                raise ValueError("Bitte geben Sie einen Dateinamen ein!")
            self.model.save_to_file(filename)

            # Erfolgsmeldung anzeigen
            self.view.show_message("Erfolg", f"Personenliste wurde in '{filename}' gespeichert.")
        except Exception as e:
            self.view.show_error("Fehler", f"Die Datei konnte nicht gespeichert werden: {e}")

    def load_from_file(self):
        """Lädt die Personenliste aus einer JSON-Datei."""
        try:
            filename = self.view.filename_entry.get()
            if not filename:
                raise ValueError("Bitte geben Sie einen Dateinamen ein!")
            self.model.load_from_file(filename)

            # View anstoßen, sich selbst zu aktualisieren
            self.view.update_person_list()
            self.view.show_message("Erfolg", f"Personenliste wurde aus '{filename}' geladen.")
        except FileNotFoundError:
            self.view.show_error("Fehler", "Die Datei wurde nicht gefunden!")
        except Exception as e:
            self.view.show_error("Fehler", f"Die Datei konnte nicht geladen werden: {e}")
