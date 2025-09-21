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
from skills_page import skills
from cv_demo.cv_demo import cv_demo
#from education_page import education


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

# ----------------- About Me -----------------
def aboutMe():
    st.markdown(
        """
        <style>
        .gradient-header {
            text-align: center;
            font-size: 45px;
            font-weight: bold;
            background: linear-gradient(90deg, #3f2b96, #a8c0ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .card {
            background-color: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("<div class='gradient-header'>👋 Hello, I'm Mayur</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(
            """
            I’m an **AI Engineer & Data Scientist** passionate about building AI systems that scale in the real world.  
            My work spans **Machine Learning, Deep Learning, Computer Vision, and Generative AI**.  
            With expertise in **LLMs, MLOps, and Cloud Deployment**, I specialize in turning research into production-ready applications.
            """
        )

        # Cards for highlights
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                """
                <div class='card'>
                <h4>🖊️ LLaMA-Pen</h4>
                <p>AI-powered blog generator with full MLOps pipeline.</p>
                </div>
                """, unsafe_allow_html=True
            )
        with c2:
            st.markdown(
                """
                <div class='card'>
                <h4>🌊 River Plastic Detection</h4>
                <p>YOLOv8-based vision system to detect river waste.</p>
                </div>
                """, unsafe_allow_html=True
            )
        with c3:
            st.markdown(
                """
                <div class='card'>
                <h4>🏥 CareCast</h4>
                <p>CNN model achieving 92%+ accuracy in medical imaging.</p>
                </div>
                """, unsafe_allow_html=True
            )

        # Tech stack section
        st.markdown("### 🛠️ Tech Stack")
        st.markdown(
            """
            - **Frameworks:** PyTorch, TensorFlow, YOLOv8  
            - **MLOps & Deployment:** MLflow, DVC, Docker, FastAPI, Streamlit, AWS, GCP, Hugging Face  
            - **Visualization:** Power BI, Streamlit  
            """
        )

        # Social links
        st.markdown("### 🌍 Connect with me")
        c1, c2, c3 = st.columns(3)
        c1.markdown("[**GitHub**](https://github.com/MayurjareMJ)")
        c2.markdown("[**LinkedIn**](https://www.linkedin.com/in/mayur-jare-mj/)")
        c3.markdown("[**Medium**](https://medium.com/@mayurjaremj)")

    with col2:
        lottie_path = "assets/Animation_blue_robo.json"
        lottie_anim = load_lottie_file(lottie_path)
        st_lottie(lottie_anim, height=350, key="robot")

# ----------------- Top Navigation -----------------
selected = option_menu(
    menu_title=None,
    options=["About me", "Projects", "Skills" , "Experience", "CV Demo", "Certifications","Education" ,"Contact"],
    icons=['person-fill', "folder", "cpu", 'briefcase', 'camera', 'mortarboard-fill', 'file-text','envelope','file-text'],
    orientation="horizontal",
    default_index=0,
)

# ----------------- Main Content -----------------
if selected == "About me":
    aboutMe()
elif selected == "Skills":
    skills()
elif selected == "Resume":
    resume()
elif selected == "Experience":
    experience()
elif selected == "Projects":
    projects()
elif selected == "Certifications":
    certifications()
elif selected == "Contact":
    contact()
elif selected == "CV Demo":
    cv_demo()

##########

