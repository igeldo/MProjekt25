import tkinter as tk
from tkinter import messagebox

class PersonView:
    """Verantwortlich für die GUI."""
    def __init__(self, model):
        self.model = model
        self.root = tk.Tk()
        self.root.title("Personenverwaltung")

        # Eingabefelder für Personendaten
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Alter:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Größe (cm):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Gewicht (kg):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Blutgruppe:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.blood_type_entry = tk.Entry(self.root)
        self.blood_type_entry.grid(row=4, column=1, padx=10, pady=5)

        # Listbox zur Anzeige der Personen
        self.person_listbox = tk.Listbox(self.root, width=50, height=10)
        self.person_listbox.grid(row=5, column=0, columnspan=2, pady=10)

        # Eingabefeld für Dateinamen (für JSON-Datei)
        tk.Label(self.root, text="Dateiname:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.filename_entry = tk.Entry(self.root)
        self.filename_entry.grid(row=6, column=1, padx=10, pady=5)

    def add_button(self, text, row, column, command, columnspan=1):
        """Fügt einen Button hinzu."""
        button = tk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column, columnspan=columnspan, pady=10)
        return button

    def update_person_list(self):
        """Aktualisiert die Personenliste in der GUI."""
        self.person_listbox.delete(0, tk.END)
        for person in self.model.get_all():
            self.person_listbox.insert(tk.END, str(person))

    def show_message(self, title, message):
        """Zeigt eine Erfolgsmeldung."""
        messagebox.showinfo(title, message)

    def show_error(self, title, message):
        """Zeigt eine Fehlermeldung."""
        messagebox.showerror(title, message)

    def run(self):
        """Startet die GUI."""
        self.root.mainloop()
