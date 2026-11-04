
# FitBuddy AI 🏋️

### AI-Powered Personalized Fitness Plan Generator

FitBuddy AI is a web-based fitness application that helps users generate personalized 7-day workout plans based on their fitness profile, goals, and workout intensity.

## 🚀 Features

- User fitness profile management
- Personalized 7-day workout plans
- Different fitness goals
- Workout intensity selection
- Experience-level based workout suggestions
- Nutrition tips
- Workout plan feedback and updates
- User details management

## 🛠️ Technologies Used

- Python
- FastAPI
- HTML
- CSS
- Jinja2
- SQLAlchemy
- SQLite
- Google Gemini AI

## 📁 Project Structure

```text
FitBuddy-AI/
│
├── app/
│   ├── ai/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── static/
├── templates/
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── README.md
```

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd FitBuddy-AI
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
uvicorn app.main:app --reload
```

7. Open your browser:

```text
http://127.0.0.1:8000
```

## 🎯 Project Goal

To help users improve their fitness journey through personalized workout recommendations and nutrition guidance.

## 👩‍💻 Developed By

Sadhanya Saravanan

B.Sc. Artificial Intelligence and Machine Learning
