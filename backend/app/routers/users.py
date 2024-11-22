from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal
from backend.app.models import User
from backend.app.schemas import UserResponse, UserCreate, UserUpdate  # Import du schéma Pydantic pour validation
from typing import Optional
from backend.app.utils import hash_password

router = APIRouter()

# Fonction utilitaire pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route pour lire tous les utilisateurs
@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/filter", response_model=list[UserResponse])
def filter_users(
    gender: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    workout_type: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
    Filtre les utilisateurs selon différents critères.
    """
    query = db.query(User)
    if gender:
        query = query.filter(User.gender == gender)
    if min_age is not None:
        query = query.filter(User.age >= min_age)
    if max_age is not None:
        query = query.filter(User.age <= max_age)
    if workout_type:
        query = query.filter(User.workout_type == workout_type)

    return query.all()

# Route pour créer un nouvel utilisateur
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Hache le mot de passe avant de créer l'utilisateur
    hashed_password = hash_password(user.password)
    user_data = user.dict()
    user_data.pop("password")  # Supprime le mot de passe en clair
    new_user = User(**user_data, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_data: UserUpdate, db: Session = Depends(get_db)):
    """
    Met à jour les données d'un utilisateur existant.
    """
    # Recherche de l'utilisateur
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Mise à jour des champs fournis
    updated_data_dict = updated_data.dict(exclude_unset=True)  # Ignore les champs non définis
    for key, value in updated_data_dict.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Supprime un utilisateur par son ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": f"User with ID {user_id} has been deleted"}