# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:43:18 2024

@author: Soso chouw
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import psycopg2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interface.ui", self)  # Charger l'interface utilisateur depuis le fichier interface.ui

        # Connexion du signal "clicked" du bouton à la méthode get_input_data
        self.pushButton.clicked.connect(self.get_input_data)
        
        # Définir les attributs pour stocker les valeurs
        self.nom_ressource = None
        self.crafts = [None] * 8
        self.nombres = [0] * 8
        self.prix_item = 0

    def get_input_data(self):
        # Récupérer les valeurs saisies dans les champs d'entrée
        self.nom_ressource = self.lineEdit_1.text()
        self.crafts[0] = self.lineEdit_2.text() or ""
        self.crafts[1] = self.lineEdit_3.text() or ""
        self.crafts[2] = self.lineEdit_4.text() or ""
        self.crafts[3] = self.lineEdit_5.text() or ""
        self.crafts[4] = self.lineEdit_6.text() or ""
        self.crafts[5] = self.lineEdit_7.text() or ""
        self.crafts[6] = self.lineEdit_8.text() or ""
        self.crafts[7] = self.lineEdit_9.text() or ""
        self.nombres[0] = int(self.lineEdit_10.text()) if self.lineEdit_10.text() else 0
        self.nombres[1] = int(self.lineEdit_11.text()) if self.lineEdit_11.text() else 0
        self.nombres[2] = int(self.lineEdit_12.text()) if self.lineEdit_12.text() else 0
        self.nombres[3] = int(self.lineEdit_13.text()) if self.lineEdit_13.text() else 0
        self.nombres[4] = int(self.lineEdit_14.text()) if self.lineEdit_14.text() else 0
        self.nombres[5] = int(self.lineEdit_15.text()) if self.lineEdit_15.text() else 0
        self.nombres[6] = int(self.lineEdit_16.text()) if self.lineEdit_16.text() else 0
        self.nombres[7] = int(self.lineEdit_17.text()) if self.lineEdit_17.text() else 0
        self.prix_item = int(self.lineEdit_18.text()) if self.lineEdit_18.text() else 0
        
        #séparer les centaines par un espace
        #self.prix_item = f'{self.prix_item:,.0f}'.replace(',', ' ')
        
        print("Nom de la ressource :", self.nom_ressource)
        print("Crafts :", self.crafts)
        print("Nombres :", self.nombres)
        print("Prix de l'item :", self.prix_item)

        # Appeler la méthode pour télécharger les données dans la base de données
        self.upload_form()

    def upload_form(self):
        try:
            # Connexion à la base de données PostgreSQL
            conn = psycopg2.connect(
                host='localhost',
                database='postgres',
                user='postgres',
                password='admin',
                port=5432  # Utilisez le port par défaut de PostgreSQL
            )
    
            # On crée un curseur qui permet de véhiculer de l'information entre la base de données et Python
            cur = conn.cursor()
    
            # On prend le curseur et on lui fait exécuter une commande SQL pour créer une table si elle n'existe pas
            cur.execute("""
                        INSERT INTO Tableau (nom, craft_1, nombre_1, craft_2, nombre_2, craft_3, nombre_3, craft_4, nombre_4, craft_5, nombre_5, craft_6, nombre_6, craft_7, nombre_7, craft_8, nombre_8, prix_item)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (
                        self.nom_ressource, 
                        str(self.crafts[0]), str(self.nombres[0]), 
                        str(self.crafts[1]), str(self.nombres[1]), 
                        str(self.crafts[2]), str(self.nombres[2]), 
                        str(self.crafts[3]), str(self.nombres[3]), 
                        str(self.crafts[4]), str(self.nombres[4]), 
                        str(self.crafts[5]), str(self.nombres[5]), 
                        str(self.crafts[6]), str(self.nombres[6]), 
                        str(self.crafts[7]), str(self.nombres[7]), 
                        str(self.prix_item))
                        )

            # On valide les modifications
            conn.commit()
            print("Données insérées avec succès dans la table 'Tableau' !")
    
        except psycopg2.Error as e:
            print("Erreur lors de l'insertion des données dans la table :", e)
    
        finally:
            # On ferme le curseur et la connexion quand on arrête d'utiliser la base de données
            cur.close()
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())