import csv
from sqlalchemy.orm import Session
from backend.app.models import User
from backend.app.database import SessionLocal, engine

# Initialiser la base de données
from backend.app.models import Base
Base.metadata.create_all(bind=engine)

# Charger les données
def load_data():
    session = SessionLocal()
    with open('dataset/gym_members_exercise_tracking.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = User(
                name=row['Name'],
                age=int(row['Age']),
                gender=row['Gender'],
                weight=float(row['Weight (kg)']),
                height=float(row['Height (m)'])
            )
            session.add(user)
        session.commit()
    session.close()

if __name__ == "__main__":
    load_data()