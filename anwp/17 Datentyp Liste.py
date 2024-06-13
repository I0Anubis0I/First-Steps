"""
1. Füge zwei vorher festgelegte Listen zu einer zusammen und gib diese aus 
Beispiel: [3,8,9,2] zusammengefügt mit [4,6] ergibt [3,8,9,2,4,6] 
2. Trenne eine Liste an einem Index in zwei Teillisten. 
Hinweis: Der Index beginnt bei 0. Getrennt wird vor dem Eintrag an der Indexstelle. Soll eine 
Liste an Index 0 getrennt werden, dann ist die erste Liste leer. 
Beispiel: [1,3,5,8,9,3] getrennt an Index 3 ergibt [1,3,5] [8,9,3] 
3. Von der Konsole sind beliebig viele Elemente einzulesen und einer Liste hinzuzufügen 
Mit der Eingabe q soll die Eingabe beendet werden. 
Die Liste ist zur Kontrolle auszugeben; anschließend ist die Liste sortiert auszugeben 
4. Erstelle eine Liste mit den Namen von fünf Großstädten. Diese Liste ist sortiert auszugeben. 
Über die Konsole sollen anschließend zwei weitere Städte zur Eingabe angefordert werden 
und zur Liste hinzugefügt werden. Diese Liste, nun mit 7 Städtenamen, ist wieder zu sortieren 
und anschließend in umgekehrter Reihenfolge auszugeben. Im nächsten Schritt werden die 
erste und die letzte Stadt aus der Liste entfernt und die reduzierte Liste ausgegeben. 
5. Entferne ein bestimmtes Element aus einer festgelegten Liste. 
Hinweis: Kommt ein Element mehr als einmal vor, sollte es überall entfernt werden. 
Beispiel: [3,8,9,5,1,3,6,4] ohne 3 ergibt [8,9,5,1,6,4] 
"""

##a1
liste1 = [3, 8, 9, 2]
liste2 = [4, 6]

liste3 = liste1 + liste2
print(liste1)
print(liste2)
print(liste3)


##a2
liste4 = [1, 3, 5, 8, 9, 3]

liste5 = liste4[0:3]
liste6 = liste4[3:len(liste4)]

print(liste4)
print(liste5)
print(liste6)


##a3
liste7 = []
while True:
    eingabe = input('Bitte fügen Sie Daten zu einer Liste hinzu, mit Q brechen Sie die Eingabe ab: ')
    if eingabe.lower() == "q":
        break
    liste7.append(eingabe)

print(liste7)
liste7.sort()
print(liste7)


##a4
staedte = ['New York', 'Berlin', 'London', 'Los Angeles', 'München']
while True:
    stadt = input('Bitte fügen Sie Städte zu einer Liste hinzu, mit Q brechen Sie die Eingabe ab: ')
    if stadt.lower() == "q":
        break
    staedte.append(stadt)

print(staedte)
staedte.sort(reverse = True)
print(staedte)
staedte.pop(0)
staedte.pop(len(staedte)-1)
print(staedte)


##a5
liste8 = [3, 8, 9, 5, 1, 3, 6, 4, 8, 3]
print(liste8)


for x in liste8:
    if liste8.count(x) > 1:
        while x in liste8:
            liste8.remove(x)

print(liste8)
