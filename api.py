import datetime
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

capsules = {
    "capsule1": {
        'value': "Hello, World!",
        'created_at': "2021-01-01T00:00:00Z"
    },
    "capsule2": {
        'value': "Hello, Moon!",
        'created_at': "2021-01-02T00:00:00Z",
        'password': "password"
    }
}

@app.route("/create/<string:name>", methods=["POST"])
def create_capsule(name: str):
    capsule = {
        'name': name,
        'value': request.form.get('value'),
        'created_at': datetime.datetime.now()
    }
    if 'password' in request.form:
        capsule['password'] = request.form.get('password')
        
    capsules[name] = capsule

    return '', 201

@app.route("/get/<string:name>", methods=["GET"])
def get_capsule(name: str):

    if name not in capsules:
        return jsonify({'error': 'Capsule not found'}), 404
     
    if 'password' in capsules[name] and request.form.get('password') != capsules[name]['password']:
        return jsonify({'error': 'Access restricted'}), 403

    return jsonify({ 'value': capsules[name]['value'] })

@app.route('/remove_password/<string:name>', methods=["PUT"])
def remove_password(name: str):
    if name not in capsules:
        return jsonify({'error': 'Capsule not found'}), 404
    
    if capsules[name]['password'] is None:
        return jsonify({'error': 'Password not set'}), 400
    
    if(request.form.get('password') != capsules[name]['password']):
        return jsonify({'error': 'Incorrect password'}), 403

    capsules[name]['password'] = None
    
    return '', 204

if __name__ == "__main__":
    app.run(port=5000, debug=True)
