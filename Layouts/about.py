import base64
import streamlit as st
from PIL import Image
import time
import json
import requests
from streamlit_lottie import st_lottie

def app():

    with st.spinner():
        # Add content that requires loading
        time.sleep(5)  # Simulated loading time
        st.success('Loading complete!')





    # st.title('👋 Who Are We?')

    # st.image('./Assets/images.jpeg', use_column_width=True)

    # Load the Lottie animation JSON file
    with open('Assets/Hello.json', 'r') as lottie_file:
        lottie_data = json.load(lottie_file)

    # Display the Lottie animation at the end in a smaller size
    st_lottie(lottie_data, speed=1, reverse=False, loop=True, quality="low", width="100%", height=200)

    team_members = [
        {
            'name': 'Debarghya Chakravarty',
            'description': 'Being an Android developer, AI enthuciast, Competitive Coder and a problem solver, I am a passionate techie who is constantly Upskilling, Innovating and Exploring with Code',
            'linkedin': 'https://www.linkedin.com/in/debarghya-chakravarty-5a2563238/',
            'github': 'https://github.com/Deba951'
        },
        {
            'name': 'Raktim Bar',
            'description': 'I am a passionate engineer, currently diving deep into the world of computer science engineering, exploring algorithms, coding, and the limitless possibilities of technology.',
            'linkedin': 'https://www.linkedin.com/in/raktim-bar',
            'github': 'https://github.com/raktimbar100'
        },
        {
            'name': 'Supriyo Bose',
            'description': 'I am a full-stack software engineer and writer. I love programming, reading, writing and speaking. As a software engineer, I enjoy using my obsessive attention to detail, my unequivocal love for making things that change the world.',
            'linkedin': 'https://www.linkedin.com/in/supriyo-bose-116b8b203/',
            'github': 'https://github.com/bosesupriyo'
        },
        {
            'name': 'Swathik Majumder',
            'description': 'I am a Enthusiastic and skilled CSE engineer with a passion for software development and problem-solving. Expertise in Java, Python, and C++. Proven ability to design and develop. Seeking to utilize my skills in a challenging and rewarding environment.',
            'linkedin': 'https://www.linkedin.com/in/swathik-majumder-038080210/',
            'github': 'https://github.com/Swathik2000'
        },
        {
            'name': 'Tunir Chakrabarty',
            'description': 'Final Year Student at AOT',
            'linkedin': 'https://www.linkedin.com/in/tunir-chakraborty-9342481aa?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app',
            'github': 'https://github.com/Tanzo11'
        }
    ]


    st.subheader(f"Connect with us!!!")
    for member in team_members:
        # st.subheader(f"Connect with {member['name']}")

        with st.expander(f"{member['name']}"):
            st.markdown(member['description'])
            st.markdown(f"LinkedIn: [{member['name']}]({member['linkedin']})")
            st.markdown(f"GitHub: {member['github']}")

    # Load the Lottie animation JSON file
    with open('Assets/ThankYou.json', 'r') as lottie_file:
        lottie_data = json.load(lottie_file)

    # Display the Lottie animation at the end in a smaller size
    st_lottie(lottie_data, speed=1, reverse=False, loop=True, quality="low", width="100%", height="50%")



if __name__ == '__main__':
    app()

