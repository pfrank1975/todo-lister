def anzeigen(eintraege):
    i = 0
    if not eintraege:
        print("\nDie ToDo-Liste ist leer.")
        return

    for name, eintrag in eintraege.items():
        i += 1
        print(name, eintrag["pos"], eintrag["fortschritt"], eintrag["bemerkung"])
    print('Es konnten ' + str(i) + ' Datensätze aufgelistet werden.')
