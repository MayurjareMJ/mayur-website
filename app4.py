# import streamlit as st
# from streamlit_option_menu import option_menu
# from streamlit_lottie import st_lottie
# import json
# import base64

# # Import custom pages
# from reume_page import resume
# from experience_page import experience
# from project_page import projects
# from contact_form import contact
# from certifications_page import certifications
# from skills import skills

# # ----------------- Page setup -----------------
# st.set_page_config(
#     page_title="Mayur | AI Portfolio",
#     page_icon="🤖",
#     layout="wide",
# )

# # ----------------- Helpers -----------------
# def load_lottie_file(filepath: str):
#     with open(filepath, "r") as file:
#         return json.load(file)

# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()

# logo_base64 = get_base64_image("assets/about/profile.jpg")

# # ----------------- Custom CSS -----------------
# st.markdown(f"""
#     <style>
#     /* Hide default header */
#     header {{visibility: hidden;}}
#     .block-container {{padding-top: 4rem; padding-left: 2rem; padding-right: 2rem;}}

#     /* Smooth scrolling */
#     html {{
#         scroll-behavior: smooth;
#         background: linear-gradient(135deg, #e0f7fa, #e1bee7);
#     }}

#     /* Navbar */
#     .navbar {{
#         position: fixed;
#         top: 0;
#         left: 0;
#         right: 0;
#         height: 60px;
#         background: rgba(63, 43, 150, 0.95);
#         display: flex;
#         align-items: center;
#         padding: 0 20px;
#         z-index: 1000;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.15);
#         border-bottom-left-radius: 12px;
#         border-bottom-right-radius: 12px;
#     }}
#     .navbar img {{
#         height: 45px;
#         width: 45px;
#         border-radius: 50%;
#         margin-right: 15px;
#         border: 2px solid #fff;
#         box-shadow: 0 2px 8px rgba(0,0,0,0.2);
#     }}

#     /* Option menu horizontal inside navbar */
#     .st-emotion-cache-1wmy9hl.e1fqkh3o3 {{
#         flex-grow: 1;
#         justify-content: flex-end;
#     }}

#     /* Card hover effect */
#     .card {{
#         background-color: white;
#         border-radius: 15px;
#         padding: 20px;
#         box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
#         transition: transform 0.3s ease;
#         margin-bottom: 20px;
#     }}
#     .card:hover {{
#         transform: translateY(-8px);
#         box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
#     }}

#     /* Gradient header */
#     .gradient-header {{
#         text-align: center;
#         font-size: 45px;
#         font-weight: bold;
#         background: linear-gradient(90deg, #3f2b96, #a8c0ff);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 20px;
#     }}

#     /* Mobile responsiveness */
#     @media (max-width: 768px) {{
#         .st-emotion-cache-1wmy9hl.e1fqkh3o3 {{
#             flex-wrap: wrap;
#             justify-content: center;
#         }}
#     }}
#     </style>
# """, unsafe_allow_html=True)

# # ----------------- Top Navbar -----------------
# st.markdown(f"""
# <div class="navbar">
#     <img src="data:image/png;base64,{logo_base64}" alt="logo">
# </div>
# """, unsafe_allow_html=True)

# # Place the option_menu in the navbar container
# selected = option_menu(
#     menu_title=None,
#     options=["About me", "Resume", "Skills", "Experience", "Projects", "Certifications", "Contact"],
#     icons=['person-fill', 'file-text', 'cpu', 'briefcase', 'folder', 'mortarboard-fill', 'envelope'],
#     orientation="horizontal",
#     default_index=0,
# )

# # ----------------- About Me -----------------
# def aboutMe():
#     st.markdown("<br><br>", unsafe_allow_html=True)  # spacing under navbar
#     st.markdown("<div class='gradient-header'>👋 Hello, I'm Mayur</div>", unsafe_allow_html=True)

#     col1, col2 = st.columns([2, 1], gap="large")

#     with col1:
#         st.write(
#             """
#             I’m an **AI Engineer & Data Scientist** passionate about building AI systems that scale in the real world.  
#             My work spans **Machine Learning, Deep Learning, Computer Vision, and Generative AI**.  
#             With expertise in **LLMs, MLOps, and Cloud Deployment**, I specialize in turning research into production-ready applications.
#             """
#         )

#         # Cards for highlights
#         c1, c2, c3 = st.columns(3)
#         with c1:
#             st.markdown(
#                 "<div class='card'><h4>🖊️ LLaMA-Pen</h4><p>AI-powered blog generator with full MLOps pipeline.</p></div>",
#                 unsafe_allow_html=True
#             )
#         with c2:
#             st.markdown(
#                 "<div class='card'><h4>🌊 River Plastic Detection</h4><p>YOLOv8-based vision system to detect river waste.</p></div>",
#                 unsafe_allow_html=True
#             )
#         with c3:
#             st.markdown(
#                 "<div class='card'><h4>🏥 CareCast</h4><p>CNN model achieving 92%+ accuracy in medical imaging.</p></div>",
#                 unsafe_allow_html=True
#             )

