# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:43:18 2024

@author: Soso chouw
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import psycopg2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interface.ui", self)  # Charger l'interface utilisateur depuis le fichier interface.ui

        # Connexion du signal "clicked" du bouton à la méthode get_input_data
        self.pushButton.clicked.connect(self.get_input_data)

    def get_input_data(self):
        # Récupérer les valeurs saisies dans les champs d'entrée
        nom_ressource = self.lineEdit_1.text()
        craft_1 = self.lineEdit_2.text()
        craft_2 = self.lineEdit_3.text()
        craft_3 = self.lineEdit_4.text()
        craft_4 = self.lineEdit_5.text()
        craft_5 = self.lineEdit_6.text()
        craft_6 = self.lineEdit_7.text()
        craft_7 = self.lineEdit_8.text()
        craft_8 = self.lineEdit_9.text()
        quantité_1 = int(self.lineEdit_10.text()) if self.lineEdit_10.text() else 0
        quantité_2 = int(self.lineEdit_11.text()) if self.lineEdit_11.text() else 0
        quantité_3 = int(self.lineEdit_12.text()) if self.lineEdit_12.text() else 0
        quantité_4 = int(self.lineEdit_13.text()) if self.lineEdit_13.text() else 0
        quantité_5 = int(self.lineEdit_14.text()) if self.lineEdit_14.text() else 0
        quantité_6 = int(self.lineEdit_15.text()) if self.lineEdit_15.text() else 0
        quantité_7 = int(self.lineEdit_16.text()) if self.lineEdit_16.text() else 0
        quantité_8 = int(self.lineEdit_17.text()) if self.lineEdit_17.text() else 0

        # Afficher les valeurs récupérées
        print("Nom de la ressource :", nom_ressource)
        print("Craft 1 :", craft_1, "Quantité 1 :", quantité_1)
        print("Craft 2 :", craft_2, "Quantité 2 :", quantité_2)
        print("Craft 3 :", craft_3, "Quantité 3 :", quantité_3)
        print("Craft 4 :", craft_4, "Quantité 4 :", quantité_4)
        print("Craft 5 :", craft_5, "Quantité 5 :", quantité_5)
        print("Craft 6 :", craft_6, "Quantité 6 :", quantité_6)
        print("Craft 7 :", craft_7, "Quantité 7 :", quantité_7)
        print("Craft 8 :", craft_8, "Quantité 8 :", quantité_8)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())