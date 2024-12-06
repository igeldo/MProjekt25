
class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.setup_callbacks()

    def setup_callbacks(self):
        # Verknüpft die View-Callbacks mit den Controller-Funktionen
        self.view.submit_button.configure(command=self.handle_submit)

    def handle_submit(self):
        # Behandelt den Speichern-Button
        # Daten aus der View abrufen
        vorname = self.view.entry1.get()
        age = self.view.entry2.get()
        geschlecht = self.view.gender_var.get()
        gewicht = self.view.entry4.get()
        groeße = self.view.entry5.get()

        # Eingaben validieren
        if not vorname or not age or not geschlecht or not gewicht or not groeße:
            self.view.result_label.configure(text="Bitte alle Felder ausfüllen!", text_color="red")
            return

        try:
            age = int(age)
            gewicht = float(gewicht)
            groeße = float(groeße)
        except ValueError:
            self.view.result_label.configure(text="Ungültige Werte!", text_color="red")
            return

        # Grundumsatz berechnen
        grundumsatz = self.view.calculate_bmr(geschlecht, gewicht, groeße, age)
        if grundumsatz is None:
            self.view.result_label.configure(text="Ungültiges Geschlecht!", text_color="red")
            return

        # Datenbank speichern
        try:
            self.model.add_person(vorname, age, geschlecht, gewicht, groeße)
            self.view.result_label.configure(
                text=f"{vorname}, Ihr Grundumsatz: {grundumsatz:.2f} Kalorien/Tag.",
                text_color="green"
            )
            self.view.clear_inputs()
        except Exception as e:
            self.view.result_label.configure(text=f"Datenbankfehler: {e}", text_color="red")