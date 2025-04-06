from flask import Flask, request
from flask_cors import CORS
import numpy as np
import pickle
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for communication with React

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    values = [float(data[key]) for key in data]
    prediction = model.predict([np.array(values)])
    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    return json.dumps({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
