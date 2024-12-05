import psycopg2

# --- Model ---
class Database:
    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def close(self):
        self.connection.close()


# --- View ---
class PatientView:
    def get_input(self, prompt):
        return input(prompt)

    def show_message(self, message):
        print(f"\n{message}\n")

    def show_error(self, error):
        print(f"\nFehler: {error}\n")


# --- Controller ---
class PatientController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate_risk(self, alter, geschlecht, hdl, ldl, blutdruck, raucher, diabetes):
        risiko_punkte = 0
        # Alter
        if 30 <= alter < 40:
            risiko_punkte += 1 if geschlecht == 'M' else 0
        elif 40 <= alter < 50:
            risiko_punkte += 2 if geschlecht == 'M' else 1
        elif 50 <= alter < 60:
            risiko_punkte += 3 if geschlecht == 'M' else 2
        elif 60 <= alter < 70:
            risiko_punkte += 4 if geschlecht == 'M' else 3
        elif alter >= 70:
            risiko_punkte += 5 if geschlecht == 'M' else 4
        # HDL
        if hdl < 40:
            risiko_punkte += 2
        elif 40 <= hdl < 50:
            risiko_punkte += 1
        elif hdl >= 60:
            risiko_punkte -= 1
        # LDL
        if ldl >= 160:
            risiko_punkte += 2
        elif 130 <= ldl < 160:
            risiko_punkte += 1
        # Blutdruck
        if blutdruck >= 140:
            risiko_punkte += 2
        elif 120 <= blutdruck < 140:
            risiko_punkte += 1
        # Raucher
        if raucher:
            risiko_punkte += 2
        # Diabetes
        if diabetes:
            risiko_punkte += 2

        if risiko_punkte <= 5:
            return "Niedriges Risiko (<10%)"
        elif 6 <= risiko_punkte <= 10:
            return "Mittleres Risiko (10-20%)"
        else:
            return "Hohes Risiko (>20%)"

    def run(self):
        while True:
            try:
                gesundheitsnummer = int(self.view.get_input("Gesundheitsnummer: "))
                vorname = self.view.get_input("Vorname: ")
                nachname = self.view.get_input("Nachname: ")
                alter = int(self.view.get_input("Alter: "))
                geschlecht = self.view.get_input("Geschlecht (M/F): ").strip().upper()
                adresse = self.view.get_input("Adresse: ")
                telefon = self.view.get_input("Telefon: ")
                email = self.view.get_input("E-Mail: ")

                patient_data = (gesundheitsnummer, vorname, nachname, alter, geschlecht, adresse, telefon, email)
                self.model.execute_query("""
                    INSERT INTO patienten (gesundheitsnummer, vorname, nachname, alter, geschlecht, adresse, telefon, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, patient_data)

                hdl = float(self.view.get_input("HDL-Cholesterin: "))
                ldl = float(self.view.get_input("LDL-Cholesterin: "))
                blutdruck = int(self.view.get_input("Blutdruck: "))
                diabetes = self.view.get_input("Diabetesstatus (ja/nein): ").strip().lower() == "ja"
                raucher = self.view.get_input("Raucherstatus (ja/nein): ").strip().lower() == "ja"

                risiko = self.calculate_risk(alter, geschlecht, hdl, ldl, blutdruck, raucher, diabetes)
                health_data = (gesundheitsnummer, hdl, ldl, blutdruck, diabetes, raucher, risiko)
                self.model.execute_query("""
                    INSERT INTO gesundheitsdaten (gesundheitsnummer, hdl_cholesterin, ldl_cholesterin, systolischer_blutdruck, diabetes_status, raucher_status, risiko)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """, health_data)

                self.view.show_message(f"Patient hinzugefügt. Risiko: {risiko}")

                weiter = self.view.get_input("Weiteren Patienten hinzufügen? (ja/nein): ").strip().lower()
                if weiter != "ja":
                    break
            except Exception as e:
                self.view.show_error(e)

if __name__ == "__main__":
    db = Database("postgres", "postgres", "1376saghar", "localhost", "5432")
    view = PatientView()
    controller = PatientController(db, view)
    controller.run()
    db.close()
