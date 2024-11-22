from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import plotly.express as px
import plotly.io as pio
from backend.app.routers import auth, users  # Import des fichiers de routes
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

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

# Ajout du frontend
app.mount("/frontend", StaticFiles(directory="./frontend"), name="frontend")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chargement du fichier CSV
def load_csv():
    csv_path = "dataset/gym_members_exercise_tracking.csv"
    try:
        data = pd.read_csv(csv_path)
        return data
    except FileNotFoundError:
        return None

# Page d'accueil
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
            body {{
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f3f4f6;
                color: #1a202c;
            }}
            .header {{
                background-color: #0073e6;
                padding: 1.5em;
                text-align: center;
                color: white;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .header h1 {{
                margin: 0;
                font-size: 2.5em;
            }}
            .container {{
                max-width: 900px;
                margin: 2em auto;
                background: white;
                padding: 2em;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                animation: fadeIn 1.5s ease-in-out;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1.5em 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #0073e6;
                color: white;
            }}
            footer {{
                text-align: center;
                padding: 1em;
                margin-top: 2em;
                font-size: 0.9em;
                color: #4a5568;
            }}
            footer a {{
                color: #0073e6;
            }}
            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Bienvenue sur le Gym API</h1>
            <p>Votre solution complète pour la gestion d'adhérents et des entraînements cardiovasculaires !</p>
        </div>
        <div class="container">
            <h2>Statistiques du tableau de bord</h2>
            <table>
                <thead>
                    <tr>
                        <th>Total des adhérents</th>
                        <th>Moyenne des calories brûlées</th>
                        <th>Calories brûlées (min)</th>
                        <th>Calories brûlées (max)</th>
                        <th>Médiane du BMI</th>
                        <th>Parité</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{total_members}</td>
                        <td>{avg_calories:.2f}</td>
                        <td>{min_calories:.2f}</td>
                        <td>{max_calories:.2f}</td>
                        <td>{median_bmi:.2f}</td>
                        <td>{gender_distribution}</td>
                    </tr>
                </tbody>
            </table>
            <h2>Ressources disponibles</h2>
            <ul>
                <li><a href="/docs" target="_blank">Documentation Swagger</a> - Explorez et testez l'API.</li>
                <li><a href="/redoc" target="_blank">Documentation ReDoc</a> - Documentation détaillée et stylée.</li>
                <li><a href="/dashboard" target="_blank">Tableau de bord interactif</a> - Visualisez les données sous forme de graphiques interactifs.</li>
                <li><a href="/login" target="_blank">Page de connexion admin</a> - Accédez à l'interface admin.</li>
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
    # Charger les statistiques depuis le CSV
    data = load_csv()
    if data is None:
        return HTMLResponse(content="<h1>Erreur : Fichier CSV introuvable</h1>")
    
    # Calculs des statistiques
    total_members = data.shape[0]
    avg_calories = data["Calories_Burned"].mean()
    min_calories = data["Calories_Burned"].min()
    max_calories = data["Calories_Burned"].max()
    median_bmi = data["BMI"].median()
    gender_counts = data["Gender"].value_counts()
    gender_distribution = ", ".join([f"{k}: {v}" for k, v in gender_counts.items()])

    # Retourner la page HTML avec les données insérées
    return HTMLResponse(content=html_content.format(
        total_members=total_members,
        avg_calories=avg_calories,
        min_calories=min_calories,
        max_calories=max_calories,
        median_bmi=median_bmi,
        gender_distribution=gender_distribution
    ))
   
   
   
   
   
   

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    data = load_csv()
    if data is None:
        return HTMLResponse(content="<h1>Erreur : Fichier CSV introuvable</h1>")

    # 1. Histogramme des fréquences d'entraînement
    fig1 = px.histogram(
        data,
        x="Workout_Frequency (days/week)",
        title="Répartition des fréquences d'entraînement",
        labels={"x": "Nombre de jours d'entraînement par semaine"},
        color_discrete_sequence=["#0073e6"]
    )
    fig1.update_layout(template="plotly_white")

    # 2. Histogramme des calories brûlées
    fig2 = px.histogram(
        data,
        x="Calories_Burned",
        nbins=20,
        title="Répartition des calories brûlées",
        labels={"x": "Calories brûlées"},
        color_discrete_sequence=["#28a745"]
    )
    fig2.update_layout(template="plotly_white")

    # 3. Camembert des types d'entraînement
    fig3 = px.pie(
        data,
        names="Workout_Type",
        title="Répartition des types d'entraînement",
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    # 4. Boxplot du BMI par type d'entraînement
    fig4 = px.box(
        data,
        x="Workout_Type",
        y="BMI",
        title="Dispersion du BMI par type d'entraînement",
        color="Workout_Type",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig4.update_layout(template="plotly_white")

    # Convertir les graphiques en HTML
    graph1_html = pio.to_html(fig1, full_html=False)
    graph2_html = pio.to_html(fig2, full_html=False)
    graph3_html = pio.to_html(fig3, full_html=False)
    graph4_html = pio.to_html(fig4, full_html=False)

    # Retourner une page HTML contenant tous les graphiques
    return HTMLResponse(content=f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gym API Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f9f9f9;
                color: #333;
            }}
            h1 {{
                text-align: center;
                color: #0073e6;
            }}
            .chart-container {{
                margin: 20px 0;
                padding: 20px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
        </style>
    </head>
    <body>
        <h1>Gym API Dashboard</h1>
        <div class="chart-container">
            <h2>Répartition des fréquences d'entraînement</h2>
            {graph1_html}
        </div>
        <div class="chart-container">
            <h2>Répartition des calories brûlées</h2>
            {graph2_html}
        </div>
        <div class="chart-container">
            <h2>Répartition des types d'entraînement</h2>
            {graph3_html}
        </div>
        <div class="chart-container">
            <h2>Dispersion du BMI par type d'entraînement</h2>
            {graph4_html}
        </div>
    </body>
    </html>
    """)
    
    
@app.get("/admin", response_class=HTMLResponse)
def admin_interface():
    with open("frontend/admin.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
    
@app.get("/login", response_class=HTMLResponse)
def login_page():
    with open("frontend/login.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
