import pyxel

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
        self.x = 112
        self.y = 56

    def draw_perso(self):
        pyxel.blt(self.x, self.y, 1, 0, 0, 8, 8, 7)

    def deplacement(self, axe, inc):
        if axe == 'x':
            self.x += inc
        if axe == 'y':
            self.y += inc

    def act(self):
        if pyxel.btnp(pyxel.KEY_Z) and self.y >= 8:
            return self.deplacement('y', -8)
        if pyxel.btnp(pyxel.KEY_Q) and self.x >= 48:
            return self.deplacement('x', -8)
        if pyxel.btnp(pyxel.KEY_S) and self.y <= 119:
            return self.deplacement('y', 8)
        if pyxel.btnp(pyxel.KEY_D) and self.x <= 207:
            return self.deplacement('x', 8)
    
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