class Perso:
    """
    Classe representant un personnage joueur
    Une instance de la classe est capable de:
        se déplacer avec les touches du clavier
        Intéragir avec son environnement (Ouvrir des portes, fouiller des coffres...)
        Se battre avec des ennemis
        Faire du troc avec des PNJ type marchand, villageois...
    """
    def __init__(self, nom):
        self.nom = nom  # Nom du perso
        self.pv = 15    # Points de vie du perso
        self.ps = 15    # Points d'endurance du perso
        self.de = 5     # Points de défence du perso
    
    def get_nom(self):
        return self.nom
    
    def get_pv(self):
        return self.pv
    
    def get_ps(self):
        return self.ps

    def get_de(self):
        return self.de
    
    def en_vie(self):
        return self.pv > 0

    def prends_degats(self, atk):
        self.pv -= atk
    
    def soigne(self, soin):
        self.pv += soin


if __name__ == "__main__":
    test = Perso("test")
    assert test.get_nom() == "test"
    assert test.get_pv() == 15
    assert test.get_pv() == 15
    assert test.en_vie() == True
    test.prends_degats(2)
    assert test.get_pv() == 13
    test.soigne(2)
    assert test.get_pv() == 15