import pyxel

class HUD:
    def __init__(self, vie, sta):
        self.vie = vie
        self.sta = sta
    
    def draw_vie(self, pv):
        # Dictionnaire pour chaque images dans le dossier hud, sous forme 'nom': (u, v, w, h) -> Coordonées u et v dans le dossier et taille w h
        vie = {'icon': (8, 0, 8, 8),
                    14: (8*2, 0, 16, 8), 13: (8*4, 0, 16, 8), 12: (8*6, 0, 16, 8), 11: (8*8, 0, 16, 8), 10: (8*10, 0, 16, 8),
                    9: (8*12, 0, 16, 8), 8: (8*14, 0, 16, 8), 7: (8*16, 0, 16, 8), 6: (8*18, 0, 16, 8), 5: (8*20, 0, 16, 8),
                    4: (8*22, 0, 16, 8), 3: (8*24, 0, 16, 8), 2: (8*26, 0, 16, 8), 1: (8*28, 0, 16, 8), 0: (8*30, 0, 16, 8)}
        pyxel.blt(6, 6, 0, vie['icon'][0], vie['icon'][1], vie['icon'][2], vie['icon'][3], 1)
        pyxel.blt(16, 6, 0, vie[pv][0], vie[pv][1], vie[pv][2], vie[pv][3], 1)
    
    def draw_sta(self, ps):
        # Dictionnaire similaire à celui de la vie, mais pour l'energie
        sta = {'icon': (8, 8, 8, 8),
                    14: (8*2, 8, 16, 8), 13: (8*4, 8, 16, 8), 12: (8*6, 8, 16, 8), 11: (8*8, 8, 16, 8), 10: (8*10, 8, 16, 8),
                    9: (8*12, 8, 16, 8), 8: (8*14, 8, 16, 8), 7: (8*16, 8, 16, 8), 6: (8*18, 8, 16, 8), 5: (8*20, 8, 16, 8),
                    4: (8*22, 8, 16, 8), 3: (8*24, 8, 16, 8), 2: (8*26, 8, 16, 8), 1: (8*28, 8, 16, 8), 0: (8*30, 8, 16, 8)}
        pyxel.blt(6, 16, 0, sta['icon'][0], sta['icon'][1], sta['icon'][2], sta['icon'][3], 1)
        pyxel.blt(16, 16, 0, sta[ps][0], sta[ps][1], sta[ps][2], sta[ps][3], 1)

    def contours(self):
        pyxel.line(0, 0, 255, 0, 0)
        pyxel.line(0, 127, 255, 127, 0)
        pyxel.line(0, 0, 0, 127, 0)
        pyxel.line(40, 0, 40, 127, 0)
        pyxel.line(216, 0, 216, 127, 0)
        pyxel.line(255, 0, 255, 127, 0)

    def draw_HUD(self):
        pyxel.cls(1)
        self.draw_vie(self.vie)
        self.draw_sta(self.sta)
        self.contours()
        pyxel.rect(41, 1, 175, 126, 3)

    def changement_vie(self, num):
        if self.vie < 14:
            self.vie += num

    def changement_sta(self, num):
        if self.sta < 14:
            self.sta += num