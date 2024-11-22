from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional


# Base Schema for User
class UserBase(BaseModel):
    username: str
    age: Optional[int] = Field(None, description="Âge de l'utilisateur")
    gender: Optional[str] = Field(None, description="Genre de l'utilisateur")
    weight_kg: Optional[float] = Field(None, description="Poids de l'utilisateur en kg")
    height_m: Optional[float] = Field(None, description="Taille de l'utilisateur en mètres")
    max_bpm: Optional[int] = Field(None, description="Fréquence cardiaque maximale de l'utilisateur")
    avg_bpm: Optional[int] = Field(None, description="Fréquence cardiaque moyenne de l'utilisateur")
    resting_bpm: Optional[int] = Field(None, description="Fréquence cardiaque au repos de l'utilisateur")
    session_duration_hours: Optional[float] = Field(None, description="Durée des sessions d'entraînement en heures")
    calories_burned: Optional[float] = Field(None, description="Calories brûlées pendant les sessions")
    workout_type: Optional[str] = Field(None, description="Type d'entraînement de l'utilisateur")
    fat_percentage: Optional[float] = Field(None, description="Pourcentage de graisse corporelle")
    water_intake_liters: Optional[float] = Field(None, description="Quantité d'eau consommée en litres")
    workout_frequency_days_week: Optional[int] = Field(None, description="Fréquence des entraînements par semaine")
    experience_level: Optional[str] = Field(None, description="Niveau d'expérience de l'utilisateur")
    bmi: Optional[float] = Field(None, description="Indice de masse corporelle (IMC)")

    model_config = ConfigDict(from_attributes=True)  # Remplacement de orm_mode par from_attributes

# Schéma pour mettre à jour un utilisateur
class UserUpdate(BaseModel):
    age: Optional[int] = None
    gender: Optional[str] = None
    weight_kg: Optional[float] = None
    height_m: Optional[float] = None
    max_bpm: Optional[int] = None
    avg_bpm: Optional[int] = None
    resting_bpm: Optional[int] = None
    session_duration_hours: Optional[float] = None
    calories_burned: Optional[float] = None
    workout_type: Optional[str] = None
    fat_percentage: Optional[float] = None
    water_intake_liters: Optional[float] = None
    workout_frequency_days_week: Optional[int] = None
    experience_level: Optional[str] = None
    bmi: Optional[float] = None

# Schema for creating a new user
class UserCreate(UserBase):
    password: str = Field(..., description="Mot de passe de l'utilisateur")


# Schema for user response
class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # Remplacement de orm_mode par from_attributes


# Schema for user login request
class LoginRequest(BaseModel):
    username: str = Field(..., description="Nom d'utilisateur")
    password: str = Field(..., description="Mot de passe")


# Schema for token response
class Token(BaseModel):
    access_token: str = Field(..., description="Token d'accès pour l'utilisateur")
    token_type: str = Field(..., description="Type de token")


# Schema for token data
class TokenData(BaseModel):
    username: Optional[str] = None