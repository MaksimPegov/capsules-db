from flask import Flask, jsonify, request
from flask_cors import CORS
import capsule_service

app = Flask(__name__)
CORS(app)

@app.route("/create/<string:name>", methods=["POST"])
def create_capsule(name: str):
    # capsule = {
    #     'name': name,
    #     'value': request.form.get('value'),
    #     'created_at': datetime.datetime.now()
    # }
    # if 'password' in request.form:
    #     capsule['password'] = request.form.get('password')
    body = request.json

    result = capsule_service.create_capsule(name, body.get('value'), body.get('password'))

    if result != 200:
        return {'error': 'Something went wrong'}, 500
    
    return '', 201


@app.route("/get/<string:name>", methods=["GET"])
def get_capsule(name: str):

    # if name not in capsules:
    #     return jsonify({'error': 'Capsule not found'}), 404
     
    # if 'password' in capsules[name] and request.form.get('password') != capsules[name]['password']:
    #     return jsonify({'error': 'Access restricted'}), 403

    result = capsule_service.get_capsule(name, request.form.get('password'))

    # return jsonify({ 'value': capsules[name]['value'] })
    return jsonify(result)

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
