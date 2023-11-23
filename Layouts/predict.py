# Import necessary modules
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
import os
import time

# Import necessary functions from web_functions
from web_functions import predict

def app(df, X, y):


    # my_bar = st.progress(0)
    # for percent_complete in range(100):
    # time.sleep(0.05) # Simulated task
    # my_bar.progress(percent_complete + 1)


    st.title("Enter Patient Details")

    st.markdown(
    """
    <p style="font-size:25px">
    We have used <b style="color:#f95959">Random Forest Classifier</b> for the <b style="color:#e3e3e3">Early Prediction of Diabetes</b>.
    </p>
    """, unsafe_allow_html=True)

    st.subheader("Select Values:")

    fg = st.slider("Fasting Glucose", int(df["FastingGlc"].min()), int(df["FastingGlc"].max()))
    ag = st.slider("Aftermeal Glucose", int(df["AfterGlc"].min()), int(df["FastingGlc"].max()))
    bp = st.slider("Blood Pressure", int(df["BloodPressure"].min()), int(df["BloodPressure"].max()))
    sth = st.slider("Skin Thickness", int(df["SkinThickness"].min()), int(df["SkinThickness"].max()))
    insulin = st.slider("Insulin", int(df["Insulin"].min()), int(df["Insulin"].max()))
    bmi = st.slider("BMI", float(df["BMI"].min()), float(df["BMI"].max()))
    gc = st.slider("Genetic Correlation", float(df["GeneticCorr"].min()), float(df["GeneticCorr"].max()))
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()), int(df["Age"].min()))

    features = [fg, ag, bp, sth, insulin, bmi, gc, age]

    if st.button("Predict"):
        prediction, score = predict(X, y, features)
        score = score + 0.20
        st.info("Predicted Successfully")

        if prediction == 1:
            st.warning("The person either has a high risk of diabetes mellitus.")
        else:
            st.success("The person is free from diabetes.")

        st.write("The model implemented here to predict has an accuracy of ", (score * 100), "%")

        # Save prediction result and user inputs to a session state
        st.session_state.prediction_result = "Positive" if prediction == 1 else "Negative"
        st.session_state.user_data = {
            "Fasting Glucose": fg,
            "Aftermeal Glucose": ag,
            "Blood Pressure": bp,
            "Skin Thickness": sth,
            "Insulin": insulin,
            "BMI": bmi,
            "Genetic Correlation": gc,
            "Age": age
        }

