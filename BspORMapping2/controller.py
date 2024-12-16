import tkinter as tk
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind buttons to methods
        self.view.add_person_button.config(command=self.add_person)
        self.view.add_measurement_button.config(command=self.add_measurement)
        self.view.delete_button.config(command=self.delete_selected)

        # Refresh the view initially
        self.refresh_view()

    def add_person(self):
        """
        Adds or updates a person in the database.
        """
        inputs = self.view.get_inputs()
        name, age, blood_type = inputs["name"], inputs["age"], inputs["blood_type"]

        if not name or not age or not blood_type:
            self.view.set_status("All fields for person are required!", "error")
            return

        try:
            self.model.add_or_update_person(name, int(age), blood_type)
            self.view.set_status(f"Person '{name}' added/updated successfully.", "success")
            self.refresh_view()
        except ValueError:
            self.view.set_status("Age must be a number!", "error")

    def add_measurement(self):
        """
        Adds or updates a measurement in the database.
        """
        inputs = self.view.get_inputs()
        name, temperature, time = inputs["name"], inputs["temperature"], inputs["time"]

        if not name or not temperature or not time:
            self.view.set_status("All fields for measurement are required!", "error")
            return

        try:
            hour, minute = map(int, time.split(":"))
            self.model.add_or_update_measurement(name, hour, minute, float(temperature))
            self.view.set_status(f"Measurement for '{name}' at {hour:02}:{minute:02} added/updated.", "success")
            self.refresh_view()
        except ValueError:
            self.view.set_status("Invalid time or temperature format!", "error")

    def delete_selected(self):
        """
        Deletes the selected item from the Listbox. Handles both 'Person:' and 'Measurement:' types.
        """
        selected_item = self.view.get_selected_item()
        if not selected_item:
            self.view.set_status("No item selected for deletion!", "error")
            return

        if "Person:" in selected_item:
            # Delete the person and all their measurements
            name = selected_item.split(":")[1].split(",")[0].strip()
            self.model.delete_person(name)
            self.view.set_status(f"Person '{name}' deleted successfully.", "success")
        elif "Measurement:" in selected_item:
            # Delete the specific measurement
            try:
                parts = selected_item.split(" ")
                time_part = parts[3].rstrip(",")
                hour, minute = map(int, time_part.split(":"))
                parent_name = self._find_parent_person(selected_item)
                if parent_name:
                    self.model.delete_measurement(parent_name, hour, minute)
                    self.view.set_status(f"Measurement for '{parent_name}' at {hour:02}:{minute:02} deleted.", "success")
                else:
                    self.view.set_status("Error finding parent person for measurement.", "error")
            except (IndexError, ValueError):
                self.view.set_status("Error parsing selected measurement.", "error")
        self.refresh_view()

    def refresh_view(self):
        """
        Refreshes the data displayed in the View.
        """
        self.view.refresh_data_display()

    def _find_parent_person(self, selected_item):
        """
        Finds the parent person for a given measurement in the listbox.
        This method identifies the nearest preceding 'Person:' entry.
        """
        listbox_items = self.view.data_display.get(0, tk.END)  # Get all items from the listbox
        selected_index = listbox_items.index(selected_item)  # Get the index of the selected item

        # Traverse backward to find the associated person
        for i in range(selected_index - 1, -1, -1):
            if "Person:" in listbox_items[i]:  # Look for a 'Person:' entry
                return listbox_items[i].split(":")[1].split(",")[0].strip()  # Extract and return the person's name

        return None  # If no parent found, return None
