from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Configuration du jeu
plateau = [random.choice([-10, 10, -20, 20, 30, -30, 40, -40]) for _ in range(20)]  # 20 cases aléatoires
player_position = 0
player_money = 100  # Départ avec 100 unités d'argent

@app.route('/')
def index():
    return render_template('board.html', plateau=plateau, position=player_position, money=player_money)

@app.route('/move', methods=['POST'])
def move():
    global player_position, player_money

    # Déplacer de n cases (tirage aléatoire entre 1 et 6)
    n = random.randint(1, 20)
     
    player_position = (player_position + n) % len(plateau)  # Boucler sur le plateau
    player_money += plateau[player_position]  # Gagner ou perdre de l'argent selon la case

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
