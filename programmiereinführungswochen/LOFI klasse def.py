#text = "Ich bin ein Text"
#alter = 6
#def ausgabe():
#    print(text)
#    print(alter)

#ausgabe()

#objektorientierte Version

class ersteKlasse:   #Datenstruktur
    def __init__(self):        #Konstruktor
        self.text = "Ich bin ein Text"
        self.alter = 6

    def ausgabe(self):
        print(self.text)
        print(self.alter)

dieErsteKlasse = ersteKlasse()
dieErsteKlasse.ausgabe()

