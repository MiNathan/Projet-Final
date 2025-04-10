map = [['' for i in range(10)] for i in range(10)]

class Salle():
    """
    Classe permettant la création et le placement de salles sur la carte
    Attributs:
        taille, int: Toutes les salles font la même taille, mais une variable est nécessaire pour l'affichage graphique
        typ, str: L'icone représentant la salle sur la carte. ex: '+', '|', '--'...
        nb_mstr, int: Le nombre d'ennemis à placer dans la salle
    """

    def __init__(self, typ, nb_mstr):
        if typ in ['+', '--', '|', 'tr']: # '+': Croisement; '--': Horizontale; '|': Verticale: 'tr': Tresor
            self.typ = typ
        self.mstr = nb_mstr
