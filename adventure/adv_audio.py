import pyttsx3
import random
from abc import ABC, abstractmethod
from enum import Enum

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

class RandomItemSelector:
    def __init__(self, items):
        self.items = items
        self.used_items = []

    def add_item(self, item):
        self.items.append(item)

    def pull_random_item(self):
        if len(self.used_items) == len(self.items):
            self.reset()
        available_items = [item for item in self.items if item not in self.used_items]
        selected_item = random.choice(available_items)
        self.used_items.append(selected_item)
        return selected_item

    def reset(self):
        self.used_items = []

# Define the clues and sense_exp lists
clues = [
    "Es liegt ein schwacher Geruch von Rauch in der Luft.",
    "Es gibt ein staubiges altes Buch mit herausgerissenen Seiten.",
    "Es gibt einen zerbrochenen Spiegel, der verzerrte Bilder reflektiert.",
    "Es gibt einen frischen Blutfleck auf dem Teppich.",
    "Es gibt ein flüsterndes Geräusch, das von den Wänden kommt.",
    "Es gibt ein verstecktes Fach hinter dem Gemälde.",
    "Es zieht kalt unter der Tür.",
    "Es gibt eine Spur von Fußabdrücken, die zum Fenster führt.",
    "Es liegt ein mysteriöser Schlüssel auf dem Boden.",
    "Es gibt eine flackernde Glühbirne, die unheimliche Schatten wirft."
]

sense_exp = [
    "Du siehst einen Schatten über die Wand huschen.",
    "Du hörst den entfernten Echo von Schritten im Korridor.",
    "Du riechst den schwachen Duft von Lavendel, gemischt mit etwas Metallischem.",
    "Du spürst eine Kälte, die dir den Rücken hinunterläuft, als du die kalte Steinwand berührst.",
    "Du spürst eine unsichtbare Präsenz, die dich beobachtet.",
    "Du siehst glitzernde Spinnweben im schwachen Licht.",
    "Du hörst das leise Rascheln von Stoff, als ob jemand gerade an dir vorbeigegangen ist.",
    "Du riechst den muffigen Geruch alter Bücher und Pergamente.",
    "Du fühlst plötzliche Wärme, wenn du dich dem Kamin näherst, obwohl kein Feuer brennt.",
    "Du spürst einen verborgenen Durchgang hinter dem Wandteppich.",
    "Du siehst flackerndes Kerzenlicht, das lange Schatten wirft.",
    "Du hörst den leisen Klang einer Spieluhr, die eine unheimliche Melodie spielt."
]

class SenseClueGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SenseClueGenerator, cls).__new__(cls)
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"

class EncounterOutcome(Enum):
    CONTINUE = 1
    END = 2

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self) -> EncounterOutcome:
        pass

class DefaultEncounter(Encounter):
    def __init__(self):
        self.sense_clue_generator = SenseClueGenerator()

    def run_encounter(self) -> EncounterOutcome:
        sense_clue = self.sense_clue_generator.get_senseclue()
        speak(sense_clue)
        return EncounterOutcome.CONTINUE

class Room:
    def __init__(self, name, encounter):
        self.name = name
        self.encounter = encounter

    def visit_room(self):
        return self.encounter.run_encounter()

# Create instances of DefaultEncounter
default_encounter = DefaultEncounter()

# Create a list of Room objects with interesting castle room names
rooms = [
    Room("Großer Saal", default_encounter),
    Room("Verlies", default_encounter),
    Room("Bibliothek", default_encounter),
    Room("Thronsaal", default_encounter),
    Room("Waffenkammer", default_encounter),
    Room("Geheimer Durchgang", default_encounter)
]

class TreasureEncounter(Encounter):
    def run_encounter(self) -> EncounterOutcome:
        speak("Herzlichen Glückwunsch! Du hast den Schatz gefunden und das Spiel gewonnen!")
        return EncounterOutcome.END

# füge einen Schatzraum mit einem Schatzbegegnung zum rooms-Array hinzu
rooms.append(Room("Schatzraum", TreasureEncounter()))

