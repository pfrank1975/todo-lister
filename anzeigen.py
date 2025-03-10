def anzeigen(eintraege):
    if not eintraege:
        print("\nDie ToDo-Liste ist leer.")
        return

    for eintrag in eintraege:
        print("\nName: ", eintrag["name"],
        "\nPriorität: ", eintrag["pos"],
        "\nFortschritt: ", eintrag["fortschritt"],
        "\nBemerkung: ", eintrag["bemerkung"])
