import csv
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal, engine, Base
from backend.app.models import User  # Remplacez "User" par vos modèles si nécessaire

# Importez le modèle de base
Base.metadata.create_all(bind=engine)

# Fonction pour charger les données
def load_data():
    # Ouvrez une session de base de données
    session = SessionLocal()

    # Chemin vers votre dataset CSV
    csv_file_path = "/app/dataset/gym_members_exercise_tracking.csv"

    # Chargement des données depuis le fichier CSV
    with open(csv_file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Création d'un utilisateur (ajustez selon vos modèles)
            user = User(
                age=int(row["Age"]),
                gender=row["Gender"],
                weight=float(row["Weight (kg)"]),
                height=float(row["Height (m)"]),
            )
            session.add(user)

    # Commit des données dans la base
    session.commit()
    session.close()

# Appel de la fonction lors de l'exécution directe du script
if __name__ == "__main__":
    load_data()