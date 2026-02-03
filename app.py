from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get data from the form
    # iq is an int, cgpa is a float
    iq = int(request.form['iq'])
    cgpa = float(request.form['cgpa'])
    
    # 2. Prepare data for model (reshape to 2D array)
    raw_data = np.array([[cgpa, iq]])
    
    raw_data = np.array([[cgpa, iq]])
    scaled_data = scaler.transform(raw_data)
    # 3. Get prediction
    prediction = model.predict(scaled_data)
    
    # 4. Format the result for the user
    output = "Hojayegi Placement" if prediction[0] == 1 else "Nahi hogi"
    
    return render_template('index.html', prediction_text=f'Student Status: {output}')

if __name__ == "__main__":
    app.run(debug=True)