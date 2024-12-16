import tkinter as tk
from model import get_all_people, get_measurements_for_person


class PersonView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Person and Measurements Database")

        # Status label at the top left
        self.status_label = tk.Label(self.root, text="", fg="black", bg="white", font=("Arial", 10, "bold"), anchor="w",
                                     padx=5)
        self.status_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Input fields
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.age_label = tk.Label(self.root, text="Age:")
        self.age_label.grid(row=2, column=0, padx=10, pady=5)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        self.blood_type_label = tk.Label(self.root, text="Blood Type:")
        self.blood_type_label.grid(row=3, column=0, padx=10, pady=5)
        self.blood_type_entry = tk.Entry(self.root)
        self.blood_type_entry.grid(row=3, column=1, padx=10, pady=5)

        self.temperature_label = tk.Label(self.root, text="Body Temperature:")
        self.temperature_label.grid(row=4, column=0, padx=10, pady=5)
        self.temperature_entry = tk.Entry(self.root)
        self.temperature_entry.grid(row=4, column=1, padx=10, pady=5)

        self.time_label = tk.Label(self.root, text="Time (hh:mm):")
        self.time_label.grid(row=5, column=0, padx=10, pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=5, column=1, padx=10, pady=5)

        # Listbox for displaying people and their measurements
        self.people_list_label = tk.Label(self.root, text="People and Measurements:")
        self.people_list_label.grid(row=6, column=0, padx=10, pady=5)
        self.people_listbox = tk.Listbox(self.root, height=15, width=70, selectmode=tk.SINGLE)
        self.people_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for actions
        self.add_person_button = tk.Button(self.root, text="Add/Update Person")
        self.add_person_button.grid(row=8, column=0, padx=10, pady=10)

        self.add_measurement_button = tk.Button(self.root, text="Add/Update Measurement")
        self.add_measurement_button.grid(row=8, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Selected")
        self.delete_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def set_add_person_action(self, action):
        """
        Sets the action for the Add/Update Person button.
        """
        self.add_person_button.config(command=action)

    def set_add_measurement_action(self, action):
        """
        Sets the action for the Add/Update Measurement button.
        """
        self.add_measurement_button.config(command=action)

    def set_delete_action(self, action):
        """
        Sets the action for the Delete button.
        """
        self.delete_button.config(command=action)

    def get_inputs(self):
        """
        Collects inputs from the input fields.
        """
        return {
            "name": self.name_entry.get().strip(),
            "age": self.age_entry.get().strip(),
            "blood_type": self.blood_type_entry.get().strip(),
            "body_temperature": self.temperature_entry.get().strip(),
            "time": self.time_entry.get().strip(),
        }

    def clear_inputs(self):
        """
        Clears all input fields.
        """
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.blood_type_entry.delete(0, tk.END)
        self.temperature_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

    def update_people_list(self):
        """
        Updates the people list in the Listbox with data from the database.
        """
        self.people_listbox.delete(0, tk.END)  # Clear existing content
        people = get_all_people()

        for person in people:
            # Add Person details
            self.people_listbox.insert(tk.END,
                                       f"Person: {person.name}, Age: {person.age}, Blood Type: {person.blood_type}")

            # Add associated Measurements
            measurements = get_measurements_for_person(person.name)
            for m in measurements:
                self.people_listbox.insert(
                    tk.END, f"  Measurement: {m.hour:02}:{m.minute:02}, Temp: {m.body_temperature}°C"
                )

    def get_selected_item(self):
        """
        Retrieves the selected item from the Listbox (either person or measurement).
        """
        selection = self.people_listbox.curselection()
        if not selection:
            return None

        selected_index = selection[0]
        selected_item = self.people_listbox.get(selected_index)

        if "Person:" in selected_item:
            # Selected a person
            try:
                name = selected_item.split(":")[1].split(",")[0].strip()
                return {"type": "person", "name": name}
            except (IndexError, ValueError):
                return None  # Handle unexpected string format

        elif "Measurement:" in selected_item:
            # Selected a measurement
            try:
                # Traverse backward to find the associated parent person
                parent_name = None
                for i in range(selected_index - 1, -1, -1):  # Loop backwards from current index
                    potential_person = self.people_listbox.get(i)
                    if "Person:" in potential_person:
                        parent_name = potential_person.split(":")[1].split(",")[0].strip()
                        break

                if not parent_name:
                    return None  # No associated parent person found

                # Extract hour and minute from the measurement string
                parts = selected_item.split(" ")
                time_part = parts[3].rstrip(",")  # Remove trailing comma
                hour, minute = map(int, time_part.split(":"))

                return {"type": "measurement", "name": parent_name, "hour": hour, "minute": minute}
            except (IndexError, ValueError):
                return None  # Handle unexpected string format or parsing errors

        return None

    def update_status(self, message, status_type="info"):
        """
        Updates the status label with a prefixed message.
        """
        prefixes = {
            "error": "Error:",
            "added": "Added:",
            "deleted": "Deleted:",
        }
        prefix = prefixes.get(status_type, "")
        color = "red" if status_type == "error" else "green"
        self.status_label.config(
            text=f"{prefix} {message}",
            fg=color,
            font=("Arial", 10, "bold"),
            bg="white"
        )

    def run(self):
        """
        Runs the main Tkinter loop.
        """
        self.root.mainloop()
