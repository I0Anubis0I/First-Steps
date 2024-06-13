"""
1. Ein Dictionary mit den Vornamen und dem Alter (Ganzzahl) von 5 Personen ist zu erstellen. 
Der Vorname ist der Schlüssel und das Alter der Wert in diesem Dictionary. 
Das Dictionary ist als Ganzes auf der Konsole auszugeben. Anschließend sind in einer Schleife 
nacheinander alle Elemente als Schlüssel-Werte-Paar auszugeben. 
2. Eine Person hatte Geburtstag und das Alter dieser Person soll um 1 erhöht werden. Das 
Schlüssel-Werte-Paar zu dieser Person soll vor und nach der Änderung ausgegeben werden. 
3. Alle Namen der Personen sollen ohne Alter auf der Konsole ausgegeben werden. 
4. Für alle Personen im Dictionary soll auch die Telefonnummer ergänzt werden. 
Dazu kann ein weiteres Dictionary angelegt werden, in dem die Schlüssel Geburtsjahr und 
Telefon verwendet werden, z.B. {"Geburtsjahr": 1985, "Telefon": "0151 23456"}. Mit diesen 
Angaben ist die Altersangabe zu überschreiben. Für die weiteren Personen sind diese 
Änderungen ebenfalls vorzunehmen. Das Personen-Dictionary ist komplett auszugeben. 
5. Eine Person hat 2 Telefonnummern. Es ist eine Liste mit den beiden Telefonnummern zu 
erstellen und anschließend der bestehende Eintrag Telefon mit der Liste der 
Telefonnummern zu ersetzen. In einer Schleife sind nacheinander alle Elemente als SchlüsselWerte-Paar auszugeben. 
"""

dictionary1 = {"Thomas" : 41, "Sandra" : 25, "Tanja" : 18, "Mark" : 33, "John" : 65}

print(dictionary1)

for x in dictionary1.items():
    print(x)

print(f"John ist {dictionary1["John"]} Jahre alt")

dictionary1["John"] = 66

print(dictionary1)
print(f"John hatte Geburtstag und ist jetzt {dictionary1["John"]} Jahre alt")


for x in dictionary1:
    print(x)

thomas = {"Geburtsjahr" : "1982", "Telefonnr." : "08459/77344"}
sandra = {"Geburtsjahr" : "1999", "Telefonnr." : "0177/771771"}
tanja = {"Geburtsjahr" : "2006", "Telefonnr." : "08459/3256344"}
mark = {"Geburtsjahr" : "1992", "Telefonnr." : "0177/7734661"}
john = {"Geburtsjahr" : "1977", "Telefonnr." : "01898/6767643"}

dictionary1["Thomas"] = thomas
dictionary1["Sandra"] = sandra
dictionary1["Tanja"] = tanja
dictionary1["Mark"] = mark
dictionary1["John"] = john

print(dictionary1)

johnstel = ["01898/6767643", "0189/55623434534"]

john["Telefonnr."] = johnstel

for person, daten in dictionary1.items():
    telefonnummern = daten["Telefonnr."]
    if isinstance(telefonnummern, list):
        if len(telefonnummern) > 1:
            telefonnummern_str = ", ".join(telefonnummern)
        else:
            telefonnummern_str = telefonnummern[0]
    else:
        telefonnummern_str = telefonnummern
    
    print(f"{person}: Geburtsjahr {daten['Geburtsjahr']}, Telefonnummern: {telefonnummern_str}")
