"""
Aufgabe: Textanalyse-Tool

Schreiben Sie ein Programm, das eine Textdatei analysiert und verschiedene Statistiken 
über den Text ausgibt. Das Programm soll die häufigsten Wörter, die Anzahl der Sätze, 
die durchschnittliche Wortlänge und die durchschnittliche Satzlänge ermitteln.

Anforderungen:

    Lesen Sie den Text aus einer Datei ein.
    Berechnen Sie die folgenden Statistiken:
        Die 10 häufigsten Wörter (ohne Berücksichtigung der Groß- und Kleinschreibung).
        Die Anzahl der Sätze.
        Die durchschnittliche Wortlänge.
        Die durchschnittliche Satzlänge in Wörtern.
    Geben Sie die berechneten Statistiken aus.

Beispiel:
Dateiinhalt:
"Dies ist ein Beispieltext. Er soll dazu dienen, die Funktion des Textanalyse-Tools zu testen. Der Text besteht aus mehreren Sätzen."
Ausgabe:
Die 10 häufigsten Wörter: ['der', 'die', 'zu', 'des', 'ein', 'er', 'soll', 'dies', 'testen', 'text']
Anzahl der Sätze: 3
Durchschnittliche Wortlänge: 4.5
Durchschnittliche Satzlänge: 7.0 Wörter

Hinweise:
Verwenden Sie die Bibliothek collections.Counter, um die häufigsten Wörter zu zählen.
Verwenden Sie reguläre Ausdrücke (re-Modul), um Sätze und Wörter zu erkennen.
Ignorieren Sie Satzzeichen bei der Wortzählung.
"""