''' 
 Min-Max-Berechnung 
von der Konsole sind nacheinander drei Gleitpunktzahlen einzulesen 
es ist die kleinste und die größte Zahl zu ermitteln und jeweils auszugeben 
für die Berechnung sind bedingte Anweisungen (if) bzw. Verzweigungen (if … elif … else) zu 
verwenden 
 Tipp-Spiel 
für ein Fußballtippspiel sind die erzielten Punkte zu ermitteln 
Hinweis: mit Hilfe von Variablen wie heim und gast, sowie tipp_heim und tipp_gast
könnten die erforderlichen Vergleiche durchgeführt werden 
Wertung: 
o exakter Tipp 3 Punkte 
o richtige Tendenz 1 Punkt 
Testfälle: 
o Ergebnis: 3:2 Tipp 3:2 3 Punkte 
o Ergebnis: 0:1 Tipp 0:1 3 Punkte 
o Ergebnis: 2:1 Tipp 3:0 1 Punkte 
o Ergebnis: 2:2 Tipp 1:1 1 Punkte 
o Ergebnis: 2:1 Tipp 3:0 1 Punkte 
o Ergebnis: 2:1 Tipp 0:3 0 Punkte 
'''

#1
floatlist = []
while True:
    try:
        if len(floatlist) >= 3:
            print("Die Liste hat bereits 3 Zahlen aufgenommen.")
            break
        floatzahleninput = input("Bitte geben Sie Kommazahlen ein: ")
        if floatzahleninput.lower() == "q":
                break
        floatzahl = float(floatzahleninput)
        floatlist.append(floatzahl)
    except ValueError:
        print("Falsche Eingabe!")
print(floatlist)

groesstezahl = floatlist[0]
if floatlist[1]> groesstezahl:
     groesstezahl = floatlist[1]
elif floatlist[2]> groesstezahl:
     groesstezahl = floatlist[2]
print(groesstezahl)

kleinstezahl = floatlist[0]
if floatlist[1]< kleinstezahl:
     kleinstezahl = floatlist[1]
elif floatlist[2]< kleinstezahl:
     kleinstezahl = floatlist[2]
print(kleinstezahl)

#2

spiel1 = {"Heim" : 3, "Gast" : 2}
spiel2 = {"Heim" : 0, "Gast" : 1}
spiel3 = {"Heim" : 2, "Gast" : 1}
spiel4 = {"Heim" : 2, "Gast" : 2}
spiele = [spiel1, spiel2, spiel3, spiel4]

tipp_heim = int(input("Geben Sie einen Tipp ab für die Heimmannschaft: "))
tipp_gast = int(input("Geben Sie einen Tipp ab für die Gastmannschaft: "))
spieleingabe = int(input("Für welches Spiel möchten Sie tippen(1-4): "))
#testfälle:
heim = spiele[spieleingabe-1]["Heim"]
gast = spiele[spieleingabe-1]["Gast"]
if heim > gast:
     if heim == tipp_heim and gast == tipp_gast:
          print("3 Punkte")
     elif tipp_heim > tipp_gast:
          print("1 Punkt")
     else:
          print("0 Punkte")
elif heim < gast:
     if heim == tipp_heim and gast == tipp_gast:
          print("3 Punkte")
     elif tipp_heim < tipp_gast:
          print("1 Punkt")
     else:
          print("0 Punkte")
elif heim == gast:
     if heim == tipp_heim and gast == tipp_gast:
          print("3 Punkte")
     elif tipp_heim == tipp_gast:
          print("1 Punkt")
     else:
          print("0 Punkte")

