import hashlib
import csv

def hash_name(name):
    """Generiert einen eindeutigen Hash für einen Namen."""
    hash_object = hashlib.sha256(name.encode())
    return hash_object.hexdigest()

def main():
    names = []  # Hier könnten die Namen eingelesen werden
    hashed_names = []

    # Pfad für die CSV-Datei
    csv_file_path = 'C:/Users/Marco/Desktop/Übung 6/Hash/hashed_names.csv'  # Beispiel-Pfad, an deine Bedürfnisse anpassen

    # Beispiel: Eingabe der Namen über die Kommandozeile
    while True:
        name = input("Gib einen Namen ein (oder 'ende' zum Beenden): ")
        if name == 'ende':
            break
        names.append(name)

    # Erzeugung der eindeutigen Strings
    for name in names:
        hashed_names.append((name, hash_name(name)))

    # Speichern der Namen und ihrer Hashes in der angegebenen CSV-Datei
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Original Name', 'Hashed Name'])
        writer.writerows(hashed_names)

    print(f"Die Namen wurden erfolgreich gehasht und in '{csv_file_path}' gespeichert.")

if __name__ == "__main__":
    main()
