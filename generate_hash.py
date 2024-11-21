from passlib.context import CryptContext

# Initialiser le contexte de hachage
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Remplacez "testpassword" par le mot de passe que vous voulez hacher
plain_password = "adminpassword"

# Générez le mot de passe haché
hashed_password = pwd_context.hash(plain_password)

# Affichez le mot de passe haché
print(f"Mot de passe brut : {plain_password}")
print(f"Mot de passe haché : {hashed_password}")