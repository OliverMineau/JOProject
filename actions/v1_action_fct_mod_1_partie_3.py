import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

#Supprimer une epreuve

class AppFctMod1Partie3(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_fct_mod_1.ui", self)
        self.data = data
        self.refreshResult()
        
    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_mod_1, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT * FROM LesEpreuves")
        except Exception as e:
            self.ui.table_fct_mod_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_mod_1, "Impossible d'afficher les résultats : " + repr(e))
            print("Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_mod_1, result)
            
            
    # Fonction de supression
    @pyqtSlot()
    def supprimer(self):
        
        #On prend le numero de la ligne selectionnée et le numero de l'epreuve
        ligne = self.ui.table_fct_mod_1.currentRow()
        numEp = self.ui.table_fct_mod_1.item(ligne, 0).text()
        #On supprime la ligne
        self.ui.table_fct_mod_1.removeRow(ligne)
            
        display.refreshLabel(self.ui.label_fct_mod_1, "")
        try:
            #On supprime dans la bd
            cursor = self.data.cursor()
            result = cursor.execute(f"""
                                    DELETE FROM LesEpreuves
                                    WHERE numEp = {numEp}
                                    """)
            result = cursor.execute(f"""
                                    DELETE FROM LesInscriptions
                                    WHERE numEp = {numEp}
                                    """)
        except Exception as e:
            self.ui.table_fct_mod_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_mod_1, "Supression Impossible : " + repr(e))
