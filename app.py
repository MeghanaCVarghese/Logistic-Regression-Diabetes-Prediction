import streamlit as st
import numpy as np
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🩺 Diabetes Prediction App")

# inputs
glucose = st.number_input("Glucose")
bmi = st.number_input("BMI")
age = st.number_input("Age")
bp = st.number_input("Blood Pressure")

# prediction
if st.button("Predict"):
    input_data = np.array([[glucose, bp, 0, 0, bmi, 0, 0, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")
