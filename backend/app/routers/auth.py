from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..utils import create_access_token, verify_password
from ..models import User
from .users import get_db
from ..schemas import UserResponse, Token, LoginRequest  # Import des schémas pour validation

router = APIRouter()

@router.post("/token", response_model=Token, summary="Authenticate user and retrieve access token")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Authentifie un utilisateur avec son nom d'utilisateur et son mot de passe.
    Retourne un token d'accès si les informations sont valides.
    """
    # Vérification de l'existence de l'utilisateur
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # Vérification du mot de passe
    if not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # Génération du token d'accès
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}