from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Clé primaire unique
    age = Column(Integer)  # Âge
    gender = Column(String)  # Sexe (Male/Female)
    weight_kg = Column(Float)  # Poids (en kg)
    height_m = Column(Float)  # Taille (en mètre)
    max_bpm = Column(Integer)  # Fréquence cardiaque maximale
    avg_bpm = Column(Integer)  # Fréquence cardiaque moyenne
    resting_bpm = Column(Integer)  # Fréquence cardiaque au repos
    session_duration_hours = Column(Float)  # Durée de la session (en heures)
    calories_burned = Column(Float)  # Calories brûlées
    workout_type = Column(String)  # Type d'entraînement (Yoga, HIIT, etc.)
    fat_percentage = Column(Float)  # Pourcentage de graisse corporelle
    water_intake_liters = Column(Float)  # Consommation d'eau (en litres)
    workout_frequency_days_week = Column(Integer)  # Fréquence d'entraînement (jours par semaine)
    experience_level = Column(String)  # Niveau d'expérience
    bmi = Column(Float)  # Indice de masse corporelle (BMI)