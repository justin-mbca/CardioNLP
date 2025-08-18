import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(path):
    """Load dataset from CSV file."""
    return pd.read_csv(path)

def handle_missing(df):
    """Fill or drop missing values."""
    df = df.copy()
    # Example: fill numeric columns with median
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Example: fill categorical columns with mode
    categorical_cols = df.select_dtypes(include='object').columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

def encode_categoricals(df):
    """Encode categorical features using LabelEncoder."""
    df = df.copy()
    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    return df, label_encoders

def scale_features(df, exclude=[]):
    """Standardize numerical features."""
    df = df.copy()
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include='number').columns.difference(exclude)
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df, scaler

def preprocess_pipeline(path, target_col='cardio_risk'):
    """Full preprocessing pipeline."""
    df = load_data(path)
    df = handle_missing(df)
    df, encoders = encode_categoricals(df)
    df, scaler = scale_features(df, exclude=[target_col])
    return df, encoders, scaler

