import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl") #loads a previously saved machine learning pipeline from the file "fraud_detection_pipeline.pkl" using joblib. This allows the application to use the trained model for making predictions on new data without needing to retrain it.   

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction details and use the predict button") #displays a markdown-formatted message in the Streamlit app, instructing the user to enter transaction details and use the predict button. This serves as a prompt to guide users on how to interact with the application for making fraud detection predictions.

st.divider() #adds a horizontal divider line in the Streamlit app to visually separate different sections of the user interface, improving readability and organization.

transaction_type = st.selectbox("Transaction Type", ["PAYMENT","TRANSFER","CASH_OUT", "DEPOSIT"]) #creates a dropdown select box in the Streamlit app for the user to choose the type of transaction, with options "PAYMENT", "TRANSFER", and "CASH_OUT". The selected value will be stored in the variable transaction_type for use in making predictions with the loaded model.
amount = st.number_input("Amount", min_value= 0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)" , min_value = 0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value = 0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value = 0.0, value = 0.0) 

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("The transaction can be fraudulent one .")
    else:
        st.success("The transaction looks like a non-fraudulent one.")

#python -m streamlit run fraud_detection.py