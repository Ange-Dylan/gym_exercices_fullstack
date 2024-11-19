# Gym API Project

## Description
Le **Gym API** est une application qui permet de gérer des données liées aux adhérents d'une salle de sport, incluant des fonctionnalités d'authentification, de gestion des utilisateurs et de suivi des entraînements. 

Ce projet est construit en utilisant **FastAPI** pour le back-end, **PostgreSQL** comme base de données, et il est conteneurisé avec **Docker**.

---

## Fonctionnalités
- **Authentification** : Gestion des utilisateurs via JWT (JSON Web Token).
- **CRUD Utilisateurs** : Ajouter, lire, mettre à jour et supprimer des informations d'utilisateurs.
- **Suivi des entraînements** : Analyse des données sur les entraînements des adhérents.
- **Swagger UI** : Documentation interactive pour tester les endpoints.
- **ReDoc** : Documentation technique alternative.

---

## Prérequis
Avant de commencer, assurez-vous d'avoir installé :
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.9](https://www.python.org/downloads/)

---

## Installation et Lancement

### 1. Cloner le dépôt

git clone https://github.com/votre-utilisateur/gym-api.git
cd gym-api
### 2. Configuration de l'environnement
Créez un fichier .env dans le répertoire racine du projet avec les informations suivantes :

DATABASE_URL=postgresql://postgres:password@db:5432/gym_database
SECRET_KEY=votre_cle_secrete
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
### 3. Lancer l'application avec Docker

docker-compose up --build
### 4. Accéder à l'application
Swagger UI : http://localhost:8000/docs
ReDoc : http://localhost:8000/redoc

## Structure du projet

gym-api/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py        # Configuration de la base de données
│   │   ├── models.py          # Définition des modèles SQLAlchemy
│   │   ├── schemas.py         # Schémas Pydantic pour validation
│   │   ├── routers/
│   │   │   ├── auth.py        # Routes d'authentification
│   │   │   ├── users.py       # Routes pour la gestion des utilisateurs
│   │   ├── utils.py           # Fonctions utilitaires (hash, JWT, etc.)
│   ├── __init__.py
├── init_data.py               # Script pour charger les données initiales
├── Dockerfile                 # Dockerfile pour l'application
├── docker-compose.yml         # Configuration Docker Compose
├── requirements.txt           # Dépendances Python
└── README.md                  # Documentation du projet
## Points importants
### Tests
Pour lancer les tests unitaires :

pytest tests/

### Gestion des données initiales
Le fichier init_data.py permet d'importer des données initiales dans la base de données depuis un fichier CSV.

Exécuter le script avec Docker :


docker exec -it gym_exercices_fullstack-backend python init_data.py
### Endpoints principaux
## Authentification
POST /auth/token : Obtenir un token JWT pour un utilisateur.
## Utilisateurs
- POST /users/ : Ajouter un nouvel utilisateur.
- GET /users/ : Lister tous les utilisateurs.
- GET /users/{user_id} : Récupérer les informations d'un utilisateur par ID.
- PUT /users/{user_id} : Mettre à jour les informations d'un utilisateur.
- DELETE /users/{user_id} : Supprimer un utilisateur.
### Contribution
Les contributions sont les bienvenues ! Pour contribuer :

Forkez ce dépôt.
Créez une branche (git checkout -b ma-branche).
Effectuez vos modifications.
Poussez vos modifications (git push origin ma-branche).
Créez une Pull Request.
### Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

### Contact
Pour toute question, contactez-nous à support@gymapi.com.



Vous pouvez télécharger ce fichier **README.md** directement si besoin. 