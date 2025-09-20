import streamlit as st
import time

# ----------------- Skills Page -----------------
def skills():
    st.markdown('<h2 id="skills" class="section-title">🛠 Skills</h2>', unsafe_allow_html=True)

    # Custom CSS for cards
    st.markdown("""
    <style>
    .skill-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: inline-block;
        vertical-align: top;
        width: 300px;
    }
    .skill-card:hover {
        transform: translateY(-8px);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
    }
    .skill-icon {
        font-size: 30px;
        margin-bottom: 10px;
    }
    .skill-title {
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 5px;
    }
    .skill-desc {
        font-size: 14px;
        color: #333;
        margin-bottom: 10px;
    }
    .progress-container {
        background-color: #e0e0e0;
        border-radius: 10px;
        overflow: hidden;
        height: 15px;
        margin-bottom: 10px;
    }
    .progress-bar {
        height: 15px;
        background: linear-gradient(90deg, #3f2b96, #a8c0ff);
        width: 0%;
        transition: width 1.5s ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)

    # ----------------- Skill Cards -----------------
    skill_data = [
        {"icon": "🐍", "title": "Languages", "desc": "Python, SQL", "level": 95},
        {"icon": "🤖", "title": "AI/ML", "desc": "ML, Deep Learning (ANN, CNN, RNN, LSTM, GRU), NLP, LLMs, CV, Transformers, Image Processing, Statistics", "level": 90},
        {"icon": "🧠", "title": "GenAI & NLP", "desc": "OpenAI GPT, Hugging Face Transformers, LangChain, Vector DB, NLTK, SpaCy", "level": 85},
        {"icon": "🗄️", "title": "Databases", "desc": "MySQL, PostgreSQL, MongoDB", "level": 80},
        {"icon": "⚙️", "title": "MLOps", "desc": "Docker, Kubernetes, MLflow, Statistical Modeling, CI/CD Pipelines", "level": 80},
        {"icon": "☁️", "title": "Cloud & Tools", "desc": "Git, Hugging Face Spaces, Jupyter, VS Code, Colab, AWS, Azure", "level": 75},
        {"icon": "🌐", "title": "Web Tech", "desc": "Django, Flask, RESTful API", "level": 70},
        {"icon": "🛠️", "title": "Frameworks & Libraries", "desc": "TensorFlow, PyTorch, OpenCV, Scikit-learn, Keras, NumPy, Pandas, Matplotlib, Seaborn, OpenAI APIs", "level": 90},
        {"icon": "📊", "title": "Other Tools", "desc": "Power BI, MS Excel", "level": 85}
    ]

    st.markdown('<div style="display:flex; flex-wrap:wrap;">', unsafe_allow_html=True)

    for skill in skill_data:
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{skill['icon']}</div>
            <div class="skill-title">{skill['title']}</div>
            <div class="skill-desc">{skill['desc']}</div>
            <div class="progress-container">
                <div class="progress-bar" id="{skill['title'].replace(' ', '_')}"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ----------------- Animate Progress Bars -----------------
    animate_script = "<script>"
    for skill in skill_data:
        animate_script += f"""
        var bar = document.getElementById('{skill['title'].replace(' ', '_')}');
        bar.style.width = '{skill['level']}%';
        """
    animate_script += "</script>"

    st.markdown(animate_script, unsafe_allow_html=True)
