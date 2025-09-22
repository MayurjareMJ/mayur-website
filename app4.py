import streamlit as st
from streamlit_lottie import st_lottie
import json
import base64

# Import custom pages
from pages.reume_page import resume
from pages.experience_page import experience
from pages.project_page import projects
from pages.contact_form import contact
from pages.certifications_page import certifications
from pages.skills_page import skills
from cv_demo.cv_demo import cv_demo
from cv_demo import cv_demo


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

# Resume path
resume_path = r"C:\Users\mayur\OneDrive\Desktop\Final\assets\resume\Mayur_Jare_Cv (2).pdf"

# ----------------- Custom CSS -----------------
st.markdown(f"""
<style>
/* Hide default header */
header {{visibility: hidden;}}

/* Add scroll-padding so sections aren't hidden behind sticky navbar */
html {{
    scroll-behavior: smooth;
    scroll-padding-top: 80px;
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

/* Eye icon for resume */
.resume-eye {{
    display: inline-block;
    vertical-align: middle;
    margin-left: 10px;
    cursor: pointer;
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
    <a href="#about">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#cv">CV Demo</a>
    <a href="#certifications">Certifications</a>
    <a href="#education">Education</a>
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
        # Small eye icon for resume view/download
        with open(resume_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.markdown(f"""
            <a href="data:application/pdf;base64,{base64.b64encode(PDFbyte).decode()}" target="_blank" class="resume-eye">👁️ View Resume</a>
        """, unsafe_allow_html=True)
    with col2:
        lottie_anim = load_lottie_file("assets/Animation_blue_robo.json")
        st_lottie(lottie_anim, height=350)

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
    st.markdown("### 📄 CV / Resume")
    with open(resume_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="View / Download Resume",
        data=PDFbyte,
        file_name="Mayur_Resume.pdf",
        mime="application/pdf"
    )

def cvDemoSection():
    st.markdown('<h2 id="cv" class="section-title">📄 CV Demo</h2>', unsafe_allow_html=True)
    st.write("Preview your CV below:")
    with open(resume_path, "rb") as f:
        PDFbyte = f.read()
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="Mayur_Resume.pdf",
        mime="application/pdf"
    )

# ----------------- Render Sections -----------------
aboutMe()
projectsSection()
skillsSection()
experienceSection()
cvDemoSection()
certificationsSection()
# Uncomment if you have Education section
# educationSection()
contactSection()

