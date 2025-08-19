
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.heart_score import calculate_heart_score
from utils.translator import translate_text

st.title("CardioNLP Risk Assistant")

# Add language selector

lang = st.selectbox("Select language 选择语言", ["English 英文", "Chinese 中文", "Both 两者"])

# Set bilingual labels for all fields
if lang.startswith("English"):
	age_label = "Age"
	ecg_label = "ECG"
	ecg_options = ["normal", "abnormal"]
	troponin_label = "Troponin Level"
	history_label = "Chest Pain History"
	history_options = ["none", "atypical", "typical"]
	risk_label = "Risk Factors"
	risk_options = ["diabetes", "smoking", "hypertension"]
elif lang.startswith("Chinese"):
	age_label = "年龄"
	ecg_label = "心电图"
	ecg_options = ["正常", "异常"]
	troponin_label = "肌钙蛋白水平"
	history_label = "胸痛史"
	history_options = ["无", "非典型", "典型"]
	risk_label = "危险因素"
	risk_options = ["糖尿病", "吸烟", "高血压"]
else:
	age_label = "Age 年龄"
	ecg_label = "ECG 心电图"
	ecg_options = ["normal 正常", "abnormal 异常"]
	troponin_label = "Troponin Level 肌钙蛋白水平"
	history_label = "Chest Pain History 胸痛史"
	history_options = ["none 无", "atypical 非典型", "typical 典型"]
	risk_label = "Risk Factors 危险因素"
	risk_options = ["diabetes 糖尿病", "smoking 吸烟", "hypertension 高血压"]

age = st.slider(age_label, 18, 90)
ecg = st.selectbox(ecg_label, ecg_options)
troponin = st.number_input(troponin_label)
history = st.selectbox(history_label, history_options)
risk_factors = st.multiselect(risk_label, risk_options)

score = calculate_heart_score(age, ecg, troponin, history, risk_factors)
st.write(f"HEART Score: {score}")

summary = f"Patient has HEART score of {score} with {', '.join(risk_factors)}."

if lang.startswith("English"):
	st.write("Summary:", summary)
elif lang.startswith("Chinese"):
	st.write("摘要:", translate_text(summary))
else:
	st.write("English Summary:", summary)
	st.write("Chinese Translation:", translate_text(summary))

