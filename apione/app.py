#!/bin/python

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

inventory = [
    {
        'id': 1,
        'name': u'Longsword',
        'description': u'A simple, iron sword measuring 3 feet in length.',
        'weight': 4.0
    },
    {
        'id': 2,
        'name': u'Chainmail',
        'description': u'Common armor for those who like mobility.',
        'weight': 12.0
    }
]

@app.route('/')
def index():
    return "Hello, Cleveland!\n"

@app.route('/api/v1/inventory', methods=['GET'])
def get_inventory():
    return jsonify({'inventory': inventory})

@app.route('/api/v1/inventory/<int:inv_id>', methods=['GET'])
def get_inv(inv_id):
    inv = [inv for inv in inventory if inv['id'] == inv_id]
    if len(inv) == 0:
        abort(404)
    return jsonify({'inv': inv[0]})

@app.route('/api/v1/inventory', methods=['POST'])
def create_inv():
    if not request.json or not 'name' in request.json:
        abort(400)
    inv = {
        'id': inventory[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', ""),
        'weight': request.json.get('weight', "")
    }
    inventory.append(inv)
    return jsonify({'inv': inv}), 201

@app.route('/api/v1/inventory/<int:inv_id>', methods=['PUT'])
def update_inv(inv_id):
    inv = [inv for inv in inventory if inv['id'] == inv_id]
    if len(inv) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) != unicode:
        abort(400)
    inv[0]['name'] = request.json.get('name', inv[0]['name'])
    inv[0]['description'] = request.json.get('description', inv[0]['description'])
    inv[0]['weight'] = request.json.get('weight', inv[0]['weight'])
    return jsonify({'inv': inv[0]})

@app.route('/api/v1/inventory/<int:inv_id>', methods=['DELETE'])
def delete_item(inv_id):
    inv = [inv for inv in inventory if inv['id'] == inv_id]
    if len(inv) == 0:
        abort(404)
    inventory.remove(inv[0])
    return jsonify({'result': True})

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request.  You omitted a required field or entered data the server could not parse.'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
