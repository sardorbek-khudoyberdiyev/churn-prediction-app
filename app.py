import streamlit as st

from src.predict import make_prediction


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction App")

st.write(
    "This app predicts whether a customer is likely to churn based on account and billing information."
)

st.subheader("Customer Information")

tenure = st.number_input(
    "Tenure in months",
    min_value=0,
    max_value=100,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=1000.0
)

senior_citizen = st.selectbox(
    "Senior Citizen",
    options=["No", "Yes"]
)

contract = st.selectbox(
    "Contract Type",
    options=["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    options=["DSL", "Fiber optic", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    options=[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    options=["No", "Yes"]
)

tech_support = st.selectbox(
    "Tech Support",
    options=["No", "Yes", "No internet service"]
)

online_security = st.selectbox(
    "Online Security",
    options=["No", "Yes", "No internet service"]
)


if st.button("Predict Churn"):
    input_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,

        f"Contract_{contract}": 1,
        f"InternetService_{internet_service}": 1,
        f"PaymentMethod_{payment_method}": 1,
        f"PaperlessBilling_{paperless_billing}": 1,
        f"TechSupport_{tech_support}": 1,
        f"OnlineSecurity_{online_security}": 1,
    }

    prediction, probability = make_prediction(input_data)

    st.subheader("Prediction Result")

    st.write(f"Churn probability: **{probability:.2%}**")

    st.progress(probability)

    if probability >= 0.70:
        risk_level = "High Risk"
        st.error("Prediction: Customer is likely to churn")
        st.error(f"Risk Level: {risk_level}")
    elif probability >= 0.40:
        risk_level = "Medium Risk"
        st.warning("Prediction: Customer may churn")
        st.warning(f"Risk Level: {risk_level}")
    else:
        risk_level = "Low Risk"
        st.success("Prediction: Customer is not likely to churn")
        st.success(f"Risk Level: {risk_level}")