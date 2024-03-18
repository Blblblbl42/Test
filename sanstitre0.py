# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:48:41 2024

@author: Soso chouw
"""

import psycopg2

def upload_form():
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
            CREATE TABLE Tableau (
                id SERIAL PRIMARY KEY,
                nom VARCHAR(255),
                type VARCHAR(255),
                craft_1 VARCHAR(255),
                nombre_1 INT,
                craft_2 VARCHAR(255),
                nombre_2 INT,
                craft_3 VARCHAR(255),
                nombre_3 INT,
                craft_4 VARCHAR(255),
                nombre_4 INT,
                craft_5 VARCHAR(255),
                nombre_5 INT,
                craft_6 VARCHAR(255),
                nombre_6 INT,
                craft_7 VARCHAR(255),
                nombre_7 INT,
                craft_8 VARCHAR(255),
                nombre_8 INT,
                prix_craft FLOAT,
                prix_item FLOAT,
                Bénéfice FLOAT
            )
        """)
        # On valide les modifications
        conn.commit()
        print("Table 'Tableau' créée avec succès !")

    except psycopg2.Error as e:
        print("Erreur lors de la création de la table :", e)

    finally:
        # On ferme le curseur et la connexion quand on arrête d'utiliser la base de données
        cur.close()
        conn.close()

upload_form()
