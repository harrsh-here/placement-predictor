# Student Placement Predictor 🎓

A professional Machine Learning web application that predicts the likelihood of student placement based on academic performance (CGPA) and cognitive ability (IQ). This project demonstrates a complete ML lifecycle—from data preprocessing to cloud deployment.

---

## 🔗 Live Application
**View the live project here:** [https://placement-predictor-ln7q.onrender.com](https://placement-predictor-ln7q.onrender.com)

---

## 🚀 Project Overview
This is my first Machine Learning project, designed to solve a binary classification problem. While many basic models fail when moving from a local notebook to a web server, this application includes robust logic to handle real-world user inputs.

### Core Features:
* **Predictive Engine:** Uses a supervised learning model (Logistic Regression) to classify placement outcomes.
* **Input Scaling:** Implements a `StandardScaler` pipeline. This ensures that the IQ (large range) doesn't overshadow the CGPA (small range), maintaining model accuracy.
* **Flask Integration:** A RESTful API backend that processes JSON/Form data and returns real-time predictions.
* **Web Interface:** A minimalist, user-friendly frontend for seamless interaction.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **ML Libraries:** Scikit-Learn, NumPy, Pandas
* **Web Framework:** Flask
* **WSGI Server:** Gunicorn (for production-grade hosting)
* **Deployment:** Render (Cloud Platform)

## 📊 How it Works
1. **Data Loading:** The model was trained on numerical data representing student profiles.
2. **Preprocessing:** Features are normalized to a standard scale.
3. **Inference:** When a user enters data via the web form, the app:
   - Captures the inputs as `float` and `int`.
   - Applies the saved `scaler.pkl` transformation.
   - Passes the scaled data to `model.pkl`.
   - Returns a "Placed" or "Not Placed" result to the UI.

## ⚙️ Local Setup
If you want to run this project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/harrsh-here/placement-predictor.git](https://github.com/harrsh-here/placement-predictor.git)
   cd placement-predictor
