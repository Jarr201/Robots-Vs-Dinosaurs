from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        self.dinosaur = self.dino_target
        self.dino_target -= self.active_weapon

Mecha_Godzilla = Robot("Mecha_Godzilla")

active_weapon = ("Mecha Sword", 19)