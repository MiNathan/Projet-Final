import pyxel
import UI as U
import classes as C

objets = []

class main:
    """
    Classe pyxel principale pour la fenêtre graphique
    Regroupe les autres fichiers de code
    """
    def __init__(self):
        pyxel.init(256, 129, title ="Dark Dungeon", fps= 60)
        pyxel.load('Ressources.pyxres')

        self.ui = U.UI(14, 14)
        self.joueur = C.Perso('Joueur', 14, 14)
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        objs = objets
        objets = self.joueur.act(objs)
        self.ui.debug()
        print(objets)
    
    def draw(self):
        objets.append(C.Objet("coffre", 40+8*5, 8*5))
        objets.append(C.Objet("piece", 40+8*6, 8*6))
        self.ui.draw_UI()
        for obj in objets:
            obj.draw_obj()
        self.joueur.draw_perso()

main()