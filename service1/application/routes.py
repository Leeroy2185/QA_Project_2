from flask import render_template, url_for, Response
from application import app, db
from application.models import Creature
import requests
import random

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    CreatureData = Creature.query.all()
    return render_template('home.html', title = 'Home', Creatures=CreatureData)



@app.route('/generateView', methods=['GET'])
def generate_view():
    return render_template('generate.html', title= 'Creature Name')

@app.route('/generate', methods=['GET'])
def generate_creature():
    Species = requests.get('http://service2:5001/get/species')
    Size = requests.get('http://service3:5002/get/size')
    Features = requests.post('http://service4:5003/get/features', data=Species)

    db_data = Creature(Species=Species.text, Size=Size.text, Features=Features.text)
    db.session.add(db_data)
    db.session.commit()
    Creature_record=db_data.query.all()

    return render_template('generate.html', title= 'Creature Name')