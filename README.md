#alexandre gagnon 401
import random

class NPC:
    def __init__(self, name, race, species, profession):
        self.nom = nom
        self.race = race
        self.espece = espece
        self.profession = profession
        self.force = max(random.sample(range(1,7), 3))
        self.agilite = max(random.sample(range(1,7), 3))
        self.constitution = max(random.sample(range(1,7), 3))
        self.intelligence = max(random.sample(range(1,7), 3))
        self.sagesse = max(random.sample(range(1,7), 3))
        self.charisme = max(random.sample(range(1,7), 3))
        self.classe_armure = random.randint(1,12)
        self.point_de_vie = random.randint(1,20)

    def afficher_caracteristiques(self):
        print("Nom: ", self.name)
        print("Race: ", self.race)
        print("espece: ", self.espece)
        print("Profession: ", self.profession)
        print("Force: ", self.force)
        print("Agility: ", self.agilite)
        print("Constitution: ", self.constitution)
        print("Intelligence: ", self.intelligence)
        print("sagesse: ", self.sagesse)
        print("Charisma: ", self.charisme)
        print("Armure Class: ", self.classe_armure)
        print("point_de_vie: ", self.point_de_vie)
        
class Kobold(NPC):
    def __init__(self, nom, race, species, profession):
        super().__init__(nom, race, species, profession)

    def attaquer(self, target):
        print(f"{self.name} attaque {target.name}!")
        
    def subir_dommage(self, damage):
        self.point_de_vie -= damage
        print(f"{self.name} subit {damage} points de dommage, il lui reste {self.point_de_vie} points de vie.")

class Hero(NPC):
    def __init__(self, name, race, espece, profession):
        super().__init__(name, race, espece, profession)

    def attaquer(self, target):
        print(f"{self.name} attaque {target.name}!")
        
    def subir_dommage(self, damage):
        self.point_de_vie -= damage
        print(f"{self.name} subit {damage} points de dommage, il lui reste {self.point_de_vie} points de vie.")
