"""
Sudoku Solver

Schreiben Sie ein Programm, das ein unvollständiges Sudoku-Rätsel löst. 
Ein Sudoku besteht aus einem 9x9-Gitter, das in 3x3-Untergitter unterteilt ist. 
Ziel ist es, das Gitter so zu füllen, dass jede Zeile, jede Spalte und jedes 
3x3-Untergitter die Zahlen von 1 bis 9 ohne Wiederholung enthält.

Anforderungen:

Implementieren Sie eine Funktion, die überprüft, ob eine Zahl in eine 
bestimmte Position im Gitter eingefügt werden kann.
Implementieren Sie eine rekursive Backtracking-Funktion, um das Sudoku zu lösen.
Geben Sie das gelöste Sudoku-Rätsel aus.

Beispiel:
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
"""