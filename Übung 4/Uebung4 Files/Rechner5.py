def berechne(zahl1, zahl2, operator):
    """
    Die Funktion berechne führt eine Rechnung basierend auf den gegebenen Zahlen und dem Operator durch.
    """
    if operator == "+":
        return zahl1 + zahl2
    elif operator == "-":
        return zahl1 - zahl2
    elif operator == "*":
        return zahl1 * zahl2
    elif operator == "/":
        if zahl2 != 0:
            return zahl1 / zahl2
        else:
            print("Division durch 0 ist nicht erlaubt.")
            exit()  # Programm beenden, da eine Division durch 0 versucht wurde
    else:
        print("Ungültiger Operator. Bitte nur +, -, *, oder / eingeben.")
        exit()  # Programm beenden, da ein ungültiger Operator eingegeben wurde

# Eingabe der Rechnung als String
eingabe = input("Gib die Rechnung ein (z.B. '4 + 9'): ")

# Trenne die Zahlen und den Operator mit split()
teile = eingabe.split()

# Überprüfe, ob die Eingabe gültig ist
if len(teile) != 3:
    print("Ungültige Eingabe. Bitte die Rechnung mit Leerzeichen trennen (z.B. '4 + 9').")
    exit()

# Extrahiere die Zahlen und den Operator
zahl1 = float(teile[0])
operator = teile[1]
zahl2 = float(teile[2])

# Aufruf der Funktion berechne und Ausgabe der gesamten Rechnung mit Ergebnis
ergebnis = berechne(zahl1, zahl2, operator)
print(f"{eingabe} = {ergebnis}")
