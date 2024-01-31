# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Liste des articles (contient des dictionnaires avec le nom et le prix de chaque article)
#     # articles = [
#     #     {'name': 'Article 1', 'price': '$10'},
#     #     {'name': 'Article 2', 'price': '$20'},
#     #     {'name': 'Article 3', 'price': '$30'},
#     #     {'name': 'Article 4', 'price': '$40'}
#     # ]
#     articles= [ ["test" , 3],["test2",4] ]
#     return render_template('index.html', articles=articles)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

IMAGE_DIRECTORY = os.path.join(os.getcwd(), 'images')


def load_file(nom_fichier):
    articles = []
    with open(nom_fichier, 'r') as file:
        for line in file:
            article = line.strip().split(',')
            articles.append([article[0], int(article[1]), article[2], article[3], article[4]])  # Convertir le prix en int
    return articles

articles = load_file('static/article2.txt')

def load_images():
    return os.listdir(IMAGE_DIRECTORY)

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/add_article', methods=['POST'])
def add_article():
    marque = request.form['marque']
    prix = int(request.form['prix'])
    etat= request.form['etat']
    image= request.form['image']
    cat= request.form['cat']

    articles.append([marque, prix, etat, image, cat])
    return redirect(url_for('index'))

@app.route('/filtrer_prix', methods=['POST'])
def filtrer_prix():
    prix_min = int(request.form['prix_min'])
    prix_max = int(request.form['prix_max'])
    # Filtrez les articles en fonction du prix
    res=[]
    #################################
    # Ajouter le code python pour Filtrer les articles en fonction du prix
    ###################################
    return render_template('index.html', articles=res)

@app.route('/filtrer_cat', methods=['POST'])
def filtrer_cat():
    categorie = request.form['cat']
    # Filtrez les articles en fonction du prix
    res=[]
    ################################
    # Ajouter le code python pour filtrer par categorie
    ################################
    return render_template('index.html', articles=res)

@app.route('/clear_articles', methods=['POST'])
def clear_articles():
    articles.clear()
    return redirect(url_for('index'))

@app.route('/add')
def add():
    filenames=load_images()
    return render_template('form.html', filenames=filenames)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(IMAGE_DIRECTORY, filename)

if __name__ == '__main__':
    app.run(debug=True)
