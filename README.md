# 🩺 CardioNLP – Bilingual AI Assistant for Cardiovascular Risk

## 🌍 Why This Matters

Cardiovascular disease is the leading cause of death globally. Early risk detection can save lives — but many patients are underserved due to language barriers, fragmented data, and opaque algorithms.

**CardioNLP** addresses these challenges by:
- Integrating structured and unstructured data for richer insights
- Supporting bilingual output to improve accessibility
- Using interpretable models clinicians can trust
- Simulating federated learning to protect patient privacy

This project reflects Sanofi’s mission to use AI for good, promote health equity, and transform healthcare through ethical innovation.

## 🚀 Features
* XGBoost risk model with SHAP explainability
* BioBERT-powered NLP pipeline
* HEART score override logic
* Bilingual output (English/Chinese)
* Fairness analysis across ethnic groups (now robust to single-class groups in ROC AUC)
* Streamlit app for interactive use

## 📦 How to Run
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## 📊 Notebooks

Jupyter notebooks for data exploration, model training, NLP, and fairness/bias analysis are in `notebooks/`.

### Fairness Analysis (04_bias_fairness_analysis.ipynb)

This notebook evaluates model performance (ROC AUC) across ethnic groups. If a group contains only one class in the target variable, the code now skips AUC calculation for that group and prints a message, avoiding warnings and undefined metrics.

**Warning explained:**
> Only one class is present in y_true. ROC AUC score is not defined in that case.

**How we handle it:**
The code checks for this and skips AUC calculation for such groups, ensuring robust and interpretable fairness analysis.

