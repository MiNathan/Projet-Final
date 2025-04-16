import pyxel
from UI import UI as H
from persos import classes as P



class main:
    def __init__(self):
        pyxel.init(256, 129, title ="Dark Dungeon", fps= 60)
        pyxel.load('Ressources.pyxres')

        self.ui = H.UI(14, 14)
        self.joueur = P.Perso('Joueur', 14, 14)
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.joueur.act()
    
    def draw(self):
        self.ui.draw_UI()
        self.joueur.draw_perso()

jeu = main()