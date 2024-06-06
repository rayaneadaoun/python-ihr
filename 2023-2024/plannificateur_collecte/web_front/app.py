from flask import Flask, request, jsonify, render_template
import main
import agenda

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    time_slots = data.get('timeSlots')

    person_name = f"{first_name} {last_name}"
    
    # Convertir les créneaux horaires en tuples d'heures
    availability = []
    for slot in time_slots:
        start, end = slot.split('h-')
        end = end.rstrip('h')
        availability.append((int(start), int(end)))

    # Affichage pour vérification
    print(f"Nom: {person_name}")
    print(f"Disponibilités: {availability}")
    samedi={}
    samedi[first_name]=availability
    
    test=main.creneau(samedi)

    agenda.creer_agenda(test)

    return jsonify({"status": "success", "person_name": person_name, "availability": availability})

if __name__ == '__main__':
    app.run(debug=True)
