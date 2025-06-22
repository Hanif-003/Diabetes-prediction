import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline (model + scaler)
model = joblib.load("model.pk1")

st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient's details below to predict the likelihood of diabetes:")

# User Inputs
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=122, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=18, max_value=90, value=30)

# Button to predict
if st.button("🔍 Predict Diabetes"):
    # Input as DataFrame
    input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness,
                                 insulin, bmi, dpf, age]],
                               columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                                        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

    # Predict using pipeline (which includes StandardScaler)
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ The patient is **likely** to have diabetes.")
    else:
        st.success("✅ The patient is **unlikely** to have diabetes.")
else:
    st.info("🧾 Please enter all the values and click the button to predict.")
