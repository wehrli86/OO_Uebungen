def berechne_minimale_note(noten):
    noten_werte = [float(note.replace(',', '.')) for note in noten]  # Korrigiert: Ersetzt Komma durch Punkt für float Konvertierung
    aktueller_durchschnitt = sum(noten_werte) / len(noten_werte)
    for moegliche_note in [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]:
        neuer_durchschnitt = (sum(noten_werte) + moegliche_note) / (len(noten_werte) + 1)
        if neuer_durchschnitt >= 4:
            return moegliche_note
    return 6  # Falls keine Note gefunden wird, die den Durchschnitt auf >= 4 bringt, wird die höchste Note zurückgegeben

def noten_aus_datei_einlesen(dateipfad):
    with open(dateipfad, 'r', encoding='utf-8') as datei:  # encoding='utf-8' kann nötig sein, abhängig von Ihrem System und der Datei
        for zeile in datei:
            teile = zeile.split()
            fach = teile[0]
            noten = teile[1:]
            minimale_note = berechne_minimale_note(noten)
            print(f"Für das Fach {fach} ist eine minimale Note von {minimale_note} erforderlich, um einen Durchschnitt von mindestens 4.0 zu erreichen.")

# Beispielaufruf mit korrektem Pfad als Argument
noten_aus_datei_einlesen("C:/Users/Marco/Desktop/Übung 6/Noten/noten.txt")
