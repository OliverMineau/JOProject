
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fenêtre de visualisation des données
class AppTablesDataV1(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_tablesData.ui", self)
        self.data = data

        # On met à jour l'affichage avec les données actuellement présentes dans la base
        self.refreshAllTablesV1()

    ####################################################################################################################
    # Méthodes permettant de rafraichir les différentes tables
    ####################################################################################################################

    # Fonction de mise à jour de l'affichage d'une seule table
    def refreshTable(self, label, table, query):
        display.refreshLabel(label, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(query)
        except Exception as e:
            table.setRowCount(0)
            display.refreshLabel(label, "Impossible d'afficher les données de la table : " + repr(e))
        else:
            display.refreshGenericData(table, result)

    # Fonction permettant de mettre à jour toutes les tables
    @pyqtSlot()
    def refreshAllTablesV1(self):

        self.refreshTable(self.ui.label_epreuves, self.ui.tableEpreuves, "SELECT numEp, nomEp, formeEp, nomDi, categorieEp, nbSportifsEp, dateEp FROM LesEpreuves")
        self.refreshTable(self.ui.label_sportifs, self.ui.tableSportifs, "SELECT * FROM LesSportifsEQ")
        
        self.refreshTable(self.ui.label_inscriptions, self.ui.tableInscriptions, "SELECT numIn, numEp FROM LesInscriptions")
        self.refreshTable(self.ui.label_resultats, self.ui.tableResultats, "SELECT numEp, gold, silver, bronze FROM LesResultats")

        # DONE 1.3 : modifier pour afficher les nouveaux éléments (il faut aussi changer le fichier .ui correspondant)
        # TODO 1.4b : ajouter l'affichage des éléments de la vue LesAgesSportifs après l'avoir créée
        self.refreshTable(self.ui.label_agesSportifs, self.ui.tableAgesSportifs, "SELECT numSp, nomSp, prenomSp, pays, categorieSp, dateNaisSp, strftime('%Y', 'now') + strftime('%j', 'now') / 365 - (strftime('%Y', dateNaisSp) + strftime('%j', dateNaisSp) / 365) AS ageSp FROM LesSportifsEQ")
        # TODO 1.5b : ajouter l'affichage des éléments de la vue LesNbsEquipiers après l'avoir créée
        self.refreshTable(self.ui.label_nbsEquipiers, self.ui.tableNbsEquipiers, "SELECT numEq, COUNT(numSp) AS nbEquipiersEq FROM LesSportifsEQ GROUP BY numEq HAVING numEq IS NOT NULL")