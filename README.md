# Gym API Project

## Description
Une application web complète pour gérer les utilisateurs d'une salle de sport. Ce projet comprend une API REST construite avec **FastAPI**, une interface utilisateur d'administration construite en **HTML/CSS/JavaScript**, et une base de données **PostgreSQL**. Tout est entièrement déployable avec **Docker**.


---

## Fonctionnalités
- **Authentification** : Gestion des utilisateurs via JWT (JSON Web Token).
- **CRUD Utilisateurs** : Ajouter, lire, mettre à jour, filtrage par âge, genre, type de training etc. et supprimer des informations d'utilisateurs.
- **Suivi des entraînements** : Analyse des données sur les entraînements des adhérents.
- **Tableau de bord** : Visualisez les statistiques d'entraînement en utilisant des graphiques interactifs.
- **Docker Compose** : Déploiement simplifié
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

git clone https://github.com/Ange-Dylan/gym_exercices_fullstack.git
cd gym_exercices_fullstack
### 2. OPTIONNEL : Configuration de l'environnement
Optionnel : Créez un fichier si nécessaire .env dans le répertoire racine du projet avec les informations suivantes :

DATABASE_URL=postgresql://postgres:password@db:5432/gym_database
SECRET_KEY=votre_cle_secrete
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
### 3. Lancer l'application avec Docker
docker-compose down
docker-compose up --build
### 4. Accéder à l'application
Tous les liens sont sur la page de garde dans tous les cas !  

Dashboard : http://localhost:8000/dashboard
Swagger UI : http://localhost:8000/docs
ReDoc : http://localhost:8000/redoc

## Structure du projet

## Points importants

### Gestion des données initiales
Le fichier init_data.py permet d'importer des données initiales dans la base de données depuis un fichier CSV.

Exécuter le script avec Docker :


docker exec -it gym_exercices_fullstack-backend python init_data.py
## Endpoints principaux
### Authentification
POST /auth/token : Obtenir un token JWT pour un utilisateur.
### Utilisateurs
- POST /users/ : Ajouter un nouvel utilisateur.
- GET /users/ : Lister tous les utilisateurs.
- GET /users/{user_id} : Récupérer les informations d'un utilisateur par ID.
- PUT /users/{user_id} : Mettre à jour les informations d'un utilisateur.
- DELETE /users/{user_id} : Supprimer un utilisateur.

## Interface Admin
L'interface utilisateur admin.html permet de :
IMPORTANT : pour la connexion il faut mettre "admin" en username et "adminpassword" pour le password hashé !
- Afficher la liste des utilisateurs.
- Créer un utilisateur avec validation (confirmation de mot de passe).
- Supprimer un utilisateur avec une confirmation.
- Utiliser une interface ergonomique avec défilement horizontal pour gérer les colonnes étendues.
  
## Développement
### Installation locale
Si vous ne souhaitez pas utiliser Docker, voici comment exécuter l'application localement :

1. Installez les dépendances :


pip install -r requirements.txt
2. Configurez la base de données dans backend/app/database.py.

3. Lancez le serveur :

uvicorn backend.main:app --reload

## Améliorations futures
- Interface client : Développement d'une interface pour les utilisateurs finaux.
- Graphiques interactifs : Ajout d'analyses et de visualisations pour les données d'entraînement.
- Tests automatisés : Étendre la couverture des tests avec Pytest.


  
## Contribution
Les contributions sont les bienvenues ! Pour contribuer :

Forkez ce dépôt.
Créez une branche (git checkout -b ma-branche).
Effectuez vos modifications.
Poussez vos modifications (git push origin ma-branche).
Créez une Pull Request.
## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

## Auteurs
[Rémi Labou & Ange-Dylan Gnaglo] - Développeur principal

## Contact
Pour toute question, contactez-nous à support@gymapi.com ou plutôt ange-dylan.gnaglo@edu.esiee.fr / remi.labou@edu.esiee.fr.



Vous pouvez télécharger ce fichier **README.md** directement si besoin. 
