# import streamlit as st
# from streamlit_option_menu import option_menu
# import base64
# from streamlit_lottie import st_lottie
# import json

# # Import custom pages
# from reume_page import resume
# from experience_page import experience
# from project_page import projects
# from contact_form import contact
# from certifications_page import certifications
# from skills_page import skills
# from cv_demo.cv_demo import cv_demo
# #from education_page import education


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

# # ----------------- About Me -----------------
# def aboutMe():
#     st.markdown(
#         """
#         <style>
#         .gradient-header {
#             text-align: center;
#             font-size: 45px;
#             font-weight: bold;
#             background: linear-gradient(90deg, #3f2b96, #a8c0ff);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             margin-bottom: 10px;
#         }
#         .card {
#             background-color: white;
#             border-radius: 15px;
#             padding: 20px;
#             box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
#             transition: transform 0.3s ease;
#         }
#         .card:hover {
#             transform: translateY(-8px);
#             box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
#         }
#         </style>
#         """, unsafe_allow_html=True
#     )

#     st.markdown("<div class='gradient-header'>👋 Hello, I'm Mayur</div>", unsafe_allow_html=True)

#     col1, col2 = st.columns([2, 1], gap="large")

#     with col1:
#         st.markdown(
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
#                 """
#                 <div class='card'>
#                 <h4>🖊️ LLaMA-Pen</h4>
#                 <p>AI-powered blog generator with full MLOps pipeline.</p>
#                 </div>
#                 """, unsafe_allow_html=True
#             )
#         with c2:
#             st.markdown(
#                 """
#                 <div class='card'>
#                 <h4>🌊 River Plastic Detection</h4>
#                 <p>YOLOv8-based vision system to detect river waste.</p>
#                 </div>
#                 """, unsafe_allow_html=True
#             )
#         with c3:
#             st.markdown(
#                 """
#                 <div class='card'>
#                 <h4>🏥 CareCast</h4>
#                 <p>CNN model achieving 92%+ accuracy in medical imaging.</p>
#                 </div>
#                 """, unsafe_allow_html=True
#             )

#         # Tech stack section
#         st.markdown("### 🛠️ Tech Stack")
#         st.markdown(
#             """
#             - **Frameworks:** PyTorch, TensorFlow, YOLOv8  
#             - **MLOps & Deployment:** MLflow, DVC, Docker, FastAPI, Streamlit, AWS, GCP, Hugging Face  
#             - **Visualization:** Power BI, Streamlit  
#             """
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

# # ----------------- Top Navigation -----------------
# selected = option_menu(
#     menu_title=None,
#     options=["About me", "Projects", "Skills" , "Experience", "CV Demo", "Certifications","Education" ,"Contact"],
#     icons=['person-fill', "folder", "cpu", 'briefcase', 'camera', 'mortarboard-fill', 'file-text','envelope','file-text'],
#     orientation="horizontal",
#     default_index=0,
# )

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
# elif selected == "CV Demo":
#     cv_demo()



# ############################################

# # import streamlit as st
# # from streamlit_option_menu import option_menu
# # import base64
# # from streamlit_lottie import st_lottie
# # import json

# # # Import custom pages
# # from experience_page import experience
# # from project_page import projects
# # from contact_form import contact
# # from certifications_page import certifications
# # from skills_page import skills
# # from cv_demo.cv_demo import cv_demo
# # # from education_page import education


# # # ----------------- Page setup -----------------
# # st.set_page_config(
# #     page_title="Mayur | AI Portfolio",
# #     page_icon="🤖",
# #     layout="wide",
# # )

# # # ----------------- Helpers -----------------
# # def load_lottie_file(filepath: str):
# #     with open(filepath, "r") as file:
# #         return json.load(file)

# # def get_base64_image(image_path):
# #     with open(image_path, "rb") as img_file:
# #         return base64.b64encode(img_file.read()).decode()

# # # ----------------- About Me -----------------
# # def aboutMe():
# #     st.markdown(
# #         """
# #         <style>
# #         .gradient-header {
# #             text-align: center;
# #             font-size: 45px;
# #             font-weight: bold;
# #             background: linear-gradient(90deg, #3f2b96, #a8c0ff);
# #             -webkit-background-clip: text;
# #             -webkit-text-fill-color: transparent;
# #             margin-bottom: 10px;
# #         }
# #         .card {
# #             background-color: white;
# #             border-radius: 15px;
# #             padding: 20px;
# #             box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
# #             transition: transform 0.3s ease;
# #         }
# #         .card:hover {
# #             transform: translateY(-8px);
# #             box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
# #         }
# #         </style>
# #         """, unsafe_allow_html=True
# #     )

