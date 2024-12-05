import psycopg2

# Funktion zur Verbindung mit der Datenbank
def verbinde_mit_datenbank():
    try:
        verbindung = psycopg2.connect(
            dbname="postgres",          # Name der Datenbank
            user="postgres",           # Benutzername
            password="1376saghar",     # Passwort der Datenbank
            host="localhost",          # Host
            port="5432"                # Standard-Port von PostgreSQL
        )
        print("Datenbankverbindung erfolgreich hergestellt!")
        return verbindung
    except Exception as e:
        print("Fehler bei der Verbindung zur Datenbank:", e)
        return None

# Funktion zur Berechnung des Herzerkrankungsrisikos
def berechne_risiko(alter, geschlecht, hdl, ldl, blutdruck, raucher, diabetes):
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

    # HDL-Cholesterin (je niedriger, desto höher das Risiko)
    if hdl < 40:
        risiko_punkte += 2
    elif 40 <= hdl < 50:
        risiko_punkte += 1
    elif hdl >= 60:
        risiko_punkte -= 1

    # LDL-Cholesterin (je höher, desto höher das Risiko)
    if ldl >= 160:
        risiko_punkte += 2
    elif 130 <= ldl < 160:
        risiko_punkte += 1

    # Systolischer Blutdruck
    if blutdruck >= 140:
        risiko_punkte += 2
    elif 120 <= blutdruck < 140:
        risiko_punkte += 1

    # Raucherstatus
    if raucher:
        risiko_punkte += 2

    # Diabetesstatus
    if diabetes:
        risiko_punkte += 2

    # Risiko basierend auf der Punktzahl (vereinfachte Skala)
    if risiko_punkte <= 5:
        risiko = "Niedriges Risiko (<10%)"
    elif 6 <= risiko_punkte <= 10:
        risiko = "Mittleres Risiko (10-20%)"
    else:
        risiko = "Hohes Risiko (>20%)"

    return risiko

# Funktion zur Eingabe und Speicherung von Daten
def daten_eingeben_und_risiko_berechnen():
    verbindung = verbinde_mit_datenbank()
    if not verbindung:
        return
    cursor = verbindung.cursor()

    try:
        while True:  # Schleife, um mehrere Patienten einzugeben
            print("\n--- Patientendaten eingeben ---")
            gesundheitsnummer = int(input("Gesundheitsnummer: "))  # Benutzer gibt die Gesundheitsnummer ein
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            alter = int(input("Alter (muss > 0 sein): "))
            geschlecht = input("Geschlecht (M/F): ").strip().upper()
            adresse = input("Adresse: ")
            telefon = input("Telefonnummer: ")
            email = input("E-Mail: ")

            # Daten in patienten-Tabelle einfügen
            cursor.execute("""
                INSERT INTO patienten (gesundheitsnummer, vorname, nachname, alter, geschlecht, adresse, telefon, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """, (gesundheitsnummer, vorname, nachname, alter, geschlecht, adresse, telefon, email))
            print(f"Patient eingefügt mit Gesundheitsnummer: {gesundheitsnummer}")

            print("\n--- Gesundheitsdaten eingeben ---")
            hdl_cholesterin = float(input("HDL-Cholesterin (mg/dL): "))
            ldl_cholesterin = float(input("LDL-Cholesterin (mg/dL): "))
            systolischer_blutdruck = int(input("Systolischer Blutdruck (mmHg): "))
            diabetes_status = input("Diabetesstatus (ja/nein): ").strip().lower() == "ja"
            raucher_status = input("Raucherstatus (ja/nein): ").strip().lower() == "ja"

            # Risiko berechnen
            risiko = berechne_risiko(alter, geschlecht, hdl_cholesterin, ldl_cholesterin, systolischer_blutdruck, raucher_status, diabetes_status)

            # Daten in gesundheitsdaten-Tabelle einfügen
            cursor.execute("""
                INSERT INTO gesundheitsdaten (gesundheitsnummer, hdl_cholesterin, ldl_cholesterin, systolischer_blutdruck, diabetes_status, raucher_status, risiko)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, (gesundheitsnummer, hdl_cholesterin, ldl_cholesterin, systolischer_blutdruck, diabetes_status, raucher_status, risiko))
            print(f"Gesundheitsdaten erfolgreich eingefügt. Risiko: {risiko}")

            # Änderungen speichern
            verbindung.commit()
            print("\nAlle Daten wurden erfolgreich gespeichert!")

            # Nach weiteren Patienten fragen
            weitere_patienten = input("Möchten Sie einen weiteren Patienten eingeben? (ja/nein): ").strip().lower()
            if weitere_patienten != "ja":
                break

    except Exception as e:
        print("Fehler beim Einfügen der Daten oder Berechnen des Risikos:", e)
        verbindung.rollback()

    finally:
        cursor.close()
        verbindung.close()
        print("Datenbankverbindung geschlossen.")

# Hauptprogramm
if __name__ == "__main__":
    daten_eingeben_und_risiko_berechnen()
