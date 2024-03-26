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
        self.prix_item = int(self.lineEdit_18.text()) if self.lineEdit_18.text() else 0
        for i in range(8):
            for i in range(8):
                self.crafts[i] = getattr(self, f"lineEdit_{i+2}").text() or ""
                self.nombres[i] = int(getattr(self, f"lineEdit_{i+10}").text()) if getattr(self, f"lineEdit_{i+10}").text() else 0
        
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
    
            # Préparation des données pour l'insertion
            values = [self.nom_ressource]
            for i in range(8):
                values.append(str(self.crafts[i]))
                values.append(str(self.nombres[i]))
            values.append(str(self.prix_item))
            
            # Création de la requête SQL avec les paramètres dynamiques
            sql_query = """
                INSERT INTO Tableau (nom, craft_1, nombre_1, craft_2, nombre_2, craft_3, nombre_3, craft_4, nombre_4, craft_5, nombre_5, craft_6, nombre_6, craft_7, nombre_7, craft_8, nombre_8, prix_item)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Exécution de la requête SQL
            cur.execute(sql_query, values)

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