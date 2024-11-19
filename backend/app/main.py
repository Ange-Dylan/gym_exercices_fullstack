from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from backend.app.routers import auth, users  # Import des fichiers de routes

app = FastAPI(
    title="Gym API",
    description="Une API permettant de gérer les données relatives aux adhérents qui font du sport en salle, avec des fonctionnalités d'authentification, gestion des utilisateurs, et bien plus encore :)",
    version="1.0.0",
    contact={
        "name": "Support API",
        "email": "support@gymapi.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Inclusion des routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", response_class=HTMLResponse)
def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gym API</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f3f4f6;
                color: #1a202c;
            }
            .header {
                background-color: #0073e6;
                padding: 1.5em;
                text-align: center;
                color: white;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .header h1 {
                margin: 0;
                font-size: 2.5em;
            }
            .container {
                max-width: 900px;
                margin: 2em auto;
                background: white;
                padding: 2em;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                animation: fadeIn 1.5s ease-in-out;
            }
            ul {
                line-height: 1.8;
            }
            a {
                color: #0073e6;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            footer {
                text-align: center;
                padding: 1em;
                margin-top: 2em;
                font-size: 0.9em;
                color: #4a5568;
            }
            footer a {
                color: #0073e6;
            }
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Bienvenue sur le Gym API</h1>
            <p>Votre solution complète pour la gestion d'adhérents et des entraînements cardiovasculaires</p>
        </div>
        <div class="container">
            <h2>À propos de l'API</h2>
            <p>Cette API permet de :</p>
            <ul>
                <li>Gérer les utilisateurs et leurs informations personnelles.</li>
                <li>Suivre les sessions d'entraînement et les performances.</li>
                <li>Fournir des outils d'authentification sécurisés.</li>
            </ul>
            <h2>Ressources disponibles</h2>
            <ul>
                <li><a href="/docs" target="_blank">Documentation Swagger</a> - Explorez et testez l'API.</li>
                <li><a href="/redoc" target="_blank">Documentation ReDoc</a> - Documentation détaillée et stylée.</li>
                <li>
                    <strong>Routes principales :</strong>
                    <ul>
                        <li><strong>/auth</strong> - Gestion de l'authentification (connexion, tokens).</li>
                        <li><strong>/users</strong> - Gestion des utilisateurs (CRUD).</li>
                    </ul>
                </li>
            </ul>
            <h2>Contact</h2>
            <p>Version: <strong>1.0.0</strong></p>
            <p>Support: <a href="mailto:support@gymapi.com">support@gymapi.com</a></p>
        </div>
        <footer>
            &copy; 2024 Gym API | <a href="https://opensource.org/licenses/MIT" target="_blank">MIT License</a>
        </footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)