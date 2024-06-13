begruessung = "Die Begrüßung"
wetterstatus = True

if wetterstatus:
    begruessung = "Hey das Wetter ist sehr schön heute"
    
else:
    begruessung = "Keine Wetterinformationen verfügbar"
    
print(begruessung)

MonthAYear = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

while True:

    month_input = input("Rate mal, wann ich Geburtstag habe: ")

    if month_input in MonthAYear:
        if month_input == MonthAYear[1]:
            print(f"Richtig geraten, mein Geburtstag ist im {month_input}")
            break
        else:
            print("Leider falsch geraten :(")
    else:
        print(month_input, "ist ja garkein Monat!")
