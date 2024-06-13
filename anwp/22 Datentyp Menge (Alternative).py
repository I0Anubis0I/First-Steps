text = """Textanalyse der Text dieser Aufgabenstellung soll untersucht werden:
o Für alle im Text vorkommenden Buchstaben soll die Anzahl ermittelt werden und
diese Übersicht absteigend sortiert nach der Anzahl ausgegeben werden.
o Eine weitere Untersuchung soll ermitteln, wie viele Vokale (a, e, i, o, u) im Text
gefunden werden."""

def buchstaben_anzahl(text):
    zeichenmenge = set(text)

    zeichen_dict = dict.fromkeys(zeichenmenge)

    for i in zeichen_dict.keys():
        zeichen_dict[i] = text.count(i)

    zeichen_liste = list(zeichen_dict.items())

    zeichen_liste.sort(key=lambda x:x[1], reverse=True)

    for i in dict(zeichen_liste).items():
        print(i)

buchstaben_anzahl(text)


def anzahl_vokale(text):
    vokale = ["a", "e", "i", "o", "u"]

    summe_vokale = 0
    for i in vokale:
        print(f"{i} {text.count(i)}")
        summe_vokale += text.lower().count(i)
    print(f"Insgesamt hat der Text {summe_vokale} Vokale")

anzahl_vokale(text)