#         # Tech stack section
#         st.markdown("### 🛠️ Tech Stack")
#         st.markdown(
#             "- **Frameworks:** PyTorch, TensorFlow, YOLOv8  \n"
#             "- **MLOps & Deployment:** MLflow, DVC, Docker, FastAPI, Streamlit, AWS, GCP, Hugging Face  \n"
#             "- **Visualization:** Power BI, Streamlit"
#         )

#         # Social links
#         st.markdown("### 🌍 Connect with me")
#         c1, c2, c3 = st.columns(3)
#         c1.markdown("[**GitHub**](https://github.com/MayurjareMJ)")
#         c2.markdown("[**LinkedIn**](https://www.linkedin.com/in/mayur-jare-mj/)")
#         c3.markdown("[**Medium**](https://medium.com/@mayurjaremj)")

#     with col2:
#         lottie_path = "assets/Animation_blue_robo.json"
#         lottie_anim = load_lottie_file(lottie_path)
#         st_lottie(lottie_anim, height=350, key="robot")

# # ----------------- Main Content -----------------
# if selected == "About me":
#     aboutMe()
# elif selected == "Skills":
#     skills()
# elif selected == "Resume":
#     resume()
# elif selected == "Experience":
#     experience()
# elif selected == "Projects":
#     projects()
# elif selected == "Certifications":
#     certifications()
# elif selected == "Contact":
#     contact()

##############################3

import streamlit as st
from streamlit_lottie import st_lottie
import json
import base64

# Import custom pages
from reume_page import resume
from experience_page import experience
from project_page import projects
from contact_form import contact
from certifications_page import certifications
from skills import skills

# ----------------- Page setup -----------------
st.set_page_config(
    page_title="Mayur | AI Portfolio",
    page_icon="🤖",
    layout="wide",
)

# ----------------- Helpers -----------------
def load_lottie_file(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("assets/about/profile.jpg")

# ----------------- Custom CSS -----------------
st.markdown(f"""
<style>
/* Hide default header */
header {{visibility: hidden;}}

/* Add scroll-padding so sections aren't hidden behind sticky navbar */
html {{
    scroll-behavior: smooth;
    scroll-padding-top: 80px; /* height of navbar + spacing */
    background: linear-gradient(135deg, #e0f7fa, #e1bee7);
}}

/* Navbar */
.navbar {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 70px;
    background: rgba(63, 43, 150, 0.95);
    display: flex;
    align-items: center;
    padding: 0 20px;
    z-index: 1000;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
}}
.navbar img {{
    height: 50px;
    width: 50px;
    border-radius: 50%;
    margin-right: 15px;
    border: 2px solid #fff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}}
.navbar a {{
    color: white;
    font-weight: bold;
    margin-left: 25px;
    text-decoration: none;
}}
.navbar a:hover {{
    color: #ffeb3b;
}}

/* Section title */
.section-title {{
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    background: linear-gradient(90deg, #3f2b96, #a8c0ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
    padding-top: 50px;
}}

/* Card hover effect */
.card {{
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    margin-bottom: 20px;
}}
.card:hover {{
    transform: translateY(-8px);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}}

/* Mobile responsiveness */
@media (max-width: 768px) {{
    .navbar a {{
        margin-left: 10px;
        font-size: 14px;
    }}
}}
</style>
""", unsafe_allow_html=True)

# ----------------- Navbar -----------------
st.markdown(f"""
<div class="navbar">
    <img src="data:image/png;base64,{logo_base64}" alt="logo">
    <a href="#about">About me</a>
    <a href="#resume">Resume</a>
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#certifications">Certifications</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ----------------- Sections -----------------
def aboutMe():
    st.markdown('<h2 id="about" class="section-title">👋 About Me</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([2,1], gap="large")
    with col1:
        st.write("""
        I’m an **AI Engineer & Data Scientist** passionate about building AI systems that scale in the real world.  
        My work spans **Machine Learning, Deep Learning, Computer Vision, and Generative AI**.  
        With expertise in **LLMs, MLOps, and Cloud Deployment**, I specialize in turning research into production-ready applications.
        """)
    with col2:
        lottie_anim = load_lottie_file("assets/Animation_blue_robo.json")
        st_lottie(lottie_anim, height=350)

def resumeSection():
    st.markdown('<h2 id="resume" class="section-title">📄 Resume</h2>', unsafe_allow_html=True)
    resume()

def skillsSection():
    st.markdown('<h2 id="skills" class="section-title">🛠 Skills</h2>', unsafe_allow_html=True)
    skills()

def experienceSection():
    st.markdown('<h2 id="experience" class="section-title">💼 Experience</h2>', unsafe_allow_html=True)
    experience()

def projectsSection():
    st.markdown('<h2 id="projects" class="section-title">📁 Projects</h2>', unsafe_allow_html=True)
    projects()

def certificationsSection():
    st.markdown('<h2 id="certifications" class="section-title">🏆 Certifications</h2>', unsafe_allow_html=True)
    certifications()

def contactSection():
    st.markdown('<h2 id="contact" class="section-title">✉ Contact</h2>', unsafe_allow_html=True)
    contact()

# ----------------- Render Sections -----------------
aboutMe()
resumeSection()
skillsSection()
experienceSection()
projectsSection()
certificationsSection()
contactSection()
