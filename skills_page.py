# import streamlit as st
# import time

# # ----------------- Skills Page -----------------
# def skills():
#     st.markdown('<h2 id="skills" class="section-title">🛠 Skills</h2>', unsafe_allow_html=True)

#     # Custom CSS for cards
#     st.markdown("""
#     <style>
#     .skill-card {
#         background-color: white;
#         border-radius: 15px;
#         padding: 20px;
#         margin: 10px;
#         box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
#         transition: transform 0.3s ease, box-shadow 0.3s ease;
#         display: inline-block;
#         vertical-align: top;
#         width: 300px;
#     }
#     .skill-card:hover {
#         transform: translateY(-8px);
#         box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
#     }
#     .skill-icon {
#         font-size: 30px;
#         margin-bottom: 10px;
#     }
#     .skill-title {
#         font-weight: bold;
#         font-size: 20px;
#         margin-bottom: 5px;
#     }
#     .skill-desc {
#         font-size: 14px;
#         color: #333;
#         margin-bottom: 10px;
#     }
#     .progress-container {
#         background-color: #e0e0e0;
#         border-radius: 10px;
#         overflow: hidden;
#         height: 15px;
#         margin-bottom: 10px;
#     }
#     .progress-bar {
#         height: 15px;
#         background: linear-gradient(90deg, #3f2b96, #a8c0ff);
#         width: 0%;
#         transition: width 1.5s ease-in-out;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # ----------------- Skill Cards -----------------
#     skill_data = [
#         {"icon": "🐍", "title": "Languages", "desc": "Python, SQL", "level": 95},
#         {"icon": "🤖", "title": "AI/ML", "desc": "ML, Deep Learning (ANN, CNN, RNN, LSTM, GRU), NLP, LLMs, CV, Transformers, Image Processing, Statistics", "level": 90},
#         {"icon": "🧠", "title": "GenAI & NLP", "desc": "OpenAI GPT, Hugging Face Transformers, LangChain, Vector DB, NLTK, SpaCy", "level": 85},
#         {"icon": "🗄️", "title": "Databases", "desc": "MySQL, PostgreSQL, MongoDB", "level": 80},
#         {"icon": "⚙️", "title": "MLOps", "desc": "Docker, Kubernetes, MLflow, Statistical Modeling, CI/CD Pipelines", "level": 80},
#         {"icon": "☁️", "title": "Cloud & Tools", "desc": "Git, Hugging Face Spaces, Jupyter, VS Code, Colab, AWS, Azure", "level": 75},
#         {"icon": "🌐", "title": "Web Tech", "desc": "Django, Flask, RESTful API", "level": 70},
#         {"icon": "🛠️", "title": "Frameworks & Libraries", "desc": "TensorFlow, PyTorch, OpenCV, Scikit-learn, Keras, NumPy, Pandas, Matplotlib, Seaborn, OpenAI APIs", "level": 90},
#         {"icon": "📊", "title": "Other Tools", "desc": "Power BI, MS Excel", "level": 85}
#     ]

#     st.markdown('<div style="display:flex; flex-wrap:wrap;">', unsafe_allow_html=True)

#     for skill in skill_data:
#         st.markdown(f"""
#         <div class="skill-card">
#             <div class="skill-icon">{skill['icon']}</div>
#             <div class="skill-title">{skill['title']}</div>
#             <div class="skill-desc">{skill['desc']}</div>
#             <div class="progress-container">
#                 <div class="progress-bar" id="{skill['title'].replace(' ', '_')}"></div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

#     # ----------------- Animate Progress Bars -----------------
#     animate_script = "<script>"
#     for skill in skill_data:
#         animate_script += f"""
#         var bar = document.getElementById('{skill['title'].replace(' ', '_')}');
#         bar.style.width = '{skill['level']}%';
#         """
#     animate_script += "</script>"

#     st.markdown(animate_script, unsafe_allow_html=True)








############################
import streamlit as st

