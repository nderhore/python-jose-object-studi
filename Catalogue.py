import datetime

from Produit import Produit


class Catalogue:
    _libelle: str
    _date_debut: datetime.datetime
    _date_fin: datetime.datetime
    _slogan: str
    _nb_page: int
    _list_product: list

    def __init__(self, libelle: str, date_debut: datetime.datetime, date_fin: datetime.datetime,
                 slogan: str, nb_page: int):
        self._libelle = libelle
        self._date_fin = date_fin
        self._date_debut = date_debut
        self._slogan = slogan
        self._nb_page = nb_page
        self._list_product = []

    def add_product(self, product: Produit):
        self._list_product.append(product)

    def remove_product(self, product: Produit):
        self._list_product.remove(product)


    @property
    def list_product(self):
        return self._list_product