import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

resume_path=r"C:\Users\mayur\OneDrive\Desktop\Final\assets\resume\Mayur_Jare_Cv (2).pdf"

def resume():
    with open(resume_path, "rb") as pdf_file:
        document = pdf_file.read()

    st.markdown("""
            <style>
            .stDownloadButton button {
                background-color: #1E9E35 !important;
                color: white !important;
            }
            </style>
            """, unsafe_allow_html=True)


    st.download_button(
                label="Download Resume",
                key="download_button",
                file_name=resume_path,
                data=document,
                help="Click to download.",
            )
    with st.container():
        st.markdown(
            """
            <style>
            .stContainer > div {
                width: 55%;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        pdf_viewer(resume_path)
