"""
1. Tupel erstellen und ausgeben 
es ist ein Tupel mit 5 Obstsorten (Datentyp str) zu erstellen und auf der Konsole auszugeben 
2. weitere Tupel 
zwei weitere Tupel sind zu erstellen, das eine enthält 4 Milchprodukte und einem leeren 
String, das andere 2 Backwaren. Beide Tupel sind auf der Konsole nacheinander auszugeben. 
3. mehrere Tupel zusammenfügen 
alle 3 Tupel sind in einem neuen Tupel zusammenzufügen. Auf der Konsole ist das Tupel 
selbst, sowie der Datentyp des Tupels (Hinweis: type() ) auszugeben. Weiterhin sind das erste 
und das letzte Element des Tupels sowie deren Typ auszugeben 
4. Lösung überarbeiten 
Folgende Aufgabe wurde bereits gelöst: 
Für eine Nachricht soll von einem Programm automatisch die Anrede formuliert werden. Von 
der Konsole sind Eingaben für Name, Geschlecht und die Uhrzeit als Stundenangabe 
einzulesen  Die Anrede soll je nach Tageszeit mit „Guten Morgen“ (0–9 Uhr), „Guten Tag“ 
(10–17), „Guten Abend (18–0 Uhr) beginnen und anschließend mit „Herr xxx“ bzw. „Frau xxx“ 
fortgesetzt werden. Für xxx soll der entsprechende Name eingesetzt werden 
Das Programm ist so anzupassen, dass die Überprüfung auf gültige Eingaben (wie z.B.: m, w, 
d, M, Mann, f, Frau, …) mit Hilfe eines Tupels der zugelassen Werte durchgeführt wird. 
Ebenfalls sollen die Begrüßungsformeln (Guten Morgen, Guten Tag und Guten Abend) in 
einem Tupel definiert werden und die Anrede mit entsprechenden Zugriffen daraus 
zugesetzt werden. 
"""

#1
obstsorten = ("Apfel", "Mandarine", "Kirsche", "Himbeere", "Ananas")
print(obstsorten)
#2
milchprodukte = ("Käse", "Sahne", "Joghurt", "Quark", "")
backwaren = ("Brezeln", "Brot")
print(milchprodukte, backwaren)
#3
lebensmittel = milchprodukte + backwaren + obstsorten
print(f"Datentyp: {type(lebensmittel)}, Daten im Tupel: {lebensmittel}.\n")
print(f"Erstes Element im Tupel: {lebensmittel[0]}, Datentyp: {type(lebensmittel[0])}. Letztes Element im Tupel: {lebensmittel[-1]}, Datentyp: {type(lebensmittel[-1])}.")
#4
while True:
    try:
        uhrzeit_input = input("Wieviel Uhr ist es? (oder 'q' zum Beenden): ")
        if uhrzeit_input.lower() == 'q':
            print("Programm beendet.")
            break
        uhrzeit = int(uhrzeit_input)
        if 0 <= uhrzeit <= 23:
            tageszeiten = [(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), (10, 11, 12, 13, 14, 15, 16, 17), (18, 19, 20, 21, 22, 23)]
            tagesgruss = ("Guten Morgen", "Guten Tag", "Guten Abend")
            geschlecht = input("Wie darf ich Sie ansprechen? (m, f, d): ")
            male = ("m", "Herr")
            female = ("f", "Frau")
            divers = ("d", "")
            name = input("Wie ist Ihr Name?: ")
            if uhrzeit in tageszeiten[0]:
                if geschlecht.lower() in male:
                    print(tagesgruss[0], male[1], name)
                elif geschlecht.lower() in female:
                    print(tagesgruss[0], female[1], name)
                else:
                    print(tagesgruss[0], name)
            elif uhrzeit in tageszeiten[1]:
                if geschlecht.lower() in male:
                    print(tagesgruss[1], male[1], name)
                elif geschlecht.lower() in female:
                    print(tagesgruss[1], female[1], name)
                else:
                    print(tagesgruss[1], name)
            elif uhrzeit in tageszeiten[2]:
                if geschlecht.lower() in male:
                    print(tagesgruss[2], male[1], name)
                elif geschlecht.lower() in female:
                    print(tagesgruss[2], female[1], name)
                else:
                    print(tagesgruss[2], name)
            else:
                break    
        else:
            print("Bitte gib eine Uhrzeit zwischen 0 und 23 ein.")
    except ValueError:
        print("Bitte gib eine ganze Zahl ein.")
