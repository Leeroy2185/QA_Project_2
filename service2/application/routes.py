from flask import request,Response
import requests
from application import app
import random


#generates a species name
@app.route('/get/species',methods=['GET'])
def get_species():
    species = ['Wookie','Jawa','Gamorrean']
    species = species[random.randrange(0,3)]
    return Response(species,mimetype='text/plain')