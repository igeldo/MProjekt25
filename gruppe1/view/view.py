
class View:
    def __init__(self):

        print("Test Main_view")

    def ui(self):
        # TODO Literatur

        # TODO while start

        print("Willkommen zum deinem Risikorechner")
        print("Disclaimer")
        # TODO
        # disclaimer

        name = str(input("Bitte geben Sie Ihren Vor- und Nachnamen: "))

        # TODO
        # name logic
        # name check for duplicates

        age = int(input("Bitte geben Sie Ihr Alter in Zahlen an: "))

        # TODO
        # age logic and exception string to int conversion
        # age add range

        biological_sex = str(input("Bitte geben Sie Ihr biologisches Geschlecht an (w/m): "))

        # TODO
        # biological_sex logic and data type (enum/bool/?) and exception handling and case insensitivity

        pre_existing_conditions = str(input("Bitte geben Sie an, ob Sie Vorerkrankungen haben (Ja/Nein): "))
        # TODO
        # pre_existing_conditions logic and type conversion to data type (enum/bool/?) and exception handling and case insensitivity

        print("Bitte beachten Sie: ")
        print("Risikofaktor 1:  ")
        print("Risikofaktor 2:  ")
        print("Risikofaktor 3:  ")
        print("Risikofaktor 4:  ")
        print("Risikofaktor 5:  ")
        print("Sonstige Risikofaktoren 6:  ")

        # TODO
        # research risk factors and adding them

        pre_existing_conditions = str(
            input("Bitte geben Sie die Zahl(en) der zutreffenden Risikofaktoren an (mit Komma getrennt): "))

        print("Bitte beachten Sie: ")
        print("Fitnesslevel 1: seltene Bewegung und/oder leichter Sport 1 mal im Monat. ")
        print("Fitnesslevel 2: gelegentliche Bewegung und/oder regelmäßiger Sport 1 mal in der Woche. ")
        print("Fitnesslevel 3: viel Bewegung und/oder regelmäßiger Sport mehr als 1 mal in der Woche. ")

        fitness_level = int(input("Bitte geben Sie Ihr Fitnesslevel als Zahl (1,2 oder 3) an: "))
        # TODO exceptions str to int conversion

        print("Bitte beachten Sie: ")
        print("Ernährung 1: unausgewogene Ernährung, Obst und Gemüse 1 mal im Monat. ")
        print("Ernährung 2: ausgewogenere Ernährung, Obst und Gemüse 1 mal in der Woche. ")
        print("Ernährung 3: ausgewogene Ernährung, Obst und Gemüse bis zu 5 mal in der Woche. ")

        diet_level = int(input(
            "Bitte geben Sie die Ernährungsbeschreibung, die am ehesten auf Sie zutrifft, als Zahl (1,2 oder 3) an: "))
        # TODO exceptions str to int conversion

        # TODO calculations
        result = "0"

        print("Ihr Ergebnis: Sie haben eine Wahrscheinlichkeit von " + result + " %, an _ erkrankt zu sein")
        # TODO
        # result

        addPerson_endProgramm = str(input(
            "Falls Sie das Programm beenden möchten, drücken Sie die 1, falls Sie eine weitere Person hinzufügen möchten, drücken Sie die 2. "))
        # TODO
        # restart or end logic

        # TODO while end
        print("Disclaimer")
        # TODO
        # disclaimer
        print("Vielen Dank für Ihre Teilnahme. Auf Wiedersehen und gute Besserung.")


