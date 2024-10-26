class Stuf:
    def __init__(self):
        self.Stuf = {"Dégats": "", "Vitesses": "", "Defense": ""}
        self.Objets = {
            "Dégats": {'Torche': "2 atk", 'Epée de légende': "5 atk", 'Dague démoniaque': "7 atk", 'Fouchette': "1 degat", "Turbo-marteau": "9 atk"},
            "Specials": {'Objets mystères': "2 objets aléatoires", "Bouclier inébranlable": "9 def mais pas de bonus vitesse", "Spatule dorée": "6 pour toutes stats"},
            "Vitesses": {'Botte draconique': "5 vitesse", "Geox qui court vite": "8 vitesse", 'Botte du vieux pêcheur': "1 vitesse", "vieille sabate": "3 vitesse"},
            "Defense": {"Casque du roi arthur": "6 def", "Chapeau de paille": "2 def", "Casserole": "1 def", "Bouclier doré": "5 def"}
        }

    def ajouterobj(self, objet):
        for categorie, objets in self.Objets.items():
            if objet in objets:
                if categorie in self.Stuf:
                    self.Stuf[categorie] = objets[objet]  # Ajoute l'objet dans la bonne catégorie de l'inventaire
                    print(f"L'objet '{objet}' a été ajouté dans la catégorie '{categorie}'.")
                return
        print("Cet objet n'existe pas dans l'inventaire disponible.")

    def afficherobjs(self):
        print("Voici vos objets :")
        for categorie, objet in self.Stuf.items():
            print(f"{categorie}: {objet}")
