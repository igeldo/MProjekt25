from model import add_or_update_person, add_or_update_measurement, delete_person, delete_measurement

class PersonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_add_person_action(self.add_or_update_person)
        self.view.set_add_measurement_action(self.add_or_update_measurement)
        self.view.set_delete_action(self.delete_selected)

        self.refresh_people_list()

    def add_or_update_person(self):
        inputs = self.view.get_inputs()
        name, age, blood_type = inputs["name"], inputs["age"], inputs["blood_type"]

        if not name or not age or not blood_type:
            self.view.update_status("All fields for person are required!", status_type="error")
            return

        try:
            age = int(age)
        except ValueError:
            self.view.update_status("Age must be a number!", status_type="error")
            return

        add_or_update_person(name, age, blood_type)
        self.view.update_status(f"Person '{name}' has been added/updated.", status_type="added")
        self.refresh_people_list()

    def add_or_update_measurement(self):
        inputs = self.view.get_inputs()
        name, body_temperature, time = inputs["name"], inputs["body_temperature"], inputs["time"]

        if not name or not body_temperature or not time:
            self.view.update_status("All fields for measurement are required!", status_type="error")
            return

        try:
            # Validate time format
            hour, minute = map(int, time.split(":"))
            if not (0 <= hour <= 23):
                raise ValueError("Hour must be between 0 and 23.")
            if not (0 <= minute <= 59):
                raise ValueError("Minute must be between 0 and 59.")

            # Validate body temperature
            body_temperature = float(body_temperature)

        except ValueError as e:
            self.view.update_status(f"Invalid input: {e}", status_type="error")
            return

        add_or_update_measurement(name, hour, minute, body_temperature)
        self.view.update_status(f"Measurement for '{name}' at {hour:02}:{minute:02} has been added/updated.", status_type="added")
        self.refresh_people_list()

    def delete_selected(self):
        selected = self.view.get_selected_item()
        if not selected:
            self.view.update_status("No item selected for deletion!", status_type="error")
            return

        if selected["type"] == "person":
            name = selected["name"]
            delete_person(name)
            self.view.update_status(f"Person '{name}' and all their measurements have been deleted.", status_type="deleted")
        elif selected["type"] == "measurement":
            name, hour, minute = selected["name"], selected["hour"], selected["minute"]
            delete_measurement(name, hour, minute)
            self.view.update_status(f"Measurement for '{name}' at {hour:02}:{minute:02} has been deleted.", status_type="deleted")

        self.refresh_people_list()

    def refresh_people_list(self):
        self.view.update_people_list()
