import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import json
import os

def contact():
    st.title("📨 Contact Me")
    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    # ----------------- Left Column: Lottie Animation -----------------
    lottie_path = os.path.join("assets", "Animation_contact.json")  # relative path
    lottie_json = None
    if os.path.exists(lottie_path):
        with open(lottie_path, "r") as file:
            lottie_json = json.load(file)

    with col1:
        if lottie_json:
            st_lottie(
                lottie_json,
                reverse=True,
                height=400,
                width=400,
                speed=1,
                loop=True,
                quality="high",
            )
        else:
            st.write("🎬 Animation not found!")

    # ----------------- Right Column: Card-style Contact -----------------
    with col2:
        st.markdown(
            f"""
            <div style="
                background-color: #f9f9f9;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            ">
                <h3>Send Me a Message</h3>
                <p>Fill out the form below and I'll get back to you!</p>
                <p><b>Email:</b> <a href="mailto:mayurjaremj@gmail.com">mayurjaremj@gmail.com</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # components.html(
        #     """
        #     <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScLaMWyScjbqoo6I5w5MtoQwfSU-Izghn1y_jsTP-yuf5zZOA/viewform?embedded=true" 
        #             width="100%" height="741" frameborder="0" marginheight="0" marginwidth="0">
        #     Loading…
        #     </iframe>
        #     """,
        #     height=800,
        #     scrolling=True,
        # )
