from flask import Flask, render_template, request

app = Flask(__name__)

def determine_winner(player1, player2):
    """Détermine le gagnant du jeu Pierre-Feuille-Ciseau"""
    if player1 == player2:
        return "Égalité !"
    
    if (player1 == "Pierre" and player2 == "Ciseau") or \
       (player1 == "Feuille" and player2 == "Pierre") or \
       (player1 == "Ciseau" and player2 == "Feuille"):
        return "Joueur 1 gagne !"
    else:
        return "Joueur 2 gagne !"

@app.route('/', methods=['GET', 'POST'])
def index():
    winner = None
    if request.method == 'POST':
        player1 = request.form.get('player1')
        player2 = request.form.get('player2')
        
        if player1 and player2:
            winner = determine_winner(player1, player2)
    
    return render_template('index.html', winner=winner)

if __name__ == '__main__':
    app.run(debug=True)
