from flask import request, Response
import requests
from application import app
import random


@app.route('/get/features', methods=['GET', 'POST'])
def get_features():
    species= request.data.decode('utf-8')
    if species == 'Wookie':
        features = ['Needs a wash.','Has a vicious temper.','Kind and friendly']
        return Response(features[random.randrange(0,3)],mimetype='text/plain')

    elif species == 'Jawa':
        features = ['Will steal all your tech.','Needs a new coat.','Smells terrible.']
        return Response(features[random.randrange(0,3)],mimetype='text/plain')

    elif species == 'Gamorrean':
        features = ['Eats like a pig','is a great guard.','Eats too much.']
        return Response(features[random.randrange(0,3)],mimetype='text/plain')

    else:
        return 'This is not a expected species' 