text = """
Textanalyse 
der Text dieser Aufgabenstellung soll untersucht werden: 
o Für alle im Text vorkommenden Buchstaben soll die Anzahl ermittelt werden und 
diese Übersicht absteigend sortiert nach der Anzahl ausgegeben werden. 
o Eine weitere Untersuchung soll ermitteln, wie viele Vokale (a, e, i, o, u) im Text 
gefunden werden.
"""

def analytics1(testtext):
    kleinbuchstaben = testtext.lower()
    buchstaben = [char for char in kleinbuchstaben if char.isalpha()]
    buchstabenanzahl = {}
    for buchstabe in buchstaben:
        if buchstabe in buchstabenanzahl:
            buchstabenanzahl[buchstabe] += 1
        else:
            buchstabenanzahl[buchstabe] = 1
    sortiertebuchstaben = sorted(buchstabenanzahl.items(), key = lambda x: x[1], reverse=True)
    for buchstabe, anzahl in sortiertebuchstaben:
        print(f"{buchstabe}:{anzahl}")

analytics1(text)

def analytics2(testtext):
    vokale = "aeiou"
    vokalanzahl = 0
    for i in testtext.lower():
        if i in vokale:
            vokalanzahl += 1
    return vokalanzahl

print(f"Im Testtext befinden sich {analytics2(text)} Vokale.")