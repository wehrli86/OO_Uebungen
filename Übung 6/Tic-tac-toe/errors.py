def is_winner(field, symbol):
    # count symbol horizontally
    counts = []
    for row in range(3):
        count = 0
        for col in range(3):
            if field[col][row] == symbol:  # Fehler 1
                count = count + 1
        counts.append(count)

    # count symbol vertically
    for col in range(3):
        count = 0
        for row in range(3):
            if field[col][row] == symbol:  # Fehler 2 (identisch zu Fehler 1, aber Kontext ist vertikale Zählung)
                count = count + 1
        counts.append(count)

    # count symbol on first diagonal
    count = 0  # Dies sollte außerhalb der Schleife sein
    for pos in range(3):
        if field[pos][pos] == symbol:
            count = count + 1
    counts.append(count)  # Fehlte

    # count symbol on second diagonal
    count = 0  # Reset für zweite Diagonale
    for pos in range(3):
        if field[2-pos][pos] == symbol:  # Fehler 3
            count = count + 1
    counts.append(count)  # Fehlte
    
    return max(counts) == 3  # Fehler 4
