import joblib
import pandas as pd

def load_model():
    model = joblib.load('models/churn_model.pkl')
    feature_names = joblib.load('models/feature_names.pkl')
    return model, feature_names

def make_prediction(input_data):
    model, feature_names = load_model()
    
    # Ensure input data is in the correct format
    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=feature_names, fill_value=0)
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]  # Probability of churn
    
    return prediction, probability