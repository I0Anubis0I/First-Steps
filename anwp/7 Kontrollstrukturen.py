"""
1. Einmaleins der Zahl 9 
das kleine Einmaleins der Zahl 9 ist über eine Schleife auf der Konsole auszugeben. 
2.  Fakultät, in der Mathematik geschrieben mit ! hinter der Zahl, ist definiert als 
o 0! = 1 
o 1! = 1 
o 2! = 2 * 1 = 2 
o 3! = 3 * 2 *1 = 6 
o n! = 1 * 2 * 3* … * (n-1) * n 
Von der Konsole ist eine Zahl einzulesen, für die über eine Schleife die Fakultät berechnet 
und ausgegeben wird. 
3. Es ist ein Programm zur Kapitalberechnung zu erstellen. 
o Über die Konsole werden das Anfangskapital und der Zinssatz zur Eingabe 
angefordert. 
o Es ist das Endkapital nach einem und nach 2 Jahr zu mit der foglenden Formel zu 
berechnen: 
K1 = K0*((p/100)+1)  
K0 = Anfangskapital 
p = Zinssatz 
K1 = Endkapital nach einem Jahr 
Zur Berechnung des Endkapitals des zweiten Jahrs nimmt man das Endkapital von 
ersten Jahr als Anfangskapital. 
"""
#1
for i in range(1, 11):
    result = i * 9
    print(f"{i} x 9 = {result}")
    
#2
nvariable = 4
fakultaet = 1
reihe = "1"
for i in range(2, nvariable + 1):
    fakultaet *= i
    reihe += f" * {i}"
print(f"{nvariable}! = {reihe} = {fakultaet}")

#3 Kapitalberechnung

jahre = float(input('Geben Sie an, wieviel Jahre Sie sparen möchten: ' ))
zinssatz = float(input('Geben Sie den Zinssatz ein: ' ))
anfangskapital = float(input('Geben Sie Ihr Anfangskapital ein: ' ))

i = 0
kapital = anfangskapital
jahr = 1
while jahr <= jahre:
    zinsen = kapital*(zinssatz/100)
    kapital += zinsen
    print(f'Nach {jahr} Jahren sind Sie bei {round(kapital,2)} Kapital')
    jahr += 1
