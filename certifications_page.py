# import streamlit as st
# import json
# from streamlit_lottie import st_lottie

# def certifications():
#     col1, col2 = st.columns(2)

#     # col1.markdown("## Experience")
#     with col1:
#         st.markdown("""
#                 <style>
#                 .centered {
#                     display: flex;
#                     align-items: center;
#                     height: 100%;
#                     margin-top: 200px; /* Adjust this value as needed */
#                 }
#                 </style>
#                 <div class="centered">
#                     <h1> Certifications </h1>
#                 </div>
#             """, unsafe_allow_html=True)
#     path = r"C:\Users\mayur\OneDrive\Desktop\Final\assets\Animation_edu.json"
#     with open(path, "r") as file:
#         url = json.load(file)
#     with col2:
#         st_lottie(url,
#                   reverse=True,
#                   height=400,
#                   width=400,
#                   speed=1,
#                   loop=True,
#                   quality='high',
#                   )
#     st.markdown("---")

#     certification_list = [
#     ]

#     for i, certificate in enumerate(certification_list, start=1):
#         st.markdown(f"{i}. {certificate}")

import streamlit as st
import json
from streamlit_lottie import st_lottie

def certifications():
    st.title("🎓 Certifications")
    st.markdown("---")

    # ----------------- Load Lottie Animation -----------------
    lottie_path = "assets/Animation_edu.json"  # Adjust path if needed
    with open(lottie_path, "r") as file:
        lottie_json = json.load(file)
    
    st_lottie(
        lottie_json,
        height=300,
        width=300,
        loop=True,
        speed=1
    )

    st.markdown("---")

    # ----------------- Certificate Data -----------------
    certification_list = [
        {
            "title": "Deep Learning Specialization",
            "issuer": "Coursera",
            "link": "https://www.coursera.org/account/accomplishments/specialization/certificate/ABC123"
        },
        {
            "title": "Computer Vision Nanodegree",
            "issuer": "Udacity",
            "link": "https://confirm.udacity.com/XYZ456"
        },
        {
            "title": "AWS Certified Machine Learning – Specialty",
            "issuer": "AWS",
            "link": "https://aws.amazon.com/certification/certificate/ML789"
        },
        {
            "title": "Hugging Face Transformers Course",
            "issuer": "Hugging Face",
            "link": "https://huggingface.co/courses"
        }
    ]

    # ----------------- Display as Interactive Cards -----------------
    st.markdown(
        """
        <style>
        .cert-card {
            background-color: #f9f9f9;
            padding: 20px;
            margin: 10px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .cert-card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
        }
        .cert-link {
            color: #3f2b96;
            text-decoration: none;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Use 2-column layout for cards
    cols = st.columns(2)
    for idx, cert in enumerate(certification_list):
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="cert-card">
                    <h4>🎓 {cert['title']}</h4>
                    <p><b>Issuer:</b> {cert['issuer']}</p>
                    <a href="{cert['link']}" target="_blank" class="cert-link">View Certificate</a>
                </div>
                """, unsafe_allow_html=True
            )
