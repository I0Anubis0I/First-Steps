"""
1. Variablen deklarieren und ausgeben  
für Name, Vorname und Einwohnerzahl des Wohnortes sind Variablen zu deklarieren und 
entsprechende Werte zuzuweisen. 
Diese Werte sollen ausgegeben werden; z.B.: 
Ben Müller wohnt in einer Stadt mit 50000 Einwohnern 
Weitere Variablen für Name, Vorname und Einwohnerzahl des Wohnortes sind zu 
deklarieren und mit anderen Werten zu belegen (zuzuweisen). 
Diese Werte sollen ausgegeben werden; z.B.: 
Ben Müller wohnt in einer Stadt mit 50000 Einwohnern 
Joe Lehmann wohnt in einer Stadt mit 10000 Einwohnern 
Die beiden Städte haben zusammen 60000 Einwohner 
"""
name1 = "Ben"
nachname1 = "Müller"
einwohnerzahl1 = "50000"

print(f"{name1} {nachname1} wohnt in einer Stadt mit {einwohnerzahl1} Einwohnern.")

name2 = "Joe"
nachname2 = "Lehmann"
einwohnerzahl2 = "10000"

print(f"{name2} {nachname2} wohnt in einer Stadt mit {einwohnerzahl2} Einwohnern.")

gesamteinwohner = int(einwohnerzahl1) + int(einwohnerzahl2)

print(f"Zusammen haben die beiden Städte {gesamteinwohner} Einwohner.")