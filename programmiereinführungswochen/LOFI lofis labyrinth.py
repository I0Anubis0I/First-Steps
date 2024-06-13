
def schritt():
    print("Lofi macht einen Schritt")

# schritt()       #funktionsaufruf

def drehRechts():
    print("Lofi dreht sich nach rechts")

#sequenz
drehRechts()
schritt()
drehRechts()
schritt()
schritt()
drehRechts()
schritt()
schritt()
schritt()
drehRechts()
schritt()
schritt()
schritt()
schritt()
print("\nWhile Schleife")
i=1
#iteration, wie funktioniert eine while schleife
while i <=3:
    schritt()
    i+=1

print("\nFor Schleife")
#wie funktioniert eine for schleife
for i in range(3):
    schritt()
    i+=1
vielHunger = False
print("\nIf Bedingung")
#wie funktioniert die if bedingung
if vielHunger == True:
    print("Lofi isst das Kleeblatt")

print("\nIf und Elif")
#if oder elif
willTun = "Essen"

if willTun == "Essen":
    print("Lofi isst Kleeblatt")
elif willTun == "Überraschung":
    print("Lofi öffnet das Geschenk")
elif willTun == "Besuch":
    print("Lofi besucht einen Freund")
elif willTun == "Spielen":
    print("Lofi geht spielen")


