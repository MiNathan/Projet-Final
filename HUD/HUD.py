import pyxel

class HUD:
    def __init__(self):
        pyxel.init(256, 128, title ="Classe HUD", fps= 60)
        pyxel.load('hud.pyxres')



        pyxel.run(self.update, self.draw)
    
    def draw_vie(self):
        # Dictionnaire pour chaque images dans le dossier hud, sous forme 'nom': (u, v, w, h) -> Coordonées u et v dans le dossier et taille w h
        self.vie = {'icon': (8, 0, 8, 8),
                    14: (8*2, 0, 16, 8), 13: (8*4, 0, 16, 8), 12: (8*6, 0, 16, 8), 11: (8*8, 0, 16, 8), 10: (8*10, 0, 16, 8),
                    9: (8*12, 0, 16, 8), 8: (8*14, 0, 16, 8), 7: (8*16, 0, 16, 8), 6: (8*18, 0, 16, 8), 5: (8*20, 0, 16, 8),
                    4: (8*22, 0, 16, 8), 3: (8*24, 0, 16, 8), 2: (8*26, 0, 16, 8), 1: (8*28, 0, 16, 8), 0: (8*30, 0, 16, 8)}
        pyxel.blt(6, 6, 0, self.vie['icon'][0], self.vie['icon'][1], self.vie['icon'][2], self.vie['icon'][3], 1)
        pyxel.blt(16, 6, 0, self.vie[14][0], self.vie[14][1], self.vie[14][2], self.vie[14][3], 1)
    
    def draw_sta(self):
        # Dictionnaire similaire à celui de la vie, mais pour l'energie
        self.sta = {'icon': (8, 8, 8, 8),
                    14: (8*2, 8, 16, 8), 13: (8*4, 8, 16, 8), 12: (8*6, 8, 16, 8), 11: (8*8, 8, 16, 8), 10: (8*10, 8, 16, 8),
                    9: (8*12, 8, 16, 8), 8: (8*14, 8, 16, 8), 7: (8*16, 8, 16, 8), 6: (8*18, 8, 16, 8), 5: (8*20, 8, 16, 8),
                    4: (8*22, 8, 16, 8), 3: (8*24, 8, 16, 8), 2: (8*26, 8, 16, 8), 1: (8*28, 8, 16, 8), 0: (8*30, 8, 16, 8)}
        pyxel.blt(6, 16, 0, self.sta['icon'][0], self.sta['icon'][1], self.sta['icon'][2], self.sta['icon'][3], 1)
        pyxel.blt(16, 16, 0, self.sta[14][0], self.sta[14][1], self.sta[14][2], self.sta[14][3], 1)

    def contours(self):
        pyxel.line(0, 0, 255, 0, 0)
        pyxel.line(0, 127, 255, 127, 0)
        pyxel.line(0, 0, 0, 127, 0)
        pyxel.line(40, 0, 40, 127, 0)
        pyxel.line(216, 0, 216, 127, 0)
        pyxel.line(255, 0, 255, 127, 0)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(1)
        self.draw_vie()
        self.draw_sta()
        self.contours()
        pyxel.rect(41, 1, 175, 126, 3)

HUD()