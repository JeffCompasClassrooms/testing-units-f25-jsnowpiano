import unittest
from warhammer_battle import *

class TestWarhammerBattle(unittest.TestCase):

    def test_unit_creation(self):
        unit = Unit("Test Unit", attack=5, defense=3, health=20)
        self.assertEqual(unit.name, "Test Unit")
        self.assertEqual(unit.attack, 5)
        self.assertEqual(unit.defense, 3)
        self.assertEqual(unit.health, 20)
        self.assertTrue(unit.is_alive())
    
    def test_unit_creation_negative_stats(self):
        unit = Unit("Test Unit", attack=-5, defense=-5, health=-5)
        self.assertEqual(unit.name, "Test Unit")
        self.assertEqual(unit.attack, 0)
        self.assertEqual(unit.defense, 0)
        self.assertEqual(unit.health, 1)
        self.assertTrue(unit.is_alive())
    
    def test_unit_creation_no_name(self):
        unit = Unit(None, attack=5, defense=3, health=20)
        self.assertEqual(unit.name, "Unnamed Unit")

    def test_is_alive(self):
        unit = Unit("Test Unit", attack=5, defense=3, health=1)
        self.assertTrue(unit.is_alive())
        unit.health = 0
        self.assertFalse(unit.is_alive())
    
    def test_clone(self):
        unit = Unit("Test Unit", attack=5, defense=3, health=20)
        clone = unit.clone()
        self.assertEqual(clone.name, unit.name)
        self.assertEqual(clone.attack, unit.attack)
        self.assertEqual(clone.defense, unit.defense)
        self.assertEqual(clone.health, unit.health)
        self.assertIsNot(clone, unit)
    
    def test_calculate_damage(self):
        attacker = Unit("Attacker", attack=10, defense=3, health=20)
        defender = Unit("Defender", attack=5, defense=8, health=20)
        damage = calculate_damage(attacker, defender)
        self.assertEqual(damage, 2)
    
    def test_calculate_damage_minimum(self):
        attacker = Unit("Attacker", attack=5, defense=3, health=20)
        defender = Unit("Defender", attack=5, defense=10, health=20)
        damage = calculate_damage(attacker, defender)
        self.assertEqual(damage, 1)
    
    def test_calculate_damage_equal(self):
        attacker = Unit("Attacker", attack=5, defense=3, health=20)
        defender = Unit("Defender", attack=5, defense=5, health=20)
        damage = calculate_damage(attacker, defender)
        self.assertEqual(damage, 1)
    
    def test_simulate_battle(self):
        unit1 = Unit("Unit 1", attack=10, defense=5, health=30)
        unit2 = Unit("Unit 2", attack=8, defense=4, health=25)
        winner = simulate_battle(unit1, unit2)
        self.assertIn(winner, ["Unit 1", "Unit 2"])
    
    def test_simulate_battle_edge_case(self):
        unit1 = Unit("Weak Unit", attack=1, defense=0, health=1)
        unit2 = Unit("Strong Unit", attack=10, defense=5, health=50)
        winner = simulate_battle(unit1, unit2)
        self.assertEqual(winner, "Strong Unit")
        unit1 = Unit("Weak Unit", attack=1, defense=0, health=1)
        unit2 = Unit("Strong Unit", attack=10, defense=5, health=50)
        winner = simulate_battle(unit2, unit1)
        self.assertEqual(winner, "Strong Unit")
    
    def test_space_marine_creation_tatical(self):
        marine = SpaceMarine("Tactical")
        self.assertEqual(marine.name, "Tactical Space Marine")
        self.assertEqual(marine.attack, 10)
        self.assertEqual(marine.defense, 7)
        self.assertEqual(marine.health, 25)

    def test_space_marine_creation_assault(self):
        marine = SpaceMarine("Assault")
        self.assertEqual(marine.name, "Assault Space Marine")
        self.assertEqual(marine.attack, 15)
        self.assertEqual(marine.defense, 5)
        self.assertEqual(marine.health, 20)

    def test_space_marine_creation_devastator(self):
        marine = SpaceMarine("Devastator")
        self.assertEqual(marine.name, "Devastator Space Marine")
        self.assertEqual(marine.attack, 8)
        self.assertEqual(marine.defense, 10)
        self.assertEqual(marine.health, 30)

    def test_space_marine_creation_terminator(self):
        marine = SpaceMarine("Terminator")
        self.assertEqual(marine.name, "Terminator Space Marine")
        self.assertEqual(marine.attack, 12)
        self.assertEqual(marine.defense, 15)
        self.assertEqual(marine.health, 40)

    def test_space_marine_creation_scout(self):
        marine = SpaceMarine("Scout")
        self.assertEqual(marine.name, "Scout Space Marine")
        self.assertEqual(marine.attack, 7)
        self.assertEqual(marine.defense, 4)
        self.assertEqual(marine.health, 15)

    def test_space_marine_creation_reiver(self):
        marine = SpaceMarine("Reiver")
        self.assertEqual(marine.name, "Reiver Space Marine")
        self.assertEqual(marine.attack, 14)
        self.assertEqual(marine.defense, 6)
        self.assertEqual(marine.health, 22)

    def test_space_marine_creation_default(self):    
        marine = SpaceMarine("UnknownType")
        self.assertEqual(marine.name, "Tactical Space Marine")
        self.assertEqual(marine.attack, 10)
        self.assertEqual(marine.defense, 7)
        self.assertEqual(marine.health, 25)
    
    def test_eldar_warrior_creation_guardian(self):
        eldar = EldarWarrior("Guardian")
        self.assertEqual(eldar.name, "Guardian")
        self.assertEqual(eldar.attack, 9)
        self.assertEqual(eldar.defense, 5)
        self.assertEqual(eldar.health, 20)
    
    def test_eldar_warrior_creation_dire_avenger(self):
        eldar = EldarWarrior("Dire Avenger")
        self.assertEqual(eldar.name, "Eldar Dire Avenger")
        self.assertEqual(eldar.attack, 11)
        self.assertEqual(eldar.defense, 6)
        self.assertEqual(eldar.health, 18)
    
    def test_eldar_warrior_creation_howling_banshee(self):
        eldar = EldarWarrior("Howling Banshee")
        self.assertEqual(eldar.name, "Eldar Howling Banshee")
        self.assertEqual(eldar.attack, 13)
        self.assertEqual(eldar.defense, 4)
        self.assertEqual(eldar.health, 16)
    
    def test_eldar_warrior_creation_striking_scorpion(self):
        eldar = EldarWarrior("Striking Scorpion")
        self.assertEqual(eldar.name, "Eldar Striking Scorpion")
        self.assertEqual(eldar.attack, 12)
        self.assertEqual(eldar.defense, 7)
        self.assertEqual(eldar.health, 19)
    
    def test_eldar_warrior_creation_wraithguard(self):
        eldar = EldarWarrior("Wraithguard")
        self.assertEqual(eldar.name, "Eldar Wraithguard")
        self.assertEqual(eldar.attack, 15)
        self.assertEqual(eldar.defense, 8)
        self.assertEqual(eldar.health, 25)
    
    def test_eldar_warrior_creation_farseer(self):
        eldar = EldarWarrior("Farseer")
        self.assertEqual(eldar.name, "Eldar Farseer")
        self.assertEqual(eldar.attack, 10)
        self.assertEqual(eldar.defense, 5)
        self.assertEqual(eldar.health, 15)
    
    def test_eldar_warrior_creation_avatar_of_khaine(self):
        eldar = EldarWarrior("Avatar of Khaine")
        self.assertEqual(eldar.name, "Avatar of Khaine")
        self.assertEqual(eldar.attack, 100)
        self.assertEqual(eldar.defense, 40)
        self.assertEqual(eldar.health, 100)
    
    def test_eldar_warrior_creation_default(self):
        eldar = EldarWarrior("UnknownType")
        self.assertEqual(eldar.name, "Guardian")
        self.assertEqual(eldar.attack, 9)
        self.assertEqual(eldar.defense, 5)
        self.assertEqual(eldar.health, 20)
    
    def test_battle_space_marine_vs_eldar(self):
        marine = SpaceMarine("Terminator")
        eldar = EldarWarrior("Wraithguard")
        winner = simulate_battle(marine, eldar)
        self.assertIn(winner, ["Terminator Space Marine", "Eldar Wraithguard"])
    
    def test_battle_space_marine_vs_space_marine(self):
        marine1 = SpaceMarine("Assault")
        marine2 = SpaceMarine("Devastator")
        winner = simulate_battle(marine1, marine2)
        self.assertIn(winner, ["Assault Space Marine", "Devastator Space Marine"])
    
    def test_battle_eldar_vs_eldar(self):
        eldar1 = EldarWarrior("Howling Banshee")
        eldar2 = EldarWarrior("Farseer")
        winner = simulate_battle(eldar1, eldar2)
        self.assertIn(winner, ["Eldar Howling Banshee", "Eldar Farseer"])
    
    def test_battle_identical_units(self):
        unit1 = Unit("Identical Unit", attack=10, defense=5, health=20)
        unit2 = Unit("Identical Unit", attack=10, defense=5, health=20)
        winner = simulate_battle(unit1, unit2)
        self.assertIn(winner, ["Identical Unit"])

    def test_battle_strong_vs_high_defense(self):
        strong_unit = Unit("Strong Unit", attack=20, defense=5, health=30)
        high_defense_unit = Unit("High Defense Unit", attack=5, defense=20, health=30)
        winner = simulate_battle(strong_unit, high_defense_unit)
        self.assertIn(winner, ["Strong Unit", "High Defense Unit"])
    
    def test_battle_zero_attack(self):
        zero_attack_unit = Unit("Zero Attack Unit", attack=0, defense=5, health=20)
        strong_unit = Unit("Strong Unit", attack=10, defense=5, health=20)
        winner = simulate_battle(zero_attack_unit, strong_unit)
        self.assertEqual(winner, "Strong Unit")
    
    def test_battle_high_health_unit(self):
        high_health_unit = Unit("High Health Unit", attack=10, defense=5, health=1000)
        normal_unit = Unit("Normal Unit", attack=10, defense=5, health=20)
        winner = simulate_battle(high_health_unit, normal_unit)
        self.assertEqual(winner, "High Health Unit")
    