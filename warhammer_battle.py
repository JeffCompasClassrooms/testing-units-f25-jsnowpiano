import random

class Unit:
    def __init__(self, name, attack, defense, health):
        if name is None or name == "" or not type(""):
            self.name = "Unnamed Unit"
        else:
            self.name = name
        if attack < 0:
            self.attack = 0
        else:
            self.attack = attack
        if defense < 0:
            self.defense = 0
        else:
            self.defense = defense
        if health < 1:
            self.health = 1
        else:
            self.health = health

    def is_alive(self):
        return self.health > 0

    def clone(self):
        return Unit(self.name, self.attack, self.defense, self.health)

class SpaceMarine(Unit):
    def __init__(self, SpaceMarinetype="Tactical"):
        if SpaceMarinetype == "Tactical":
            super().__init__("Tactical Space Marine", attack=10, defense=7, health=25)
        elif SpaceMarinetype == "Assault":
            super().__init__("Assault Space Marine", attack=15, defense=5, health=20)
        elif SpaceMarinetype == "Devastator":
            super().__init__("Devastator Space Marine", attack=8, defense=10, health=30)
        elif SpaceMarinetype == "Terminator":
            super().__init__("Terminator Space Marine", attack=12, defense=15, health=40)
        elif SpaceMarinetype == "Scout":
            super().__init__("Scout Space Marine", attack=7, defense=4, health=15)
        elif SpaceMarinetype == "Reiver":
            super().__init__("Reiver Space Marine", attack=14, defense=6, health=22)
        else:
            super().__init__("Tactical Space Marine", attack=10, defense=7, health=25)

class EldarWarrior(Unit):
    def __init__(self, Eldartype="Guardian"):
        if Eldartype == "Guardian":
            super().__init__("Guardian", attack=9, defense=5, health=20)
        elif Eldartype == "Dire Avenger":
            super().__init__("Eldar Dire Avenger", attack=11, defense=6, health=18)
        elif Eldartype == "Howling Banshee":
            super().__init__("Eldar Howling Banshee", attack=13, defense=4, health=16)
        elif Eldartype == "Striking Scorpion":
            super().__init__("Eldar Striking Scorpion", attack=12, defense=7, health=19)
        elif Eldartype == "Wraithguard":
            super().__init__("Eldar Wraithguard", attack=15, defense=8, health=25)
        elif Eldartype == "Farseer":
            super().__init__("Eldar Farseer", attack=10, defense=5, health=15)
        elif Eldartype == "Avatar of Khaine":
            super().__init__("Avatar of Khaine", attack=100, defense=40, health=100)  
        else:
            super().__init__("Guardian", attack=9, defense=5, health=20)

def calculate_damage(attacker, defender):
    raw_damage = attacker.attack - defender.defense
    return max(1, raw_damage)

def simulate_battle(unit1, unit2):
    """
    Simulates a turn-based battle between two units.
    Returns the name of the winner.
    """
    u1 = unit1.clone()
    u2 = unit2.clone()

    # Randomly choose who attacks first
    attacker, defender = (u1, u2) if random.choice([True, False]) else (u2, u1)

    while u1.is_alive() and u2.is_alive():
        damage = calculate_damage(attacker, defender)
        defender.health -= damage
        if not defender.is_alive():
            return attacker.name
        # Swap roles
        attacker, defender = defender, attacker

    return attacker.name  # Should always be the last attacker

# Manual test
if __name__ == "__main__":
    space_marine = SpaceMarine("Terminator")
    Eldar = EldarWarrior("Avatar of Khaine")

    winner = simulate_battle(space_marine, Eldar)
    print(f"The winner is: {winner}")
