from flask import Flask , request, render_template

import pickle
import numpy as np


model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    cgpa = float(request.form['cgpa'])
    iq = float(request.form['iq'])
    prediction = model.predict([[cgpa, iq]]) 
    result = 'Placed' if prediction[0] == 1 else 'Not Placed'

    return render_template('index.html', prediction_text='Candidate is {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)
    