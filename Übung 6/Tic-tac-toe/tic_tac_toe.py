def is_winner(field, symbol):
    # count symbol horizontally
    counts = []
    for row in range(3):
        count = 0
        for col in range(3):
            if field[row][col] == symbol:  # Korrektur für die horizontale Überprüfung
                count += 1
        counts.append(count)

    # count symbol vertically
    for col in range(3):
        count = 0
        for row in range(3):
            if field[row][col] == symbol:  # Korrektur für die vertikale Überprüfung
                count += 1
        counts.append(count)

    # count symbol on first diagonal
    count = 0
    for pos in range(3):
        if field[pos][pos] == symbol:
            count += 1
    counts.append(count)

    # count symbol on second diagonal
    count = 0
    for pos in range(3):
        if field[pos][2-pos] == symbol:  # Korrektur für die zweite Diagonale
            count += 1
    counts.append(count)
    
    # Überprüft, ob irgendein Zähler 3 erreicht
    return max(counts) == 3  # Diese Zeile war korrekt und überprüft effektiv auf einen Sieg

def print_winner(field):
    if is_winner(field, "o"):
        print("'o' hat gewonnen")
    elif is_winner(field, "x"):
        print("'x' hat gewonnen")
    else:
        print("Noch nicht fertig.")

current_field = [["x", "x", "o"], 
                 ["x", "o", "-"], 
                 ["o", "x", "-"]]
print_winner(current_field)
