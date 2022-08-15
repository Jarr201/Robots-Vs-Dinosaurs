from robot import Mecha_Godzilla, Robot
from dinosuar import Dinosuar, Godzilla

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosuar = Dinosuar()

    def run_game(self):
        # Should be able to call my functions in this to mandate the order things run in like I did on the day trip project
        pass

    def display_welcome(self):
        print("Welcome to the Inter-Galactic Fight Federation!")
        print("Brought to you by Draft Kings, tonight we Have Mecha Godzilla vs Godzilla!")

    def battle_phase(self):
        # Figure out how to handle who attacks when. May be able to handle it with if statements
        pass

    def display_winner(self):
        if Robot.health <= 0:
            print(f"{Godzilla} is your winner!")
        elif Dinosuar.health <= 0:
            print(f"{Mecha_Godzilla} is your winner!")