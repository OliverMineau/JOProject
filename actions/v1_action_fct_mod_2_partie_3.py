import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


class AppFctMod2Partie3(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_fct_mod_2.ui", self)
        self.data = data
        #self.insert_mod_2()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def insert_mod_2(self):
        try:
            numEp = [self.ui.table_fct_mod_2.item(0,0).text()]
            gold = [self.ui.table_fct_mod_2.item(0,1).text()]
            silver = [self.ui.table_fct_mod_2.item(0,2).text()]
            bronze = [self.ui.table_fct_mod_2.item(0,3).text()]
        except AttributeError:
            display.refreshLabel(self.ui.label_fct_mod_2, "Veuillez remplir la/les cases vides")
            return

        cases = [numEp[0], gold[0], silver[0], bronze[0]]
        for case in cases:
            flag = True
            try:
                int(case)
            except ValueError:
                flag = False
            if flag:
                print(case," is an integer")
            else:
                print(case," is not an integer")

        display.refreshLabel(self.ui.label_fct_mod_2, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("INSERT INTO LesResultats(numEp, gold, silver, bronze)" 
                                    "VALUES(%s, %s, %s, %s)" %(''.join(numEp),
                                                               ''.join(gold),
                                                               ''.join(silver),
                                                               ''.join(bronze)))
        except Exception as e:
            self.ui.table_fct_mod_2.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_mod_2, "Impossible d'afficher les résultats : " + repr(e))
            print("Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_mod_2, result)