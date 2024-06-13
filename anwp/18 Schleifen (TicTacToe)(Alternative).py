"""1. Tic Tac Toe
Das Spiel Tic Tac Toe (Drei-gewinnt) ist mit Python zu programmieren.
o Es gibt 2 Spieler, die abwechselnd in einem 3x3 großen Spielfeld ein x bzw. ein o
setzen.
o Wer zuerst 3 Felder in einer Reihe, einer Spalte oder in der Diagonalen belegt, hat
gewonnen.
o Das Spielfeld sollte im Programm über den Datentyp Liste abgebildet werden
o Bei der Programmerstellung sollten folgende Funktionalitäten beachtet werden
 Hauptroutine festlegen
 Spielfeld erstellen und ausgeben
 Spielzug erfassen
 Spielzug in das Spielfeld einarbeiten
 Sieger ermitteln
 Spiel vorzeitig beenden"""

# Frage 1 = warum wird das Spielfeld nicht geprintet bei einem Sieg/Patt?
# Frage 2 = Siehe Kommentar bei der "player" FUnktion

# Definition statischer Variablen
player1_symbol = "[x]"
player2_symbol = "[o]"
row = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
playing_field_string = "Spielfeld: "
player1_win = "Player 1 hat gewonnen!"
player2_win = "Player 2 hat gewonnen!"
total_turn = 0


# Funktionen
def player_turn(player_input, player_symbol):
    """Diese Funktion setzt die Spielerzüge um"""
    # "pop(index)" löscht einen gezielten indexwert einer Liste
    # "inser(index, wert)" fügt an einem bestimmten Index einen  bestimmten Wert hinzu
    # DieSchleife sit so unnötig, da die Eingabe neugestartet werden muss. Mache ich es mit einem True/False Wert?
    give_up = False
    if player_input == "oben links":
        row.pop(0)
        row.insert(0, player_symbol)
    elif player_input == "oben mitte":
        row.pop(1)
        row.insert(1, player_symbol)
    elif player_input == "oben rechts":
        row.pop(2)
        row.insert(2, player_symbol)
    elif player_input == "mitte links":
        row.pop(3)
        row.insert(3, player_symbol)
    elif player_input == "mitte mitte":
        row.pop(4)
        row.insert(4, player_symbol)
    elif player_input == "mitte rechts":
        row.pop(5)
        row.insert(5, player_symbol)
    elif player_input == "unten links":
        row.pop(6)
        row.insert(6, player_symbol)
    elif player_input == "unten mitte":
        row.pop(7)
        row.insert(7, player_symbol)
    elif player_input == "unten rechts":
        row.pop(8)
        row.insert(8, player_symbol)
    elif player_input == "aufgeben":
        give_up = True
        return give_up


def help():
    """Diese Funktion gibt bei dem Schlüsselwort eine Hilfestellung"""
    print("Mögliche Spielzügen wären \"oben links\", \"mitte mitte\" oder \"unten rechts\". Aufgeben kannst du mit dem Schlüsselwort \"aufgeben\"")


def win(player_symbol):
    """Diese Funktion prüft die Siegbedingungen & gibt einen Bool zurück"""
    win_bool = False
    if row[0] == row[1] == row[2] == player_symbol:
        win_bool = True
    elif row[3] == row[4] == row[5] == player_symbol:
        win_bool = True
    elif row[6] == row[7] == row[8] == player_symbol:
        win_bool = True
    elif row[0] == row[3] == row[6] == player_symbol:
        win_bool = True
    elif row[1] == row[4] == row[7] == player_symbol:
        win_bool = True
    elif row[2] == row[5] == row[8] == player_symbol:
        win_bool = True
    elif row[0] == row[4] == row[8] == player_symbol:
        win_bool = True
    elif row[2] == row[4] == row[6] == player_symbol:
        win_bool = True

    return win_bool


def draw(total_turn):
    """Diese Funktion prüft ob ein unentschieden vorliegt & beendet dann ggf. die Partie"""
    draw_bool = False
    if total_turn == 5:
        draw_bool = True
    return draw_bool


def print_playing_field():
        print(playing_field_string)
        print(row[0], row[1], row[2])
        print(row[3], row[4], row[5])
        print(row[6], row[7], row[8])
        print(100 * "-")


# mit if überschreiben prüen, wenn gefahr droht auf true und warnung printen
def player(total_turn):
    """Diese Funktion verarbeitet die Spielereingaben von Player 1 & Player 2. Anschließend wird das aktuelle Spielfeld ausgegeben"""
    player_turn_list = []
    while True:
        # Player 1
        print_playing_field()
        while True:
            player_turn_input = input("Player 1, bitte geben Sie ihren Spielzug ein (Für helfe geben Sie einefach das Schlüsselwort \"help\" ein): ")
            if player_turn_input in player_turn_list:
                print("Dies ist kein zulässiger Spielzug!")
            elif player_turn_input in ["oben links", "oben mitte", "oben rechts", "mitte links", "mitte mitte", "mitte rechts", "unten links", "unten mitte", "unten rechts"]:
                player_turn(player_turn_input, player1_symbol)
                player_turn_list.append(player_turn_input)
                break
            elif player_turn_input == "help":
                help()
            elif player_turn_input == "spielfeld":
                print_playing_field()
            elif player_turn_input == "aufgeben":
                if player_turn(player_turn_input, player1_symbol):
                    print("Player 1 hat aufgegeben, Player 2 hat die Partie gewonnen!\n", print_playing_field())
                    break
            else:
                print(100 * "-", f"\n{player_turn_input} ist kein zulässiger Spielzug!\n", 100 * "-")

            if win(player1_symbol):
                print("Player 1 hat die Partie gewonnen!")
                break

        total_turn += 1

        if draw(total_turn):
            print("Die Partie ist ein Patt!")
            print_playing_field()
            break


        # Player 2
        print_playing_field()
        while True:
            player_turn_input = input("Player 2, bitte geben Sie ihren Spielzug ein (Für helfe geben Sie einefach das Schlüsselwort \"help\" ein): ")
            if player_turn_input in player_turn_list:
                print("Dies ist kein zulässiger Spielzug!")
            elif player_turn_input in ["oben links", "oben mitte", "oben rechts", "mitte links", "mitte mitte", "mitte rechts", "unten links", "unten mitte", "unten rechts"]:
                player_turn(player_turn_input, player2_symbol)
                player_turn_list.append(player_turn_input)
                break
            elif player_turn_input == "help":
                help()
            elif player_turn_input == "spielfeld":
                print_playing_field()
            elif player_turn_input == "aufgeben":
                if player_turn(player_turn_input, player1_symbol):
                    print("Player 2 hat aufgegeben, Player 1 hat die Partie gewonnen!\n", print_playing_field())
                    break
            else:
                print(100 * "-", f"\n{player_turn_input} ist kein zulässiger Spielzug!\n", 100 * "-")

            if win(player1_symbol):
                print("Player 1 hat die Partie gewonnen!")
                break

        
player(total_turn)