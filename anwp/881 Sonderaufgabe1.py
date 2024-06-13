"""
1. Schreiben Sie ein Programm, das alle ungeraden Zahlen bis einschließlich 147 
und anschließend die Zahl 3.1415 ausgibt. Stellen Sie sicher, dass 3.1415 nur einmal ausgegeben wird!

2. Kofferpacken: Sie haben eine Liste von Gegenständen, genauer deren Gewicht, gegeben.
Das heißt, Gegenstand 0 hat ein Gewicht von 2 Kilogramm, Gegenstand 1 hat Gewicht 7 Kilogramm usw.
Außerdem haben Sie einen Koffer, der ein Gewicht von 50 Kilogramm tragen kann.
Ziel von Kofferpacken ist es, die Gegenstände von vorne nach hinten anzuschauen 
und einen Gegenstand in den Koffer zu packen, sofern er noch hineinpassen.
Schreiben Sie also ein Programm, das die Einträge der Liste durchläuft und für 
jeden Eintrag überprüft, ob es noch ausreichende Kapazität gibt. Passt der Gegenstand 
noch in den Koffer, dann geben Sie das Gewicht mit `print()` aus und passen die Kapazität an:
Packen wir einen Gegenstand mit Gewicht 5 in einen Koffer mit Kapazität 50, so verringert 
sich die Kapazität um 5, von 50 auf 45. Vorsicht! Die Kapazität kann nicht kleiner als 0 sein!
Ist der Eintrag größer als die Kapazität, machen Sie nichts mit dem Eintrag.
gegenstaende = [2,7,13,5,24,5,14,17,5,3]
kapazitaet = 50

3. Vervollständigen Sie das Programm so, dass alle Elemente der Liste bis zum ersten Auftauchen 
von "Ende" ausgegeben werden. Dabei soll "Ende" selbst nicht ausgegeben werden.

liste = ["Vervollständigen", "Sie", "das", "Programm", "so", "dass", "alle", "Elemente", 
"der", "Liste", "bis", "zum", "ersten", "Auftauchen", "von", "Ende", "ausgegeben", "werden." 
"Dabei", "soll", "Ende", "selbst", "nicht", "ausgegeben", "werden."]

Verwenden Sie dabei **keine Listendindizes!**

4. Modifizieren Sie Ihr Programm von Aufgabe 3 so, dass alle Elemente bis zum zweiten Auftauchen 
von "Ende" ausgegeben werden. "Ende" selbst soll dabei weiterhin nicht ausgegeben werden.

5. Schreiben Sie ein Programm, das den Nutzer wiederholt auffordert eine Zahl oder "quit" einzugeben. 
Gibt der Nutzer eine Zahl `x` ein, soll "Echo + x" ausgegeben werden.

Ist die Nutzereingabe 5, so ist die Ausgabe des Programms:
Echo 5

Danach beginnt der Prozess von vorne und der Nutzer wird erneut nach einer Zahl oder "quit" gefragt.
Gibt der Nutzer allerdings "quit" ein, so wird das Programm beendet.
"""