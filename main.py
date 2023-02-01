# This is a sample Python script.
import datetime

from Produit import Produit
from Catalogue import Catalogue


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Generation du premier Catalogue")
    mon_catalogue: Catalogue = Catalogue("premier catalogue", datetime.datetime.now(),
                                         datetime.datetime.now(), " test ", 21)

    print("ajout d'un produit dans mon catalogue")
    mon_catalogue.add_product(Produit("sauce soja", "pour sucrer vos sushis",
                                      15.0, 2.0, True))

    for i in mon_catalogue.list_product:
        print(str(i.libelle))