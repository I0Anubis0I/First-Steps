"""
1. Rückgeld  
in einem Programm sind der zu zahlende Betrag und der gezahlte Geldbetrag über 
Konsoleingabe einzugeben. 
Es soll errechnet werden, wie viel Rückgeld der Kunde bekommt. 
Falls der Kunde zu wenig bezahlt hat, soll das Programm eine Warnung ausgeben. 
2. Rabattrechner 
zu einem Preis wird ein Rabatt gewährt. Beide Werte werden über die Konsole angefordert. 
Bei einem Rabatt von mehr als 100% soll eine Meldung ausgegeben werden. 
3. Benzin-Rechner 
mit den Eingaben Literpreis Kraftstoff, verbrauchter Kraftstoff, gefahrene Strecke in km 
sollen die Werte Verbrauch pro 100 km, Kosten pro 100 km und Kosten der Gesamtstrecke 
errechnet und auf die Konsole ausgegeben werden 
"""

#1
while True:
    zuzahlenderbetrag = float(input("Das müssen Sie bezahlen: "))
    gezahlterbetrag = float(input("Das haben Sie bezahlt: "))
    rückgeld = 0
    if zuzahlenderbetrag < gezahlterbetrag:
        rückgeld = round((gezahlterbetrag - zuzahlenderbetrag), 2)
        print(f"Ihr Rückgeld ist {rückgeld} €.")
        break
    elif zuzahlenderbetrag == gezahlterbetrag:
        print("Sie bekommen kein Rückgeld.")
        break
    elif zuzahlenderbetrag > gezahlterbetrag:
        rückgeld = round(zuzahlenderbetrag - gezahlterbetrag)
        print(f"Sie müssen noch {rückgeld} € bezahlen.")
        break
#2
while True:
    rabatt = float(input("Bitte geben Sie einen Rabatt ein: "))
    preis = float(input("Bitte geben Sie einen Preis ein: "))
    rabattierterpreis = round(((preis/100)*(100-rabatt)), 2)
    if rabatt < 100:
        print(f"Für den Preis von {preis} € mit einem Rabatt von {rabatt} % müssen Sie noch {rabattierterpreis}€ zahlen.")
        break
    else:
        print(f"Sie können nicht 100% Rabatt geben!")

#3
literpreis = float(input("Benzinpreis: "))
verbrauchtesbenzin = float(input("Verbrauchtes Benzin in l: "))
gefahrenestrecke = float(input("Gefahrene Strecke in km: "))
hundertkmkosten = round((((verbrauchtesbenzin * literpreis) / gefahrenestrecke) * 100.0), 2)
print(f"Kosten pro 100 km: {hundertkmkosten} €")
verbrauchprohundert = round(((verbrauchtesbenzin / gefahrenestrecke ) * 100), 2)
print(f"Verbrauch pro 100 km: {verbrauchprohundert} Liter")
gesamtstreckenkosten = round((verbrauchtesbenzin * literpreis), 2)
print(f"Kosten der Gesamtstrecke: {gesamtstreckenkosten} €")