# copilot_course

## Spieleübersicht

Dieses Repository enthält drei verschiedene Spiele, die in Python implementiert sind. Jedes Spiel hat seine eigenen Regeln und Mechaniken. Im Folgenden finden Sie eine kurze Beschreibung der einzelnen Spiele und deren Funktionsweise.

### 1. Schlossabenteuerspiel (ADV_AUDIO.PY und ADV_GAME.PY)

Das Schlossabenteuerspiel ist ein textbasiertes Abenteuerspiel, bei dem der Spieler durch verschiedene Räume eines Schlosses navigiert. Jeder Raum hat eine eigene Begegnung, die der Spieler bestehen muss, um weiterzukommen. Das Ziel des Spiels ist es, den Schatz zu finden.

#### Hauptkomponenten:
- **RandomItemSelector**: Eine Klasse zur zufälligen Auswahl von Elementen aus einer Liste, ohne Wiederholung.
- **SenseClueGenerator**: Eine Singleton-Klasse, die zufällige Hinweise und Sinneserfahrungen generiert.
- **Encounter**: Eine abstrakte Basisklasse für Begegnungen im Spiel.
- **DefaultEncounter**: Eine Standardbegegnung, die zufällige Hinweise und Sinneserfahrungen ausgibt.
- **TreasureEncounter**: Eine Begegnung, bei der der Spieler den Schatz findet und das Spiel gewinnt.
- **RedWizardEncounter**: Eine Begegnung mit einem Zauberer, bei der der Spieler einen Zauberwettstreit bestehen muss.
- **BlueWizardEncounter**: Eine ähnliche Begegnung wie die mit dem Roten Zauberer, jedoch mit anderen Regeln.
- **Room**: Eine Klasse, die einen Raum im Schloss repräsentiert und eine Begegnung enthält.
- **Castle**: Eine Klasse, die das Schloss und die Navigation durch die Räume verwaltet.
- **Game**: Die Hauptklasse, die das Spiel steuert und den Spielablauf verwaltet.

### 2. Rock Paper Scissors Lizard Spock (RPSLS.PY)

Dieses Spiel ist eine erweiterte Version des klassischen Schere-Stein-Papier-Spiels, bei dem zwei zusätzliche Optionen hinzugefügt wurden: Echse und Spock. Das Spiel wird über die Konsole gespielt, und der Spieler tritt gegen den Computer an.

#### Hauptkomponenten:
- **RPSLSGame**: Die Hauptklasse des Spiels, die die Spielregeln, die Benutzereingabe und die Spielausgabe verwaltet.
  - **rules**: Ein Wörterbuch, das die Regeln des Spiels enthält.
  - **determine_winner**: Eine Methode zur Bestimmung des Gewinners basierend auf den Regeln.
  - **get_user_choice**: Eine Methode zur Abfrage der Benutzereingabe.
  - **get_computer_choice**: Eine Methode zur zufälligen Auswahl der Computerwahl.
  - **play_game**: Eine Methode, die den Spielablauf steuert.

### Installation und Ausführung

Um die Spiele auszuführen, stellen Sie sicher, dass Python installiert ist. Klonen Sie das Repository und führen Sie die gewünschten Python-Dateien aus.

```bash
git clone <repository-url>
cd copilot_course
python3 adv_audio.py  # Für das Schlossabenteuerspiel
python3 rpsls.py      # Für Rock Paper Scissors Lizard Spock