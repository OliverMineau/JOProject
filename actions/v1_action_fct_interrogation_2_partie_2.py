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
            result = cursor.execute("""
                                    WITH Pays AS (
                                        SELECT DISTINCT numSp AS num, pays
                                        FROM LesSportifsEq
                                        UNION ALL
                                        SELECT DISTINCT numEq AS num, pays
                                        FROM LesSportifsEq
                                        WHERE numEq IS NOT NULL
                                    ), 
                                    PaysGold AS (
                                        SELECT pays, COUNT(pays) AS gold
                                        FROM Pays P JOIN LesResultats R ON (P.num=R.gold)
                                        GROUP BY pays
                                    ), 
                                    PaysSilver AS (
                                        SELECT pays, COUNT(pays) AS silver
                                        FROM Pays P JOIN LesResultats R ON (P.num=R.silver)
                                        GROUP BY pays
                                    ), 
                                    PaysBronze AS (
                                        SELECT pays, COUNT(pays) AS bronze
                                        FROM Pays P JOIN LesResultats R ON (P.num=R.bronze)
                                        GROUP BY pays
                                    ), 
                                    Meds AS (
                                        SELECT pays, gold, 0 AS silver, 0 AS bronze
                                        FROM Pays P JOIN PaysGold USING(pays)
                                        UNION ALL
                                        SELECT pays, 0 AS gold, silver, 0 AS bronze
                                        FROM Pays P JOIN PaysSilver USING(pays)
                                        UNION ALL
                                        SELECT pays, 0 AS gold, 0 AS silver, bronze
                                        FROM Pays P JOIN PaysBronze USING(pays)
                                    ), 
                                    MedParPays AS (
                                        SELECT pays, MAX(gold) AS gold, MAX(silver) AS silver, MAX(bronze) AS bronze
                                        FROM Meds
                                        GROUP BY pays
                                    )
                                    SELECT pays, gold, silver, bronze
                                    FROM MedParPays
                                    ORDER BY (gold+silver+bronze) DESC
                                    """)
        except Exception as e:
            self.ui.table_fct_interrogation_2.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_interrogation_2, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_interrogation_2, result)