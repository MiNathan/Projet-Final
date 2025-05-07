import pyxel

class UI:
    """
    Classe pour la création et l'interaction avec l'interface utilisateur
    Principalement des methodes pyxel pour dessiner des lignes et des icones
    Les méthodes avec la préposition 'draw' dessinnent dans l'interface
    Les autres méthodes servent à modifier les attributs
    """
    def __init__(self, vie, sta):
        self.vie = vie
        self.sta = sta
        self.arg = 0
    
    def draw_UI(self):
        """
        Fait appel aux autres méthodes pour dessiner l'interface
        """
        pyxel.cls(0)
        self.draw_contours()
        self.draw_grille()
        self.draw_vie(self.vie)
        self.draw_sta(self.sta)
        self.draw_arg(self.arg)

    def draw_vie(self, pv):
        """
        Dessine la barre de vie
        """
        # Dictionnaire pour chaque images dans le dossier hud, sous forme 'nom': (u, v, w, h) -> Coordonées u et v dans le dossier et taille w h
        vie = {'icon': (8, 0, 8, 8),
                    14: (8*2, 0, 16, 8), 13: (8*4, 0, 16, 8), 12: (8*6, 0, 16, 8), 11: (8*8, 0, 16, 8), 10: (8*10, 0, 16, 8),
                    9: (8*12, 0, 16, 8), 8: (8*14, 0, 16, 8), 7: (8*16, 0, 16, 8), 6: (8*18, 0, 16, 8), 5: (8*20, 0, 16, 8),
                    4: (8*22, 0, 16, 8), 3: (8*24, 0, 16, 8), 2: (8*26, 0, 16, 8), 1: (8*28, 0, 16, 8), 0: (8*2, 0, 16, 8)}
        pyxel.blt(6, 6, 0, vie['icon'][0], vie['icon'][1], vie['icon'][2], vie['icon'][3], 7)
        pyxel.blt(16, 6, 0, vie[pv][0], vie[pv][1], vie[pv][2], vie[pv][3], 7)
    
    def draw_sta(self, ps):
        """
        Dessine la barre d'endurance
        """
        # Dictionnaire similaire à celui de la vie, mais pour l'endurance
        sta = {'icon': (8, 8, 8, 8),
                    14: (8*2, 8, 16, 8), 13: (8*4, 8, 16, 8), 12: (8*6, 8, 16, 8), 11: (8*8, 8, 16, 8), 10: (8*10, 8, 16, 8),
                    9: (8*12, 8, 16, 8), 8: (8*14, 8, 16, 8), 7: (8*16, 8, 16, 8), 6: (8*18, 8, 16, 8), 5: (8*20, 8, 16, 8),
                    4: (8*22, 8, 16, 8), 3: (8*24, 8, 16, 8), 2: (8*26, 8, 16, 8), 1: (8*28, 8, 16, 8), 0: (8*2, 8, 16, 8)}
        pyxel.blt(6, 16, 0, sta['icon'][0], sta['icon'][1], sta['icon'][2], sta['icon'][3], 7)
        pyxel.blt(16, 16, 0, sta[ps][0], sta[ps][1], sta[ps][2], sta[ps][3], 7)

    def draw_arg(self, gd):
        """
        Inscrit la quantité d'argent du joueur
        """
        pyxel.blt(221, 6, 0, 0, 0, 8, 8, 7)
        pyxel.text(231, 8, str(gd), 10)

    def draw_contours(self):
        """
        Dessine les bords bleu foncés
        """
        pyxel.rect(0, 0, 40, 128, 5)
        pyxel.rect(216, 0, 216, 128, 5)
        pyxel.line(0, 0, 255, 0, 1)
        pyxel.line(0, 128, 255, 128, 1)
        pyxel.line(0, 0, 0, 128, 1)
        pyxel.line(40, 0, 40, 128, 1)
        pyxel.line(216, 0, 216, 128, 1)
        pyxel.line(255, 0, 255, 128, 1)

    def draw_grille(self):
        """
        Dessine la grille bleu foncée sur laquelle se déplace le personnage
        """
        for i in range((216-40) // 8):
            pyxel.line(i*8 + 40, 0, i*8 + 40, 127, 1)
            pyxel.line(40, i*8, 216, i*8, 1)

    def changement_vie(self, num):
        """
        Permet de changer la valeur de la barre de vie (barre rouge)
        """
        if self.vie + num < 14:
            self.vie += num
        elif self.vie + num <= 0:
            self.vie = -1
        else:
            self.vie = 14

    def changement_sta(self, num):
        """
        Permet de changer la valeur de la barre d'endurance (barre jaune)
        """
        if self.sta + num < 14:
            self.sta += num
        elif self.sta + num <= 0:
            self.sta = -1
        else:
            self.sta = 14

    def debug(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.changement_vie(1)
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.changement_vie(-1)
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.changement_sta(-1)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.changement_sta(1)