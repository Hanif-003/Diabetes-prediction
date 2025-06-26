#  Diabetes Prediction App

This project is a machine learning web application that predicts the likelihood of diabetes based on user input health parameters. Built using Python, Streamlit, and scikit-learn, it allows users to interactively input values and get real-time predictions.

## 🔗 Live Demo

[👉 Click here to try the DIABETES Prediction App](https://hanif-003-diabetes-prediction-app-k2n0sp.streamlit.app/)


##  Features

- User-friendly web interface with Streamlit
- Trained ML model (e.g., Logistic Regression )
- Predicts based on:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age


##  Files in This Repository

- `app.py` – Streamlit app source code
- `diabetes_model.pkl` – Pre-trained machine learning model
- `requirements.txt` – List of dependencies
- `README.md` – Project documentation

## 💡 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

