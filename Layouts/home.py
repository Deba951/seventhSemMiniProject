# Import necessary modules
import streamlit as st
import json
from streamlit_lottie import st_lottie
def app():
    # Add title to the home page
    st.title("Welcome to our Diabetes Prediction System")

    # Load the Lottie animation JSON file
    with open('Assets/medicalBanner.json', 'r') as lottie_file:
        lottie_data = json.load(lottie_file)

    # Display the Lottie animation at the end in a smaller size
    st_lottie(lottie_data, speed=1, reverse=False, loop=True, quality="low", width="100%", height="100%")

    # Add image to the home page
    # st.image("./Assets/images.jpeg")

    # Add brief describtion of your web app
    st.write(
        """
        <p style="text-align: justify;">Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. It's a metabolic disorder characterized by elevated blood sugar levels. There isn't a cure yet for diabetes, but lifestyle modifications such as losing weight, eating a balanced diet, and being physically active can significantly reduce the impact of diabetes and improve the quality of life.</p>
        
        <p style="text-align: justify;">Our web app employs machine learning techniques, specifically the Random Forest Classifier, to predict whether a person has diabetes or is at risk of developing diabetes in the future. By analyzing a set of essential health features, our tool provides valuable insights and early detection, enabling users to take proactive steps towards managing their health.</p>
        
        <p style="text-align: justify;">Empowering individuals with the knowledge and tools to make informed decisions about their health is at the core of our mission. Explore the features and predictions offered by our Diabetes Prediction Web App to take control of your well-being and make healthier choices.</p>
        """, 
    unsafe_allow_html=True)
