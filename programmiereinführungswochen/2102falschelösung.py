begruessung = "Die Begrüßung"
wetterstatus = True

if wetterstatus:
    begruessung = "Hey das Wetter ist sehr schön heute"
    
else:
    begruessung = "Keine Wetterinformationen verfügbar"
    
print(begruessung)

MonateImJahr = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

print("Rate mal, wann ich Geburtstag habe: ")
Monat = input()
if Monat == MonateImJahr[1]:
        print("Richtig geraten! =)")
if Monat == MonateImJahr[0] or [2] or [3] or [4] or [5] or [6] or [7] or [8] or [9] or [10] or [11]:
        print("Leider falsch :(")
else: Monat not in MonateImJahr
print("Das ist ja garkein Monat! :O")
