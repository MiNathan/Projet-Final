import pyxel
from HUD import HUD as H

class main:
    def __init__(self, HUD):
        pyxel.init(256, 128, title ="Dark Dungeon", fps= 60)
        pyxel.load('HUD/hud.pyxres')

        self.hud = HUD

        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass
    
    def draw(self):
        self.hud.draw_HUD()

vie = 0
sta = 0
HUD = H.HUD(vie, sta)

jeu = main(HUD)