import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json
from reume_page import resume
from experience_page import experience
#from upwork_page import feedbackRating
from project_page import projects
from contact_form import contact
from certifications_page import certifications
from skills_page import skills


 # Page setup
st.set_page_config(
    page_title="Mayur",
    page_icon="📋",
    layout="wide",
)


def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)
def aboutMe():
    col1, col2 = st.columns(2)
    full_name = "Mayur"
    info = {'Intro': "Data scientist"}

    with col1:
        st.markdown("<h2 style='text-align: center; '>Hello! I'm Mayur 👋</h2>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        .center-text {
        text-align: justify;
        }
        </style>
        <div class="justify-text">
        
        👋 About Me

        I am an AI Engineer & Data Scientist with a strong foundation in Machine Learning, Deep Learning, Computer Vision, and Generative AI. I specialize in building end-to-end AI solutions that transform ideas into impactful real-world applications.

        ✨ Highlights of my work include:

        LLaMA-Pen – an AI-powered blog generator with full MLOps integration (MLflow, DVC, CI/CD, AWS).

        River Plastic Detection – a YOLOv8-based computer vision system to detect plastic waste in rivers.

        CareCast – a TensorFlow CNN model achieving 92%+ accuracy in medical image classification.

        ⚙️ My toolbox includes PyTorch, TensorFlow, MLflow, Docker, FastAPI, Streamlit, Power BI, and deployment expertise on AWS, GCP, and Hugging Face Spaces.

        🎯 With internship experience in data analytics and predictive modeling, and certifications in Python, Computer Vision, and MLOps, I bring both practical industry experience and cutting-edge technical skills.

        🌍 My passion lies in LLMs, MLOps-driven AI systems, and scalable computer vision applications. I aim to build AI solutions that don’t just work in research—but thrive in the real world.


        I am a passionate Data Scientist and AI Engineer with hands-on experience in Machine Learning, Deep Learning, Computer Vision, and Generative AI. 
        I have a proven ability to design and deploy end-to-end AI solutions, from data collection and preprocessing to model training, deployment, and monitoring. 
        My expertise includes working with LLMs (LLaMA 2), MLOps (MLflow, DVC, CI/CD), and advanced computer vision models (YOLOv8), demonstrating my strength in translating cutting-edge research into impactful real-world applications.

        I have built and deployed projects such as an AI blog generator using LLaMA 2 with a complete MLOps pipeline, a YOLOv8-based river plastic detection system, and a CNN-powered health prediction tool.
        These projects showcase my ability to combine model development, cloud deployment (AWS, GCP, Hugging Face), and visualization (Streamlit, Power BI) into scalable, user-centric solutions.

        Alongside my technical expertise, I bring practical experience from internships where I developed interactive dashboards in Power BI and contributed to predictive modeling and EDA pipelines.
        I hold a B.Tech in Artificial Intelligence from Pune University and have certifications in Python, Computer Vision, and MLOps from globally recognized platforms.

        Currently, my focus is on Large Language Models, MLOps-driven workflows, and real-world computer vision solutions, with the goal of building reliable, scalable, and impactful
        AI systems that bridge the gap between research and business outcomes.            
                 
        </div>
        """, unsafe_allow_html=True)
        c1,c2, c3 =st.columns(3)
        c1.markdown("""**[GitHub](https://github.com/MayurjareMJ)**""")
        c2.markdown("""**[LinkedIn](https://www.linkedin.com/in/mayur-jare-mj/)** """)
        c3.markdown("""**[Medium](https://medium.com/@mayurjaremj)**""")


    path = r"C:\Users\mayur\OneDrive\Desktop\Final\assets\Animation_blue_robo.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:

        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get the base64 string of the image
logo_base64 = get_base64_image(r"C:\Users\mayur\OneDrive\Desktop\Final\assets\about\profile.jpg")

# Logo styling
logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""

# Display logo in the sidebar
st.sidebar.markdown(logo_html, unsafe_allow_html=True)
with st.sidebar:
    # Other sidebar elements
    # st.sidebar.image("logo_image.png", width=200, use_column_width=True)
    # Option menu in sidebar
    pages = ["About me", "Skills", "Experience",  "Projects & Publications", "Certifications", "Testimonials", "Resume", "Contact"]
    nav_tab_op = option_menu(
        menu_title="Mayur",
        options=pages,
        icons=['person-fill', 'briefcase', 'folder', 'mortarboard-fill', 'star', 'file-text', 'envelope'],
        menu_icon="cast",
        default_index=0,
    )
# Main content of the app
if nav_tab_op == "About me":
    aboutMe()

elif nav_tab_op == "Skills":
     skills()

elif nav_tab_op == "Experience":
    experience()

elif nav_tab_op == "Projects & Publications":
    projects()

elif nav_tab_op == "Certifications":
    certifications()

elif nav_tab_op == "Resume":
    resume()

elif nav_tab_op == "Contact":
    contact()