# #     st.markdown("<div class='gradient-header'>👋 Hello, I'm Mayur</div>", unsafe_allow_html=True)

# #     col1, col2 = st.columns([2, 1], gap="large")

# #     with col1:
# #         st.markdown(
# #             """
# #             I’m an **AI Engineer & Data Scientist** passionate about building AI systems that scale in the real world.  
# #             My work spans **Machine Learning, Deep Learning, Computer Vision, and Generative AI**.  
# #             With expertise in **LLMs, MLOps, and Cloud Deployment**, I specialize in turning research into production-ready applications.
# #             """
# #         )

# #         # Cards for highlights
# #         c1, c2, c3 = st.columns(3)
# #         with c1:
# #             st.markdown(
# #                 """
# #                 <div class='card'>
# #                 <h4>🖊️ LLaMA-Pen</h4>
# #                 <p>AI-powered blog generator with full MLOps pipeline.</p>
# #                 </div>
# #                 """, unsafe_allow_html=True
# #             )
# #         with c2:
# #             st.markdown(
# #                 """
# #                 <div class='card'>
# #                 <h4>🌊 River Plastic Detection</h4>
# #                 <p>YOLOv8-based vision system to detect river waste.</p>
# #                 </div>
# #                 """, unsafe_allow_html=True
# #             )
# #         with c3:
# #             st.markdown(
# #                 """
# #                 <div class='card'>
# #                 <h4>🏥 CareCast</h4>
# #                 <p>CNN model achieving 92%+ accuracy in medical imaging.</p>
# #                 </div>
# #                 """, unsafe_allow_html=True
# #             )

# #         # Tech stack section
# #         st.markdown("### 🛠️ Tech Stack")
# #         st.markdown(
# #             """
# #             - **Frameworks:** PyTorch, TensorFlow, YOLOv8  
# #             - **MLOps & Deployment:** MLflow, DVC, Docker, FastAPI, Streamlit, AWS, GCP, Hugging Face  
# #             - **Visualization:** Power BI, Streamlit  
# #             """
# #         )

# #         # Social links
# #         st.markdown("### 🌍 Connect with me")
# #         c1, c2, c3 = st.columns(3)
# #         c1.markdown("[**GitHub**](https://github.com/MayurjareMJ)")
# #         c2.markdown("[**LinkedIn**](https://www.linkedin.com/in/mayur-jare-mj/)")
# #         c3.markdown("[**Medium**](https://medium.com/@mayurjaremj)")

# #     with col2:
# #         lottie_path = "assets/Animation_blue_robo.json"
# #         lottie_anim = load_lottie_file(lottie_path)
# #         st_lottie(lottie_anim, height=350, key="robot")

# # # ----------------- Top Navigation -----------------
# # selected = option_menu(
# #     menu_title=None,
# #     options=["About me", "Projects", "Skills" , "Experience", "CV Demo", "Certifications","Education" ,"Contact"],
# #     icons=['person-fill', "folder", "cpu", 'briefcase', 'camera', 'mortarboard-fill', 'file-text','envelope','file-text'],
# #     orientation="horizontal",
# #     default_index=0,
# # )

# # # ----------------- Main Content -----------------
# # if selected == "About me":
# #     aboutMe()
# # elif selected == "Skills":
# #     skills()
# # elif selected == "Experience":
# #     experience()
# # elif selected == "Projects":
# #     projects()
# # elif selected == "Certifications":
# #     certifications()
# # elif selected == "Contact":
# #     contact()
# # elif selected == "CV Demo":
# #     cv_demo()


#########################3
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import json

# ----------------- Import Custom Pages -----------------
from experience_page import experience
from project_page import projects
from contact_form import contact
from certifications_page import certifications
from skills_page import skills
from cv_demo.cv_demo import cv_demo
# from education_page import education  # Uncomment when ready


# ----------------- Page Setup -----------------
st.set_page_config(
    page_title="Mayur | AI Portfolio",
    page_icon="🤖",
    layout="wide",
)


# ----------------- Helper Functions -----------------
def load_lottie_file(filepath: str):
    """Load Lottie animation from a local JSON file."""
    with open(filepath, "r") as file:
        return json.load(file)


