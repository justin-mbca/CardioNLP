def calculate_heart_score(age, ecg, troponin, history, risk_factors):
    score = 0
    score += 1 if age > 65 else 0
    score += 1 if ecg == 'abnormal' else 0
    score += 1 if troponin > 0.04 else 0
    score += 1 if history == 'typical' else 0
    score += len(risk_factors)
    return score

