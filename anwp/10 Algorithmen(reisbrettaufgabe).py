"""
1. Multiplikation zweier Zahlen x und y-  
kann auch als x-maliges Addieren der Zahl y gelöst werden: 
z.B. 3 *4 = 4 + 4+ 4 = 12 
für diese Berechnung ist eine iterative Lösung (mit einer Schleife) zu erstellen. 
Die jeweiligen Werte für die Zahlen x und y werden über die Konsole eingegeben. 
2. Multiplikation zweier Zahlen x und y-  
für diese Berechnung ist rekursive Lösung (keine Schleife) zu erstellen. 
Die jeweiligen Werte für die Zahlen x und y werden über die Konsole eingegeben. 
3. Weizenkörner -  
auf einem Schachbrett liegen Körner – auf dem ersten Feld liegt ein Korn, auf dem zweiten 
Feld liegen zwei Körner - die Zahl der Körner soll sich von Feld zu Feld jeweils verdoppeln. 
Die Anzahl der Körner auf dem Schachbrett ist mit einem beliebigen Algorithmus, iterativ 
oder rekursiv, zu berechnen. 
"""

# iterativ
def addieren(x, y):
    ergebnis = 0
    for i in range(1, y+1):
        ergebnis += x
    return ergebnis
print(addieren(3, 5))

# rekursiv
def addieren1(x, y):
    if x > 1:
        return y + addieren1(x-1, y)
    else:
        return y   
print(addieren1(4, 7))



def fullboard(fb):
    i = 1
    rice = 0
    for i in range(1, 65):
        rice += fb
        print(f'Ab Feld {i} ist die Summe aller Reiskörner auf dem Schachbrett {rice} Reiskörner')
        rice *= 2
    return rice
(fullboard(1))

def singlefield(sf):
        i = 1
        onefieldrice = sf
        for i in range(1, 65):
             print(f'Auf Feld {i} befinden sich {onefieldrice} Reiskörner')
             onefieldrice += onefieldrice
        return onefieldrice
singlefield(1)