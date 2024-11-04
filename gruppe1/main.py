
# Ganzzahlen int
# print("Willkommen zum Addierer-Programm")
# value1 = int(input("Erst Zahl eingeben:")) # Variablen langfristig als int_Typ verwandelt
# value2 = int(input("Erste Zahl eingeben:")) # Variablen langfristig als int_Typ verwandelt
# print(value1 + value2)

#TODO Literatur

#TODO while start

print("Willkommen zum deinem Risikorechner")
print("Disclaimer")
#TODO
# disclaimer

name = str(input("Bitte geben Sie Ihren Namen oder einen Alias ein: "))

#TODO
# name logic

age = int(input("Bitte geben Sie Ihr Alter an: "))

#TODO
# age logic and exception string to int conversion

biological_sex = str(input("Bitte geben Sie Ihr biologisches Geschlecht an (w/m): "))

#TODO
# biological_sex logic and data type (enum/bool/?) and exception handling and case insensitivity

pre_existing_conditions = str(input("Bitte geben Sie an, ob Sie Vorerkrankungen haben (Ja/Nein): "))
#TODO
# pre_existing_conditions logic and type conversion to data type (enum/bool/?) and exception handling and case insensitivity

print("Bitte beachten Sie: ")
print("Fitnesslevel 1: seltene Bewegung und/oder leichter Sport 1 mal im Monat. ")
print("Fitnesslevel 2: gelegentliche Bewegung und/oder regelmäßiger Sport 1 mal in der Woche. ")
print("Fitnesslevel 3: viel Bewegung und/oder regelmäßiger Sport mehr als 1 mal in der Woche. ")

fitness_level = int(input("Bitte geben Sie Ihr Fitnesslevel als Zahl (1,2 oder 3) an: "))
#TODO exceptions str to int conversion

print("Bitte beachten Sie: ")
print("Ernährung 1: unausgewogene Ernährung, Obst und Gemüse 1 mal im Monat. ")
print("Ernährung 2: ausgewogenere Ernährung, Obst und Gemüse 1 mal in der Woche. ")
print("Ernährung 3: ausgewogene Ernährung, Obst und Gemüse bis zu 5 mal in der Woche. ")

diet = int(input("Bitte geben Sie die Ernährungsbeschreibung, die am ehesten auf Sie zutrifft, als Zahl (1,2 oder 3) an: "))
#TODO exceptions str to int conversion

#TODO calculations
result = "0"

print("Ihr Ergebnis: Sie haben eine Wahrscheinlichkeit von " + result + " %, an _ erkrankt zu sein")
#TODO
# result

addPerson_endProgramm = str(input("Falls Sie das Programm beenden möchten, drücken Sie die 1, falls Sie eine weitere Person hinzufügen möchten, drücken Sie die 2. "))
#TODO
# restart or end logic

#TODO while end
print("Disclaimer")
#TODO
# disclaimer
print("Vielen Dank für Ihre Teilnahme. Auf Wiedersehen und gute Besserung.")
