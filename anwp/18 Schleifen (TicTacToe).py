"""
1. Tic Tac Toe 
Das Spiel Tic Tac Toe (Drei-gewinnt) ist mit Python zu programmieren. 
o Es gibt 2 Spieler, die abwechselnd in einem 3x3 großen Spielfeld ein x bzw. ein o
setzen. 
o Wer zuerst 3 Felder in einer Reihe, einer Spalte oder in der Diagonalen belegt, hat 
gewonnen. 
o Das Spielfeld sollte im Programm über den Datentyp Liste abgebildet werden 
o Bei der Programmerstellung sollten folgende Funktionalitäten beachtet werden 
 Hauptroutine festlegen 
 Spielfeld erstellen und ausgeben 
 Spielzug erfassen 
 Spielzug in das Spielfeld einarbeiten 
 Sieger ermitteln 
 Spiel vorzeitig beenden
"""

def wincondition(figur):
    win = False
    if pf[1] and pf[2] and pf[3] == figur:
        win = True
    if pf[1] and pf[4] and pf[7] == figur:
        win = True
    if pf[1] and pf[5] and pf[9] == figur:
        win = True
    if pf[2] and pf[5] and pf[8] == figur:
        win = True
    if pf[3] and pf[6] and pf[9] == figur:
        win = True
    if pf[3] and pf[5] and pf[7] == figur:
        win = True
    if pf[4] and pf[5] and pf[6] == figur:
        win = True
    if pf[7] and pf[8] and pf[9] == figur:
        win = True

def playfieldprint(pf):
    print("<><>--------------<><>".center(40))
    print(f"{pf[0]}{pf[1]}{pf[0]}{pf[2]}{pf[0]}{pf[3]}{pf[0]}".center(40))
    print(f"{pf[0]}{pf[4]}{pf[0]}{pf[5]}{pf[0]}{pf[6]}{pf[0]}".center(40))
    print(f"{pf[0]}{pf[7]}{pf[0]}{pf[8]}{pf[0]}{pf[9]}{pf[0]}".center(40))
    print("<><>--------------<><>".center(40))

def playerfigur(pl):
    if pl == 1:   
        return "X"
    else: return "O"

def playerinput(pi):
    figur = playerfigur(pl)
    pf.pop(pi)
    pf.insert(pi, figur)

print(f"Willkommen zu Tic Tac Toe".center(40))



pf = ["|", "X", " ", " ", "O", "X", " ", " ", " ", " "]
playfieldprint(pf)
print("Dies sind die gültigen Felder,".center(40))
print("die Spieler 1 oder Spieler 2 ".center(40))
print("eingeben können!".center(40)) 
pf = ["|", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
playfieldprint(pf)
print("Spieler 1 ist Figur X".center(40))
print("Spieler 2 ist Figur O".center(40))
print("Kann ein Spieler 3 seiner Figuren".center(40))
print("in eine Reihe bringen,".center(40))
print("vertikal, horizontal oder diagonal,".center(40))
print("dann hat dieser gewonnen!".center(40))
print("Viel Spaß beim Spielen!".center(40))
print("Mit der Eingabe von Q können".center(40))
print("Sie das Spiel jederzeit beenden".center(40))
pf = ["|", " ", " ", " ", " ", " ", " ", " ", " ", " "]

pl = 1

playfieldprint(pf)

fy = int(input("Spieler 1: Gib ein Feld an: "))
playerinput(fy)
playfieldprint(pf)


field = input("Spieler 2: Gib ein Feld an: ")
playfieldprint(pf)