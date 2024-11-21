-- Création de la table des utilisateurs
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    age INT,
    gender VARCHAR(50),
    weight_kg FLOAT,
    height_m FLOAT,
    max_bpm INT,
    avg_bpm INT,
    resting_bpm INT,
    session_duration_hours FLOAT,
    calories_burned FLOAT,
    workout_type VARCHAR(100),
    fat_percentage FLOAT,
    water_intake_liters FLOAT,
    workout_frequency_days_week INT,
    experience_level VARCHAR(50),
    bmi FLOAT
);

-- Insertion de données initiales
INSERT INTO users (username, hashed_password, age, gender, weight_kg, height_m, max_bpm, avg_bpm, resting_bpm, session_duration_hours, calories_burned, workout_type, fat_percentage, water_intake_liters, workout_frequency_days_week, experience_level, bmi)
VALUES
('admin', '$2b$12$lkyU2LVMWURGqnH3AC3Mv.edRd.S96bg3YuaPPbfy.cC4g6kIEEZO', 30, 'Male', 80, 1.80, 180, 90, 70, 1.5, 500, 'Cardio', 15, 2, 3, 'Advanced', 24.7);