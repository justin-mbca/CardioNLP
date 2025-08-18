
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.heart_score import calculate_heart_score
from utils.translator import translate_text

st.title("CardioNLP Risk Assistant")

age = st.slider("Age", 18, 90)
ecg = st.selectbox("ECG", ["normal", "abnormal"])
troponin = st.number_input("Troponin Level")
history = st.selectbox("Chest Pain History", ["none", "atypical", "typical"])
risk_factors = st.multiselect("Risk Factors", ["diabetes", "smoking", "hypertension"])

score = calculate_heart_score(age, ecg, troponin, history, risk_factors)
st.write(f"HEART Score: {score}")

summary = f"Patient has HEART score of {score} with {', '.join(risk_factors)}."
st.write("English Summary:", summary)
st.write("Chinese Translation:", translate_text(summary))

