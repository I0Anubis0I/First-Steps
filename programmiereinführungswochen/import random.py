import random
import datetime
from datetime import date


print("Willkommen Reisender, ich bin die berühmte Wahrsagerin Alessia \nVerrate mir doch deinen Namen und deinen Nachnamen")
name = input("Name: ") 
nachname = input("Nachname: \n")
print("Dein Alter und dein Hobby würde ich auch sehr gerne noch wissen")

#loop ask age, if not integer, ask again
while True:
     try:
          alter = int(input("Alter: "))
          if alter == int(alter):
               break
     except ValueError:
          pass
     
     print("Verrate mir bitte, wie alt du bist!")

diesesJahr = date.today().year
geburtsjahr = diesesJahr - alter

if geburtsjahr >= 2019:
     print(f"Ohh du wurdest im Jahr {geburtsjahr} geboren, das war ein sehr interessantes Jahr!")
if geburtsjahr <= 2018:
     print(f"An das Jahr {geburtsjahr} habe ich einige gute Erinnerungen!")

hobby = input("Hobbie: \n")

print(f"Ahhh, ja, {hobby} ist ein sehr schönes Hobby")
print(f"Nun, {name} {nachname}, was führt dich zu mir?")
print("Ich wette du möchtest dir die Zukunft vorhersagen lassen!")

sterbedatum = random.randint(90, 110)
sterbedatum2 = alter + random.randint(1, 10)
sterbejahr = sterbedatum + date.today().year
sterbejahr2 = sterbedatum2 + date.today().year
ynlist = ["ja", "nein"]

#loop to ask yes or no, give different number according to user input
while True:
    
    yesOrNo = input("Ja oder Nein: ").lower()

    if yesOrNo in ynlist:
       if yesOrNo == ynlist[0]: 
            print(f"Da du nicht gelogen hast, kann ich sagen, dass du ein glückliches Leben führen wirst und erst im hohen Alter von {sterbedatum} im Jahr {sterbejahr} sterben wirst")
            break
       else:
            print(f"Du hast mich belogen! Für so eine Unverschämtheit wirst du bald erkranken und bereits im Alter von {sterbedatum2} im Jahr {sterbejahr2} sterben!!!")
            break
    else:
        print("Entscheide dich! Schreib Ja oder Nein!")
    
