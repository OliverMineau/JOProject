import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

#Ajout de resultats

class AppFctMod2Partie3(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_fct_mod_2.ui", self)
        self.data = data

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def insert_mod_2(self):
        
        #On recupere les données à inserer
        try:
            numEp = self.ui.table_fct_mod_2.item(0,0).text()
            gold = self.ui.table_fct_mod_2.item(0,1).text()
            silver = self.ui.table_fct_mod_2.item(0,2).text()
            bronze = self.ui.table_fct_mod_2.item(0,3).text()
        except AttributeError:
            display.refreshLabel(self.ui.label_fct_mod_2, "Veuillez remplir la/les cases vides")
            return

        #On test si ce sont des nombres
        cases = [numEp, gold, silver, bronze]
        for case in cases:
            
            try:
                int(case)
            except ValueError:
                display.refreshLabel(self.ui.label_fct_mod_2, "Veuillez remplir correctement, uniquement de chiffres")
                return

        #On insere dans la bd
        display.refreshLabel(self.ui.label_fct_mod_2, "")
        try:
            cursor = self.data.cursor()
                
            cursor.execute("INSERT INTO LesResultats(numEp, gold, silver, bronze)" 
                                    "VALUES(%s, %s, %s, %s)" %(numEp,
                                                               gold,
                                                               silver,
                                                               bronze))
        except Exception as e:
            display.refreshLabel(self.ui.label_fct_mod_2, "Impossible d'ajouter ce resultat, l'epreuve ou les participants n'existent pas")
            print(repr(e))
        else:
            for i in range(4):
                self.ui.table_fct_mod_2.item(0,i).setText('')