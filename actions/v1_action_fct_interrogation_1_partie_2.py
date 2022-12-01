import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction d'interrogation 1 sur BD V1
class AppFctInterrogation1Partie2(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_fct_interrogation_1.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_interrogation_1, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("""
                                    SELECT S.numEq, ROUND(AVG(A.ageSp),2) AS ageMoyen
                                    FROM LesAgesSportifs A JOIN LesSportifsEQ S ON (A.numSp = S.numSp)
                                    GROUP BY S.numEQ   
                                    HAVING S.numEq IN ( SELECT gold FROM LesResultats)""")
        except Exception as e:
            self.ui.table_fct_interrogation_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_interrogation_1, "Impossible d'afficher les résultats : " + repr(e))
            print("Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_interrogation_1, result)