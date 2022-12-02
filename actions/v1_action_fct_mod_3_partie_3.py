import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

#Modifier une epreuve

class AppFctMod3Partie3(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_fct_mod_3.ui", self)
        self.data = data
        self.refreshResult()
        
    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_mod_3, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT * FROM LesSportifsEq")
        except Exception as e:
            self.ui.table_fct_mod_3.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_mod_3, "Impossible d'afficher les résultats : " + repr(e))
            print("Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_mod_3, result)
            
            
    # Fonction de supression
    @pyqtSlot()
    def modifier(self):
        ligne = self.ui.table_fct_mod_3.currentRow()
        numSp = self.ui.table_fct_mod_3.item(ligne, 0).text()  # get cell at row, col
        self.ui.table_fct_mod_3.removeRow(ligne)
        
        nom = self.ui.lineEdit_nom.text()
        prenom = self.ui.lineEdit_prenom.text()
        
        display.refreshLabel(self.ui.label_fct_mod_3, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(f"""
                                    UPDATE LesSportifsEq
                                    SET nomSp = '{nom}', prenomSp = '{prenom}'
                                    WHERE numSp = {numSp}
                                    """)
        except Exception as e:
            self.ui.table_fct_mod_3.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_mod_3, "Modification Impossible : " + repr(e))
            print(repr(e))
        else:
            self.refreshResult()

