"""
1. Visitenkarte 
über die Konsole werden die Personendaten (Vorname, Nachname, Straße, Ort und 
Telefonnr.) erfasst  
Diese Daten sind wie folgt auszugeben:  
Name:     
Heinrich Müller 
Strasse:  Luisenstr. 5 
Ort:      
Düsseldorf 
Telefon:  123456 
"""

#1
vskname = "Name:"
vskstrasse = "Straße:"
vskort = "Ort:"
vsktelefonnr = "Telefon:"
inputname = input("Bitte geben Sie Ihren Namen ein: ")
inputstrasse = input("Bitte geben Sie Ihre Straße ein: ")
inputort = input("Bitte geben Sie Ihren Wohnort ein: ")
inputtelefon = input("Bitte geben Sie Ihre Telefonnummer ein: ")
print(f"{vskname:15}{inputname}")
print(f"{vskstrasse:15}{inputstrasse}")
print(f"{vskort:15}{inputort}")
print(f"{vsktelefonnr:15}{inputtelefon}")