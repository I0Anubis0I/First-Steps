"""Aufgabe 
1. Tic-Tac-Toe - 
die Ausgabe des Spielfeldes soll mit Hilfe von Formatierungsangaben erfolgen. 
2. Pyramide - 
erzeuge ein Programm zur Ausgabe einer Pyramide auf der Konsole, wobei Höhe und Breite 
frei wählbar sind; als Benutzereingabe über die Konsole; z.B. Höhe = 4 und Breite = 10 
 ** 
 **** 
 ****** 
******** 
3. Tannenbaum - 
erzeuge ein Programm zur Ausgabe eines Tannenbaums auf der Konsole, wobei Höhe und 
Breite frei wählbar sind; als Benutzereingabe über die Konsole; z.B. Höhe = 4 und Breite = 10 
 ** 
 **** 
 ****** 
******** 
 **"""

# tictactoe
flatline = '_'
empty = ''
field = ""

print(f" {5*flatline:6}{5*flatline:6}{5*flatline:6}")
print(f"|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|")
print(f"|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|")
print(f"|{5*flatline:5}|{5*flatline:5}|{5*flatline:5}|")
print(f"|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|")
print(f"|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|")
print(f"|{5*flatline:5}|{5*flatline:5}|{5*flatline:5}|")
print(f"|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|")
print(f"|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|{empty:2}{field:1}{empty:2}|")
print(f"|{5*flatline:5}|{5*flatline:5}|{5*flatline:5}|")
print("")
#Pyramide
brick = "*"
print(f"{1*brick:^10}")
print(f"{3*brick:^10}")
print(f"{5*brick:^10}")
print(f"{7*brick:^10}")
print(f"{9*brick:^10}")
print("")
#tannenbaum
tree = "@"
print(f"{2*tree:^10}")
print(f"{4*tree:^10}")
print(f"{6*tree:^10}")
print(f"{8*tree:^10}")
print(f"{2*tree:^10}")