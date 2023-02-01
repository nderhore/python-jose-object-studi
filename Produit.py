class Produit:

     #encapsulation : définie la visibilité des attributs
     _libelle : str
     _description : str
     _prix : float
     _quantite : float
     _is_promo : bool


     #constructeur : construit un produit (plan d'architect)
     def __init__(self, libelle : str, description : str, prix : float,
                  quantite : float, is_promo : bool):
          self._prix = prix
          self._libelle = libelle
          self._description = description
          self._quantite = quantite
          self._is_promo = is_promo

     @property
     def libelle(self):
          return self._libelle

