FROM python:3.9-slim

WORKDIR /app

# Copie le fichier requirements.txt et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le dossier backend
COPY ./backend /app/backend

# Copie init_data.py dans le répertoire de travail du conteneur
COPY ./init_data.py /app/init_data.py

# Exposer le port sur lequel FastAPI écoute
EXPOSE 8000

# Commande par défaut pour lancer l'application
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]