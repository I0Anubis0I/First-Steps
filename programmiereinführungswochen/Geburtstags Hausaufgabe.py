monatsliste = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

for geburtsmonat in monatsliste:
    print("Das sind die Monate im Jahr:", geburtsmonat)
    if geburtsmonat == monatsliste[1]:
        print("Ich habe im", geburtsmonat ,"geburtstag")
       


DasJahr = ["Januar", "Februar", "März", "April" ,"Mai" ,"Juni" ,"Juli" ,"August" ,"September" ,"Oktober" ,"November" ,"Dezember", "Terziember"]

for Monat in DasJahr:
    print(Monat, ", das ist nicht Geburtsmonat")
    if Monat == DasJahr[11]:
        print(Monat, ", das ist mein Geburtsmonat")
        break
