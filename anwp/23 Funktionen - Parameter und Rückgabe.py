"""
Umdrehen 
Es sind Funktionen zu definieren, mit denen die Reihenfolge der einzelnen Elemente in 
Zeichenketten, Listen, und Tupel umgedreht werden bzw. für Zahlen soll das Vorzeichen 
umgedreht werden. 
Mit Testdaten der Datentypen Ganzzahl, Gleitpunktzahl, Zeichenkette, Liste und Tupel soll 
getestet werden – auf der Konsole sind die Werte vor dem Umdrehen und nach dem 
Umdrehen auszugeben 
"""

def turn(testdata):
    testresult = 0
    if isinstance(testdata, (str, tuple)):
        testresult = testdata[::-1]
        # testresult = tuple(reversed(testdata))
    if isinstance(testdata, (int, float)):
        testresult = -testdata
    if isinstance(testdata, list):
        testdata.reverse()
        testresult = testdata       
    return testresult

def usertest(eingabe):
    if len(eingabe) == 1:
        item = eingabe[0]
        try:
            return int(item)
        except ValueError:
            pass
        try:
            return float(item)
        except ValueError:
            pass
        try:
            return str(item)
        except ValueError:
            pass
        return item
    else:
        return eingabe            
         
while True:
    datenfrage = input("Möchtest du Daten eingeben Ja oder Nein:")
    fragelisteyes = ["yes", "y", "ja", "j"]
    fragelisteno = ["no", "n", "nein"]
    if datenfrage.lower() in fragelisteyes:
        userlist = []
        while True:
            userinput = input('Bitte geben Sie Daten ein, mit Q brechen Sie die Eingabe ab: ')
            if userinput.lower() == "q":
                break 
            userlist.append(userinput)
      
        new = usertest(userlist)
        print("\n\n")
        print(f"{type(turn(new))} vorm Umdrehen: {new}. Nach dem Umdrehen: {turn(new)}")
        print("\n\n")
    elif datenfrage.lower() in fragelisteno:
        break


string1 = "Tomatensalat"
print(f"String vorm Umdrehen: {string1}. Nach dem Umdrehen: {turn(string1)}\n")
int1 = -24
print(f"Integer vorm Umdrehen: {int1}. Nach dem Umdrehen: {turn(int1)}\n")
float1 = 24.77
print(f"Float vorm Umdrehen: {float1}. Nach dem Umdrehen: {turn(float1)}\n")
list1 = [1, 2, 3, 4]
print(f"Liste vorm Umdrehen: {list1}. Nach dem Umdrehen: {turn(list1)}\n")
tuple1 = (1, 2, 3, 4)
print(f"Tuple vorm Umdrehen: {tuple1}. Nach dem Umdrehen: {turn(tuple1)}\n")