class RedWizardEncounter(Encounter):
    def run_encounter(self) -> EncounterOutcome:
        game_rules = {
            "Feuerball": ["Eis Splitter", "Blitzschlag"],
            "Eis Splitter": ["Windstoß", "Erdbeben"],
            "Windstoß": ["Blitzschlag", "Feuerball"],
            "Blitzschlag": ["Erdbeben", "Eis Splitter"],
            "Erdbeben": ["Feuerball", "Windstoß"]
        }
        
        choices = list(game_rules.keys())
        
        while True:
            user_choice = input("Wähle einen Zauber: Feuerball, Eis Splitter, Windstoß, Blitzschlag oder Erdbeben: ").strip().title()
            if user_choice not in choices:
                speak("Ungültige Auswahl. Bitte versuche es erneut.")
                continue
            
            wizard_choice = random.choice(choices)
            speak(f"Der Rote Zauberer zaubert: {wizard_choice}")
            
            if user_choice == wizard_choice:
                speak("Es ist ein Unentschieden! Beide Zauber prallen aufeinander und haben keine Wirkung. Versuche es erneut.")
                continue
            elif wizard_choice in game_rules[user_choice]:
                speak("Dein Zauber übertrifft den Zauber des Roten Zauberers! Du hast den Zauberwettstreit gewonnen!")
                return EncounterOutcome.CONTINUE
            else:
                speak("Der Zauber des Roten Zauberers übertrifft deinen Zauber! Du wurdest aus diesem Schloss verbannt.")
                return EncounterOutcome.END

# Füge einen Raum namens "Die Höhle des Roten Zauberers" mit der RedWizardEncounter hinzu und füge ihn zur rooms-Liste hinzu
rooms.append(Room("Die Höhle des Roten Zauberers", RedWizardEncounter()))

class BlueWizardEncounter(Encounter):
    def run_encounter(self) -> EncounterOutcome:
        game_rules = {
            "Feuerball": "Eis Splitter",
            "Eis Splitter": "Erdbeben",
            "Erdbeben": "Feuerball"
        }
        
        choices = list(game_rules.keys())
        
        while True:
            user_choice = input("Wähle einen Zauber: Feuerball, Eis Splitter oder Erdbeben: ").strip().title()
            if user_choice not in choices:
                speak("Ungültige Wahl. Bitte versuche es erneut.")
                continue
            
            wizard_choice = random.choice(choices)
            speak(f"Der Blaue Zauberer zaubert: {wizard_choice}")
            
            if user_choice == wizard_choice:
                speak("Unentschieden! Versuche es nochmal.")
                continue
            elif game_rules[user_choice] == wizard_choice:
                speak("Du hast den Blauen Zauberer aus diesem Schloss verbannt!")
                return EncounterOutcome.CONTINUE
            else:
                speak("Der Blaue Zauberer hat dich aus diesem Schloss verbannt.")
                return EncounterOutcome.END

# create a room called “The Blue Wizard’s Lair” with the Blue Wizard Encounter and add it to the rooms list
rooms.append(Room("Die Höhle des Blauen Zauberers", BlueWizardEncounter()))

class Castle:
    def __init__(self, rooms):
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self):
        while True:
            num_doors = random.randint(2, 4)
            speak(f"Es gibt {num_doors} Türen vor dir.")
            try:
                selected_door = int(input(f"Wähle eine Türnummer (1 bis {num_doors}): "))
                if 1 <= selected_door <= num_doors:
                    return selected_door
                else:
                    speak(f"Ungültige Auswahl. Bitte wähle eine Zahl zwischen 1 und {num_doors}.")
            except ValueError:
                speak("Ungültige Eingabe. Bitte gib eine Zahl ein.")

    def next_room(self):
        self.select_door()
        room = self.room_selector.pull_random_item()
        speak(f"Du hast den Raum {room.name} betreten.")
        return room.visit_room()

    def reset(self):
        self.room_selector.reset()

class Game:
    def __init__(self, rooms):
        self.castle = Castle(rooms)

    def play_game(self):
        speak("Willkommen beim Schlossabenteuerspiel!")
        speak("Dein Ziel ist es, durch das Schloss zu navigieren und den Schatz zu finden.")
        speak("Viel Glück!")

        while True:
            outcome = self.castle.next_room()
            if outcome == EncounterOutcome.END:
                self.castle.reset()
                speak("Spiel vorbei.")
                play_again = input("Möchtest du ein anderes Schloss erkunden? (ja/nein): ").strip().lower()
                if play_again != 'ja':
                    speak("Vielen Dank fürs Spielen!")
                    break

# Start the game
game = Game(rooms)
game.play_game()