from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal
from backend.app.models import User
from backend.app.schemas import UserResponse, UserCreate  # Import du schéma Pydantic pour validation

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

# Route pour filtrer les utilisateurs par critères (genre, âge, type d'entraînement)
@router.get("/filter")
def filter_users(
    gender: str = None,
    min_age: int = None,
    max_age: int = None,
    workout_type: str = None,
    db: Session = Depends(get_db),
):
    query = db.query(User)

    if gender:
        query = query.filter(User.gender == gender)
    if min_age:
        query = query.filter(User.age >= min_age)
    if max_age:
        query = query.filter(User.age <= max_age)
    if workout_type:
        query = query.filter(User.workout_type == workout_type)

    return query.all()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Route pour mettre à jour un utilisateur existant
@router.put("/{user_id}")
def update_user(user_id: int, updated_data: UserCreate, db: Session = Depends(get_db)):
    # Recherchez l'utilisateur à mettre à jour
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Mettez à jour les champs avec les nouvelles données
    for key, value in updated_data.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user

# Route pour supprimer un utilisateur (optionnel si besoin)
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Recherchez l'utilisateur à supprimer
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Supprimez l'utilisateur
    db.delete(user)
    db.commit()

    return {"detail": f"User with ID {user_id} has been deleted"}