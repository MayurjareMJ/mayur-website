import streamlit as st
from streamlit_lottie import st_lottie
import json

def experience():
    col1,col2 =st.columns(2)

    with col1:
        st.markdown("""
            <style>
            .centered {
                display: flex;
                align-items: center;
                height: 100%;
                margin-top: 200px; /* Adjust this value as needed */
            }
            </style>
            <div class="centered">
                <h2>Experience</h2>
            </div>
        """, unsafe_allow_html=True)
    path = r"C:\Users\mayur\OneDrive\Desktop\Final\assets\Animation_exp.json"
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
        
    with st.container():
        col1, col2 = st.columns([3, 2])
        
        col1.markdown(""" 
            #### Computer Vision Engineer Intern –– [Elansol Technologies Pvt.Ltd](https://elansoltech.com/) (December 2021 - December 2024)
            - Conducted A/B testing experiments to assess the effectiveness of various
            promotion strategies, resulting in a remarkable 24% increase in revenue.
            - Developed machine learning models using scikit-learn to optimize pricing
            strategies, leading to a substantial 12% boost in profit.
            - Led full data lifecycle: collection, cleaning, feature engineering, modeling,
            validation, and dashboard/report creation.
            - Proficiently developed complex SQL queries, procedures, and reports using
            Redshift, Sagemaker, SQL, and Python to meet diverse client needs.
            - Developed a Large-scale multi-label text classification model using Tensorflow
            and Keras to enhance text analysis capabilities.
                            """)
        col2.markdown("""
            **Tools:**

            - Programming Languages: Python, SQL
            - Machine Learning: Scikit-Learn, TensorFlow, Keras
            - Data Visualization: Matplotlib, Seaborn, Plotly, Retool, Tableau
            - Cloud: Redshift, Sagemaker, S3 Bucket
            - ETL Processes: Custom SQL, Python scripts
            - A/B Testing: Custom Python scripts
            - Other Tools: Git, Colab Notebooks, Retool
            """)
    
    with st.container():
        col1, col2 = st.columns([3,2])

        col1.markdown("""
            #### Artificial Intelligence Engineer intern –– [Naresh It Technologies](https://www.uniquify.com)(January 2025 - June 2025)
            - Led training and development of neural networks using TensorFlow, optimizing
            models for enhanced accuracy and efficiency.
            - Conducted comprehensive experiments with TensorFlow scripts and analyzed
            results to enhance model performance and understand framework dynamics.
            - Played a key role in debugging and improving an automation framework for
            neural network and TensorFlow scripts, streamlining workflows and ensuring
            reliable model training.
            - Developed advanced image processing and segmentation algorithms to solve
            complex problems, contributing to project success.
            """)
        col2.markdown("""
            **Tools:**
    
            - Programming Languages: Python
            - Machine Learning: TensorFlow, PyTorch
            - Image Processing: OpenCV, custom Python scripts
            - Object Detection: YOLO
            - Image Labeling:  LabelImg
            - Automation: Custom Python scripts
            """)
    with st.container():
        col1, col2 = st.columns([3,2])
        col1.markdown("""
        #### Data Analyst –– [Spark Minda](https://sparkminda.com/) (January 2020 - July 2021)
        - Developed an NLP system using NLTK to automate text analysis, resulting in a significant 39% reduction in manual analysis efforts, improving efficiency and accuracy.
        - Leveraged analytical and technical expertise to provide actionable insights and proposals, driving business improvement strategies.
        - Designed and implemented a range of predictive models, including classification and forecasting models, using various machine learning tools to solve complex business challenges.
        - Identified trends, key metrics, and critical data points, generating insightful dashboards using a variety of data visualization tools to facilitate data-driven decision-making.
            """)
        col2.markdown("""
        **Tools & Skills:**
    - **Programming Languages:** Python, SQL
    - **Libraries & Frameworks:** NLTK, scikit-learn, Pandas, NumPy
    - **Machine Learning Tools:** Classification, Forecasting
    - **Data Visualization Tools:** Tableau, Matplotlib, Seaborn, Power BI
    - **Other:** Data Cleaning, Statistical Analysis, Predictive Modeling """)
