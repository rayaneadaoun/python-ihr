import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random

def creer_agenda(disponibilites):
    # Appliquer un style de matplotlib
    plt.style.use('bmh')

    # Création d'une figure et d'un axe
    fig, ax = plt.subplots(figsize=(10, 8))

    # Extraction unique des personnes
    personnes = sorted(set(personne for personnes in disponibilites.values() for personne in personnes))

    # Génération de couleurs aléatoires pour chaque personne
    couleurs = {personne: (random.random(), random.random(), random.random()) for personne in personnes}

    # Itération sur les créneaux horaires pour dessiner chaque bloc de disponibilité
    x_positions = {personne: i * 10 for i, personne in enumerate(personnes)}  # Positions des barres pour chaque personne
    for (debut, fin), personnes_presentes in disponibilites.items():
        for personne in personnes_presentes:
            ax.broken_barh([(x_positions[personne], 9)], (debut, fin - debut), facecolors=couleurs[personne], edgecolor='black')

    # Personnalisation de l'axe
    ax.set_xlim(-5, len(personnes) * 10 + 5)
    ax.set_ylim(18, 9)  # Mettre 18 en haut et 9 en bas
    ax.set_yticks(range(9, 19))
    ax.set_yticklabels([f'{hour}:00' for hour in range(9, 19)])
    ax.set_ylabel('Heures')
    ax.set_xlabel('Personnes')
    ax.set_xticks([i * 10 + 4.5 for i in range(len(personnes))])
    ax.set_xticklabels(personnes)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Création d'une légende
    patches = [mpatches.Patch(color=couleurs[personne], label=personne) for personne in couleurs]
    ax.legend(handles=patches, loc='upper right')

    # Titre du graphique
    plt.title("Agenda des disponibilités")

    # Affichage du graphique
    plt.tight_layout()
    plt.show()

# Exemple d'utilisation




disponibilites = {
    (10, 11): ['Abdel', 'Baya'],
    (11, 12): ['Abdel', 'Baya'],
    (13, 14): ['Celia','Dalila'],
    (14, 15): ['Celia','Dalila','Emilie'],
    (15, 16): ['Abdel','Fatima'],
    (16, 17): ['Abdel','Hamid'],
    (17, 18): ['Abdel','Hamid']
}

# creer_agenda(disponibilites)
