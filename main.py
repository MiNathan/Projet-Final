import pyxel
from HUD import HUD as H
from persos import classes as P



class main:
    def __init__(self, HUD, mc):
        pyxel.init(256, 128, title ="Dark Dungeon", fps= 60)
        pyxel.load('Ressources.pyxres')

        self.hud = HUD
        self.joueur = mc
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass
    
    def draw(self):
        self.hud.draw_HUD()
        self.joueur.draw_perso()

vie = 0
sta = 0
HUD = H.HUD(vie, sta)
mc = P.Perso('Joueur', 14, 14)

jeu = main(HUD, mc)