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
        self.vie = 14    # Points de vie du perso
        self.sta = 14    # Points d'endurance du perso
    
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
    test = Perso("test")
    assert test.get_nom() == "test"
    assert test.get_vie() == 14
    assert test.get_vie() == 14
    assert test.en_vie() == True
    test.prends_degats(2)
    assert test.get_vie() == 12
    test.soigne(2)
    assert test.get_vie() == 14