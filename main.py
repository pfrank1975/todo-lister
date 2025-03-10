#!/usr/bin/env python3

def main():

    from hinzufuegen import hinzufuegen
    from anzeigen import anzeigen
    from suchen import suchen
    from speichern import speichern
    import json

    def eintraege_laden():
        try:
            with open("todo-liste.json", "r") as datei:
                return json.load(datei)
        except FileNotFoundError:
            print("\nKeine bestehenden Daten gefunden.")
        return {}

    eintraege = eintraege_laden()

    while True:
        print("\n\n1. zur ToDo-Liste hinzufügen")
        print("2. ToDo-Liste anzeigen")
        print("3. Eintrag suchen")
        print("4. speichern")
        print("5. beenden")
        auswahl = input("\nAuswahl: ")
        if auswahl == "1":
            hinzufuegen()
        elif auswahl == "2":
            anzeigen(eintraege)
        elif auswahl == "3":
            suchen()
        elif auswahl == "4":
            speichern()
        elif auswahl == "5":
            print("\nProgramm beendet.")
            break
        else:
            print("\nBitte im Bereich von 1 bis 5 wählen.")

main()
