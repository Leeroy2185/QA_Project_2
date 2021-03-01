from flask import request, Response
import requests
from application import app
import random


#generates a size
@app.route('/get/size',methods=['GET'])
def get_size():
    sizes = ['Tiny','Small','Average','Large','Humungous','Fat','Thin']
    size = sizes[random.randrange(0,15)]
    return Response(size,mimetype='text/plain')