from weapon import Weapon
from dinosuar import Dinosuar

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()
        self.robot = Robot()

    def attack(self, dinosuar):
        pass