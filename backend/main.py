import flask
import csv
import random
from flask import request, jsonify
import sys
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/resources/cars/all', methods=['GET'])
def api_all():
    with open("cars.txt") as textfile:
        # reader = csv.reader(textfile)

        return str(textfile.read())
    # with open("cars.txt", encoding="utf-8") as f:
        # data = json.load(f)

    # return str(data)

@app.route('/api/v1/resources/cars/map', methods=['GET'])
def api_array():
    map = []
    with open("map.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            map.append(row)
    return str(map)


app.run(host='0.0.0.0')

