"""
1. Countdown 
Es ist eine Funktion zu definieren, die durch Aufruf der Funktion selbst von einem Startwert 
bis 0 herunterzählt und diese Werte auf der Konsole ausgibt. 
2. Messreihe 
Aus einer Messreihe wurden 100 ganzzahlige Werte in einer Liste gespeichert. Für die 
Messwerte sollen verschiedene statistische Kenndaten ermittelt werden: 
a. Berechnung des Minimums der Messwerte 
b. Berechnung des Maximums der Messwerte 
c. Berechnung des Medians der Messwerte 
Hinweis: der Wert aus der Mitte der sortierten Liste 
d. Berechnung der Spannweite der Messwerte 
Hinweis: der Abstand zwischen dem kleinsten und dem größten Wert 
e. Berechnung der mittleren Abweichung der Messwerte 
Hinweis: für alle Werte ist der positive Abstand zum Mittelwert zu bilden 
diese Abstände werden aufsummiert und durch die Anzahl der 
Werte geteilt 
Beispiel für 3 Werte: 
Werte  
Mittelwert 
3, 7, 2 
(3+7+2) / 3 = 4 
mittlere Abw. (|3-4|+|7-4|+|2-4|) / 3 = (1+3+2) / 3 = 2 
f. 
Berechnung des Wertes, der am häufigsten vorkommt 
Hinweis zur Erzeugung der 100 Messwerte: 
# Standardmodul random einbinden 
import random 
messwerte = random.choices(range(0,1000), k=100) 
"""

#1
def countdown(x):
    for x in range(0, x + 1)[::-1]:
        print(x)
        x - 1

countdown(2)
print(f"\n\n")

#2
def berechne_minimum(liste):
    minimum = liste[0]
    for wert in liste:
        if wert < minimum:
            minimum = wert
    return minimum

def berechne_maximum(liste):
    maximum = liste[0]
    for wert in liste:
        if wert > maximum:
            maximum = wert
    return maximum

def berechne_median(liste):
    sortierteliste = sorted(liste)
    median = sortierteliste[49]
    return median

def berechne_spannweite(liste):
    sortierteliste = sorted(liste)
    spannweite = sortierteliste[-1] - sortierteliste[0]
    return spannweite

def berechne_mittelwert_iterativ(liste):
    summe = 0
    for wert in liste:
        summe += wert
    mittelwert = summe / len(liste)
    return mittelwert

#zum Sortieren, wenn sorted Funktion nicht erlaubt ist:
# def bubbleSort(nlist):
#     for passnum in range(len(nlist)-1,0,-1):
#         for i in range(passnum):
#             if nlist[i]>nlist[i+1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i+1]
#                 nlist[i+1] = temp



liste1 = [25, 56, 48, 79, 82, 45, 62, 18, 73, 67, 95, 34, 23, 81, 51, 64, 77, 36, 53, 41, 
             27, 86, 98, 91, 39, 58, 49, 32, 70, 55, 61, 72, 66, 87, 20, 46, 31, 59, 94, 47, 
             78, 40, 57, 60, 29, 68, 75, 84, 35, 33, 37, 21, 28, 30, 63, 71, 90, 88, 42, 50, 
             44, 76, 26, 22, 89, 38, 74, 54, 43, 52, 65, 83, 99, 24, 85, 92, 19, 69, 93, 17, 
             80, 97, 13, 14, 15, 16, 12, 10, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(berechne_minimum(liste1))
print(berechne_maximum(liste1))
print(berechne_median(liste1))
print(berechne_spannweite(liste1))
print(berechne_mittelwert_iterativ(liste1))
