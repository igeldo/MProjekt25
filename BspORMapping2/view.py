
import tkinter as tk
class View:
    def __init__(self, root, model):
        self.root = root
        self.model = model  # Reference to the model to fetch data

        self.root.title("Person and Measurement Database")
        self.root.geometry("850x600")  # Adjusted for wider display

        # Status Label (First Row)
        self.status_label = tk.Label(root, text="Status: Ready", bg="lightgray", anchor="w")
        self.status_label.grid(row=0, column=0, columnspan=2, sticky="we", padx=5, pady=5)

        # Input fields
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=1, column=0)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=2, column=0)
        self.age_entry = tk.Entry(root, width=30)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        self.blood_type_label = tk.Label(root, text="Blood Type:")
        self.blood_type_label.grid(row=3, column=0)
        self.blood_type_entry = tk.Entry(root, width=30)
        self.blood_type_entry.grid(row=3, column=1, padx=5, pady=5)

        self.temp_label = tk.Label(root, text="Temperature:")
        self.temp_label.grid(row=4, column=0)
        self.temp_entry = tk.Entry(root, width=30)
        self.temp_entry.grid(row=4, column=1, padx=5, pady=5)

        self.time_label = tk.Label(root, text="Time (hh:mm):")
        self.time_label.grid(row=5, column=0)
        self.time_entry = tk.Entry(root, width=30)
        self.time_entry.grid(row=5, column=1, padx=5, pady=5)

        # Data Display
        self.data_display = tk.Listbox(root, height=15, width=80)
        self.data_display.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Buttons below the Listbox
        self.add_person_button = tk.Button(root, text="Add/Update Person", width=20)
        self.add_person_button.grid(row=7, column=0, padx=5, pady=5)

        self.add_measurement_button = tk.Button(root, text="Add/Update Measurement", width=20)
        self.add_measurement_button.grid(row=7, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(root, text="Delete Selected", width=20)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

    def refresh_data_display(self):
        """
        Refresh the data displayed in the listbox by querying the model.
        """
        data = []
        for person in self.model.get_all_people():
            data.append(f"Person: {person['name']}, {person['age']}, {person['blood_type']}")
            measurements = self.model.get_measurements_for_person(person["name"])
            for m in measurements:
                data.append(f"  Measurement: {m['hour']:02}:{m['minute']:02}, Temp: {m['temperature']}°C")

        self.update_data_display(data)

    def set_status(self, message, status_type="info"):
        """
        Updates the status label with a message and color.
        """
        self.status_label.config(text=f"Status: {message}")
        if status_type == "success":
            self.status_label.config(bg="green", fg="white")
        elif status_type == "error":
            self.status_label.config(bg="red", fg="white")
        else:
            self.status_label.config(bg="lightgray", fg="black")

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.blood_type_entry.delete(0, tk.END)
        self.temp_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

    def get_inputs(self):
        return {
            "name": self.name_entry.get(),
            "age": self.age_entry.get(),
            "blood_type": self.blood_type_entry.get(),
            "temperature": self.temp_entry.get(),
            "time": self.time_entry.get(),
        }

    def update_data_display(self, data):
        """
        Updates the listbox with data.
        """
        self.data_display.delete(0, tk.END)
        for item in data:
            self.data_display.insert(tk.END, item)

    def get_selected_item(self):
        selection = self.data_display.curselection()
        if not selection:
            return None
        return self.data_display.get(selection[0])
