from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        # Should be able to call my functions in this to mandate the order things run in like I did on the day trip project
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print("Welcome to the Inter-Galactic Fight Federation!")
        print("My name is Michael Fluffer and I'll be your ring announcer tonight!")
        print("Brought to you by Draft Kings, tonight we Have Mecha Godzilla vs Godzilla!")
        print("It looks like our combatants can't wait any longer folks!")
        print("LET'S GET READY TO RUUUUMBLLLLLEEEEEE!!!")

    def battle_phase(self):
        # Figure out how to handle who attacks when. May be able to handle it with if statements
        # Do I want a turn order?
        # I may be able to/need to slide my display winner function here as I still need an ending sequence
        # Should definitely be able to set this up like my day trip generator
        who_attacks = input("Who's making the move folks? ")
        if who_attacks == "Godzilla":
            self.dinosaur.attack()
            self.display_winner
        elif who_attacks == "Mecha Godzilla":
            self.robot.attack()
            self.display_winner
        else:
            print("Please give a combatant's name.")
            self.battle_phase()

    def display_winner(self):
        if self.robot.health <= 0:
            print(f"Godzilla is your winner!")
        elif self.dinosaur.health <= 0:
            print(f"Mecha_Godzilla is your winner!")
        # Might not need an else statement here like I thought I would
        pass

