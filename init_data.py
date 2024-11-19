import csv
from backend.app.database import SessionLocal, Base, engine
from backend.app.models import User

# Supprime toutes les tables et les recrée
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Fonction pour charger les données depuis le fichier CSV
def load_data():
    session = SessionLocal()
    try:
        # Chemin vers le fichier CSV
        csv_file_path = "/app/dataset/gym_members_exercise_tracking.csv"
        
        # Ouvrir le fichier CSV et insérer les données
        with open(csv_file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Création d'un utilisateur (ajustez selon vos modèles)
                user = User(
                    age=int(row["Age"]),
                    gender=row["Gender"],
                    weight_kg=float(row["Weight (kg)"]),
                    height_m=float(row["Height (m)"]),
                    max_bpm=int(row["Max_BPM"]),
                    avg_bpm=int(row["Avg_BPM"]),
                    resting_bpm=int(row["Resting_BPM"]),
                    session_duration_hours=float(row["Session_Duration (hours)"]),
                    calories_burned=float(row["Calories_Burned"]),
                    workout_type=row["Workout_Type"],
                    fat_percentage=float(row["Fat_Percentage"]),
                    water_intake_liters=float(row["Water_Intake (liters)"]),
                    workout_frequency_days_week=int(row["Workout_Frequency (days/week)"]),
                    experience_level=row["Experience_Level"],
                    bmi=float(row["BMI"]),
                )
                session.add(user)  # Ajouter l'utilisateur à la session
            
        session.commit()  # Enregistrer les données dans la base
        print("Les données ont été insérées avec succès dans la base de données.")
    except Exception as e:
        session.rollback()
        print(f"Erreur lors de l'insertion des données : {e}")
    finally:
        session.close()

# Exécution du script
if __name__ == "__main__":
    load_data()