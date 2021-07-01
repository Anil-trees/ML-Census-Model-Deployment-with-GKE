from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import LabelBinarizer
from tensorflow.python.lib.io import file_io
from flask import Flask, request, jsonify
from functools import wraps
import joblib
import json
import jwt
import datetime
import yaml

app = Flask(__name__)

@app.route('/')
def print_hello():
    return 'hello world!'

def token_required(f):
    @wraps(f)
    def authenticate():
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, secret_key)
        except:
            return jsonify({'error message': 'Token is invalid!'}), 403
        return f()
    return authenticate

@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.username.lower() in users.keys()\
        and auth.password==users[auth.username]:
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=720)}, secret_key)
        return jsonify({'token': token.decode('utf-8')})
    return jsonify({'error message': 'your password or username is invalid'}), 401

@app.route('/prediction', methods=['POST', 'GET'])
@token_required
def predict_output():
    input_request = request.get_json()
    outputs = ml_model.predict(input_request['inputs']).tolist()
    outputs = [prediction_decoding[output] for output in outputs]
    return jsonify({'predictions': outputs})

if __name__ == '__main__':

    with open('/configuration/config.yaml', 'r') as config_file:
        cfg = yaml.load(config_file, Loader=yaml.FullLoader)

    with file_io.FileIO(cfg['model_path'], 'rb') as infile:
        ml_model = joblib.load(infile)
    
    with file_io.FileIO(cfg['users'], 'r') as infile:
        users = json.load(infile)
    
    with file_io.FileIO(cfg['prediction_decoding'], 'r') as infile:
        prediction_decoding = json.load(infile)
        prediction_decoding = {int(key): value for key, value in prediction_decoding.items()}
    
    with file_io.FileIO(cfg['secret'], 'r') as infile:
        secret_key = infile.read()

    app.run(host='0.0.0.0', port=5090, debug=False)
