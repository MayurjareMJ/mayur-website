
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import json

# Import custom pages
from reume_page import resume
from experience_page import experience
from project_page import projects
from contact_form import contact
from certifications_page import certifications
from skills import skills


# ----------------- Page setup -----------------
st.set_page_config(
    page_title="Mayur",
    page_icon="📋",
    layout="wide",
)


# ----------------- Helpers -----------------
def load_lottie_file(filepath: str):
    """Load lottie animation from a local JSON file"""
    with open(filepath, "r") as file:
        return json.load(file)


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# ----------------- About Me Page -----------------
def aboutMe():
    st.markdown(
        """
        <style>
        .card {
            background-color: #1E1E1E;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
            color: white;
            margin-bottom: 20px;
        }
        .card h3 {
            color: #00C9A7;
        }
        .badge {
            display: inline-block;
            background: #00C9A7;
            color: white;
            padding: 5px 12px;
            border-radius: 12px;
            margin: 4px;
            font-size: 14px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown("<h2 style='color:#00C9A7;'>👋 Hello, I'm Mayur</h2>", unsafe_allow_html=True)
        st.write(
            "I’m an **AI Engineer & Data Scientist** passionate about building AI systems that scale in the real world."
        )

        # Highlights Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🚀 Highlights")
        st.markdown(
            """
            - 🖊️ **LLaMA-Pen** – AI-powered blog generator with **MLOps integration**  
            - 🌊 **River Plastic Detection** – YOLOv8 system to detect river waste  
            - 🏥 **CareCast** – CNN achieving **92%+ accuracy** in medical imaging  
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)

        # Tech Stack Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Tech Stack")
        st.markdown(
            """
            <span class="badge">PyTorch</span> <span class="badge">TensorFlow</span> 
            <span class="badge">YOLOv8</span> <span class="badge">MLflow</span>  
            <span class="badge">Docker</span> <span class="badge">FastAPI</span> 
            <span class="badge">AWS</span> <span class="badge">GCP</span> 
            <span class="badge">Hugging Face</span> <span class="badge">Power BI</span>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        # Social Links Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🌍 Connect with Me")
        c1, c2, c3 = st.columns(3)
        c1.markdown("[**GitHub**](https://github.com/MayurjareMJ)")
        c2.markdown("[**LinkedIn**](https://www.linkedin.com/in/mayur-jare-mj/)")
        c3.markdown("[**Medium**](https://medium.com/@mayurjaremj)")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        lottie_path = "assets/Animation_blue_robo.json"
        lottie_anim = load_lottie_file(lottie_path)
        st_lottie(lottie_anim, height=350, key="robot")


# ----------------- Sidebar -----------------
logo_base64 = get_base64_image("assets/about/profile.jpg")

logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
    }}
    .logo {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #00C9A7;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""

st.sidebar.markdown(logo_html, unsafe_allow_html=True)

with st.sidebar:
    pages = [
        "About me",
        "Resume",
        "Skills",
        "Experience",
        "Projects & Publications",
        "Certifications",
        "Contact",
    ]
    nav_tab_op = option_menu(
        menu_title="Navigation",
        options=pages,
        icons=[
            "person-fill",
            "file-text",
            "cpu",
            "briefcase",
            "folder",
            "mortarboard-fill",
            "envelope",
        ],
        menu_icon="cast",
        default_index=0,
    )


# ----------------- Main Content -----------------
if nav_tab_op == "About me":
    aboutMe()
elif nav_tab_op == "Skills":
    skills()
elif nav_tab_op == "Resume":
    resume()
elif nav_tab_op == "Experience":
    experience()
elif nav_tab_op == "Projects & Publications":
    projects()
elif nav_tab_op == "Certifications":
    certifications()
elif nav_tab_op == "Contact":
    contact()