def get_base64_image(image_path):
    """Convert image to Base64 for embedding."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def is_mobile():
    """Detect mobile view based on Streamlit width or user agent."""
    try:
        return st.session_state.get("device", None) == "mobile"
    except:
        return False


# ----------------- THEME TOGGLE -----------------
# Initialize theme
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"  # default mode


def toggle_theme():
    """Switch between dark and light themes."""
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"


# Theme toggle button on top-right
col1, col2 = st.columns([10, 1])
with col2:
    if st.session_state["theme"] == "light":
        if st.button("🌙", help="Switch to Dark Mode"):
            toggle_theme()
    else:
        if st.button("🌞", help="Switch to Light Mode"):
            toggle_theme()

# Inject CSS for the selected theme
if st.session_state["theme"] == "dark":
    st.markdown("""
        <style>
            body, .stMarkdown, .stText, p, h4 {
                color: #f0f0f0 !important;
                background-color: #0e1117 !important;
            }
            .card {
                background-color: #1e1e1e !important;
                box-shadow: 0px 4px 10px rgba(255,255,255,0.05) !important;
            }
            .card:hover {
                box-shadow: 0px 8px 20px rgba(255,255,255,0.08) !important;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body, .stMarkdown, .stText, p, h4 {
                color: #000000 !important;
                background-color: #ffffff !important;
            }
            .card {
                background-color: #ffffff !important;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.1) !important;
            }
            .card:hover {
                box-shadow: 0px 8px 20px rgba(0,0,0,0.15) !important;
            }
        </style>
    """, unsafe_allow_html=True)


# ----------------- ABOUT ME SECTION -----------------
def aboutMe():
    st.markdown(
        """
        <style>
        /* ---------- LIGHT MODE (default) ---------- */
        .gradient-header {
            text-align: center;
            font-size: 45px;
            font-weight: bold;
            background: linear-gradient(90deg, #3f2b96, #a8c0ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        }
        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
        }

        /* ---------- DARK MODE ---------- */
        @media (prefers-color-scheme: dark) {
            .gradient-header {
                background: linear-gradient(90deg, #a8c0ff, #3f2b96);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .card {
                background-color: #1e1e1e;
                box-shadow: 0px 4px 10px rgba(255,255,255,0.05);
            }
            .card:hover {
                box-shadow: 0px 8px 20px rgba(255,255,255,0.08);
            }
            body, p, h4 {
                color: #f0f0f0 !important;
            }
        }

        /* ---------- RESPONSIVE ---------- */
        @media only screen and (max-width: 800px) {
            .gradient-header {
                font-size: 36px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
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
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                """
                <div class='card'>
                    <h4>🌊 River Plastic Detection</h4>
                    <p>YOLOv8-based vision system to detect river waste.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                """
                <div class='card'>
                    <h4>🏥 CareCast</h4>
                    <p>CNN model achieving 92%+ accuracy in medical imaging.</p>
                </div>
                """,
                unsafe_allow_html=True,
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
        try:
            lottie_anim = load_lottie_file(lottie_path)
            st_lottie(lottie_anim, height=350, key="robot")
        except FileNotFoundError:
            st.warning("🤖 Animation file not found. Please check the assets folder path.")


# ----------------- Responsive Navigation -----------------
st.markdown(
    """
    <script>
        function detectDevice() {
            const width = window.innerWidth;
            if (width < 900) {
                window.parent.postMessage({ type: 'streamlit:setSessionState', key: 'device', value: 'mobile' }, '*');
            } else {
                window.parent.postMessage({ type: 'streamlit:setSessionState', key: 'device', value: 'desktop' }, '*');
            }
        }
        window.addEventListener('load', detectDevice);
        window.addEventListener('resize', detectDevice);
    </script>
    """,
    unsafe_allow_html=True,
)

# Determine device type
device_type = st.session_state.get("device", "desktop")

# Dynamic Navigation
if device_type == "mobile":
    with st.sidebar:
        selected = option_menu(
            "Navigate",
            ["About me", "Projects", "Skills", "Experience", "CV Demo", "Certifications", "Education", "Contact"],
            icons=["person-fill", "folder", "cpu", "briefcase", "file-text", "mortarboard-fill", "book", "envelope"],
            menu_icon="cast",
            default_index=0,
        )
else:
    selected = option_menu(
        menu_title=None,
        options=["About me", "Projects", "Skills", "Experience", "CV Demo", "Certifications", "Education", "Contact"],
        icons=["person-fill", "folder", "cpu", "briefcase", "file-text", "mortarboard-fill", "book", "envelope"],
        orientation="horizontal",
        default_index=0,
    )


# ----------------- Main Content -----------------
if selected == "About me":
    aboutMe()
elif selected == "Skills":
    skills()
elif selected == "Experience":
    experience()
elif selected == "Projects":
    projects()
elif selected == "Certifications":
    certifications()
elif selected == "Contact":
    contact()
# elif selected == "CV Demo":
#     cv_demo()
elif selected == "Education":
    st.info("🎓 Education page coming soon!")