# ----------------- Skills Page -----------------
def skills():
    st.markdown('<h2 id="skills" class="section-title">🛠 Skills</h2>', unsafe_allow_html=True)

    # ---------- Custom CSS ----------
    st.markdown("""
    <style>
    .category-wrapper {
        margin-bottom: 30px;
    }
    .category-title {
        font-size: 20px;
        font-weight: bold;
        margin: 20px 0 10px 0;
        color: #3f2b96;
    }
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 20px;
    }
    .skill-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .skill-card:hover {
        transform: translateY(-8px);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
    }
    .skill-icon img {
        width: 50px;
        height: 50px;
        margin-bottom: 12px;
        object-fit: contain;
    }
    .skill-title {
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 6px;
    }
    .progress-container {
        background-color: #e0e0e0;
        border-radius: 10px;
        overflow: hidden;
        height: 12px;
        width: 100%;
    }
    .progress-bar {
        height: 12px;
        background: linear-gradient(90deg, #3f2b96, #a8c0ff);
        width: 0%;
        animation: fillBar 2s ease-in-out forwards;
    }
    @keyframes fillBar {
        from { width: 0%; }
        to { width: var(--progress-width, 100%); }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- Skills Data ----------
    skills_by_category = {
        "Languages": [
            {"img": "assets/skills/python.png", "title": "Python", "level": 95},
            {"img": "assets/skills/mysql.png", "title": "MySQL", "level": 85},
            {"img": "assets/skills/postgresql.png", "title": "PostgreSQL", "level": 80},
            {"img": "assets/skills/mongodb.png", "title": "MongoDB", "level": 80},
        ],
        "AI / ML": [
            {"img": "assets/skills/tensorflow.png", "title": "TensorFlow", "level": 85},
            {"img": "assets/skills/pytorch.png", "title": "PyTorch", "level": 85},
            {"img": "assets/skills/opencv.png", "title": "OpenCV", "level": 80},
        ],
        "GenAI & NLP": [
            {"img": "assets/skills/huggingface.png", "title": "Hugging Face", "level": 80},
            {"img": "assets/skills/openai.png", "title": "OpenAI", "level": 80},
            {"img": "assets/skills/langchain.png", "title": "LangChain", "level": 75},
            {"img": "assets/skills/spacy.png", "title": "SpaCy", "level": 75},
            {"img": "assets/skills/nltk.png", "title": "NLTK", "level": 70},
        ],
        "MLOps": [
            {"img": "assets/skills/docker.png", "title": "Docker", "level": 85},
            {"img": "assets/skills/kubernetes.png", "title": "Kubernetes", "level": 80},
            {"img": "assets/skills/mlflow.png", "title": "MLflow", "level": 75},
            {"img": "assets/skills/github-actions.png", "title": "GitHub Actions", "level": 70},
        ],
        "Cloud & Tools": [
            {"img": "assets/skills/git.png", "title": "Git", "level": 85},
            {"img": "assets/skills/github.png", "title": "GitHub", "level": 85},
            {"img": "assets/skills/aws.png", "title": "AWS", "level": 80},
            {"img": "assets/skills/azure.png", "title": "Azure", "level": 75},
            {"img": "assets/skills/vscode.png", "title": "VS Code", "level": 90},
            {"img": "assets/skills/colab.png", "title": "Google Colab", "level": 85},
        ],
        "Web Tech": [
            {"img": "assets/skills/django.png", "title": "Django", "level": 80},
            {"img": "assets/skills/flask.png", "title": "Flask", "level": 80},
            {"img": "assets/skills/rest.png", "title": "REST API", "level": 75},
        ],
        "Frameworks & Libraries": [
            {"img": "assets/skills/numpy.png", "title": "NumPy", "level": 90},
            {"img": "assets/skills/pandas.png", "title": "Pandas", "level": 90},
        ],
        "Visualization": [
            {"img": "assets/skills/matplotlib.png", "title": "Matplotlib", "level": 85},
            {"img": "assets/skills/seaborn.png", "title": "Seaborn", "level": 80},
        ],
        "Other Tools": [
            {"img": "assets/skills/powerbi.png", "title": "Power BI", "level": 80},
            {"img": "assets/skills/excel.png", "title": "MS Excel", "level": 85},
        ]
    }

    # ---------- Render Skills Grid ----------
    for category, skills_list in skills_by_category.items():
        st.markdown(f'<div class="category-wrapper"><div class="category-title">{category}</div><div class="skills-grid">', unsafe_allow_html=True)
        for skill in skills_list:
            st.markdown(f"""
            <div class="skill-card">
                <div class="skill-icon">
                    <img src="{skill['img']}" alt="{skill['title']}">
                </div>
                <div class="skill-title">{skill['title']}</div>
                <div class="progress-container">
                    <div class="progress-bar" style="--progress-width:{skill['level']}%"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

