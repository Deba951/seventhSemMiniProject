# Importing the necessary Python modules.
import streamlit as st
from web_functions import load_data

# Import pages
from Layouts import home, data, predict, visualise, about, report

# Configure the app
st.set_page_config(
    page_title = 'Diabetes?',
    page_icon = '🩺',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Layouts = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Report": report,  # Added the "Report" page
    "Visualisation": visualise,
    "About us": about
}

# Create a sidebar and add title
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Layouts.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app function of the selected page to run
if page in ["Prediction", "Visualisation"]:
    Layouts[page].app(df, X, y)

elif page == "Report":  # Added a condition for the "Report" page
    # Example data, replace with actual user input and prediction result
    patient_name = st.text_input("Enter Patient's Name:")
    doctor_name = st.text_input("Enter Referred Doctor's Name:")
    pathology_name = st.text_input("Enter Pathology Name:")

    st.write("Enter User Data:")
    user_data = {}
    user_data["Fasting Glucose"] = st.slider("Fasting Glucose", 0, 200)
    user_data["Aftermeal Glucose"] = st.slider("Aftermeal Glucose", 0, 200)
    user_data["Blood Pressure"] = st.slider("Blood Pressure", 0, 200)
    user_data["Skin Thickness"] = st.slider("Skin Thickness", 0, 200)
    user_data["Insulin"] = st.slider("Insulin", 0, 200)
    user_data["BMI"] = st.slider("BMI", 0.0, 50.0)
    user_data["Genetic Correlation"] = st.slider("Genetic Correlation", 0.0, 1.0)
    user_data["Age"] = st.slider("Age", 0, 120)
    # Add other user input fields as needed

    # Get prediction result from user
    prediction_result = st.radio("Prediction Result:", ["Positive", "Negative"])

    # Output file path
    output_path = "diabetes_report.pdf"

    Layouts[page].generate_report(patient_name, doctor_name, pathology_name, user_data, prediction_result, output_path)
    st.write(f"Report generated and saved as {output_path}")

elif page == "Data Info":
    Layouts[page].app(df)
else:
    Layouts[page].app()