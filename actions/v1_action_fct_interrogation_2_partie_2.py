import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction d'interrogation 2 sur BD V1
class AppFctInterrogation2Partie2(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_fct_interrogation_2.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_interrogation_2, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("""             """)
        except Exception as e:
            self.ui.table_fct_interrogation_2.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_interrogation_2, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_interrogation_2, result)