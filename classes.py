import pyxel
import random as r

class Perso:
    """
    Classe representant un personnage joueur
    Une instance de la classe est capable de:
        se déplacer avec les touches du clavier
        Intéragir avec son environnement (Ouvrir des portes, fouiller des coffres...)
        Se battre avec des ennemis
        Faire du troc avec des PNJ type marchand, villageois...
    """
    def __init__(self, nom, vie, sta):
        self.nom = nom  # Nom du perso
        self.vie = vie    # Points de vie du perso
        self.sta = sta    # Points d'endurance du perso
        self.arg = 0
        self.x = 112
        self.y = 56

    def draw_perso(self):
        pyxel.blt(self.x + 1, self.y + 1, 1, 1, 1, 8, 8, 7)

    def deplacement(self, axe, inc):
        if axe == 'x':
            self.x += inc
        if axe == 'y':
            self.y += inc

    def get_pos(self):
        return (self.x, self.y)

    def act(self, objet=None):
        if pyxel.btnp(pyxel.KEY_Z) and self.y >= 8:
            return self.deplacement('y', -8)
        if pyxel.btnp(pyxel.KEY_Q) and self.x >= 48:
            return self.deplacement('x', -8)
        if pyxel.btnp(pyxel.KEY_S) and self.y <= 119:
            return self.deplacement('y', 8)
        if pyxel.btnp(pyxel.KEY_D) and self.x <= 207:
            return self.deplacement('x', 8)
        if pyxel.btnp(pyxel.KEY_E):
            for obj in objet:
                objets = obj.interaction(self.x, self.y, self)
            return objets
    
    def get_nom(self):
        return self.nom
    
    def get_vie(self):
        return self.vie
    
    def get_sta(self):
        return self.sta
    
    def en_vie(self):
        return self.vie > 0

    def prends_degats(self, atk):
        self.vie -= atk
    
    def soigne(self, soin):
        self.vie += soin

    def gagner_argent(self, arg):
        self.arg += arg

if __name__ == "__main__":
    test = Perso("test", 14, 14)
    assert test.get_nom() == "test"
    assert test.get_vie() == 14
    assert test.get_vie() == 14
    assert test.en_vie() == True
    test.prends_degats(2)
    assert test.get_vie() == 12
    test.soigne(2)
    assert test.get_vie() == 14



class Objet:
    """
    Classe permettant de créer un objet dans le monde
    Le joueur peut interagir avec cet objet, par exemple le ramasser
    """

    def __init__(self, type, x, y, nom = ""):
        self.type = type
        if x < 45:
            self.x = x + 5
        if x > 210:
            self.x = x - 5
        else:
            self.x = x

        if y < 5:
            self.y = y + 5
        if y > 122:
            self.y = y - 5
        else:
            self.y = y
        self.nom = nom
        self.inter = False
    
    def draw_obj(self):
        if self.type == "piece":
            pyxel.blt(self.x + 1, self.y + 1, 2, 1, 1, 7, 7, 7)
        if self.type == "coffre":
            if self.inter == False:
                pyxel.blt(self.x + 1, self.y + 1, 2, 1, 9, 7, 7, 7)
            else:
                pyxel.blt(self.x + 1, self.y + 1, 2, 9, 9, 7, 7, 7)
    
    def get_pos(self):
        return (self.x, self.y)

    def interaction(self, x, y, joueur):
        if self.type == "piece" and self.inter == False:
            self.inter = True
            pyxel.rect(self.x, self.y, 7, 7, 0)
            joueur.gagner_argent(1)

        if self.type == "coffre" and x == self.x and y == self.y and self.inter == False:

            loot = ["piece"]
            objets = []
            for i in range(5):
                objets.append(Objet(r.choice(loot), self.x + r.randint(0, 5), self.y + r.randint(0, 5)))
            self.inter = True
            pyxel.rect(self.x, self.y, 7, 7, 0)
            return objets