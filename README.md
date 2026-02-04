Mood-Based Quote Generator

A Python Flask web application that provides personalized motivational quotes based on the user’s current mood. The app evaluates mood from simple inputs like sleep, energy, stress, motivation, focus, and social interaction.

📝 Project Description

This application helps users discover their mood and receive an encouraging quote to lift their spirits. It uses a scoring system to classify moods as Sad, Neutral, or Happy, then displays a quote corresponding to that mood. The user interface is simple, clean, and interactive.

Key Objectives:

Assess the user’s mood based on their daily experiences.

Show a motivational quote tailored to the mood.

Use a simple and friendly web interface.

💡 How It Works

Mood Quiz Input:
Users answer six questions about:

Sleep quality

Energy level

Stress level

Motivation

Focus

Social interaction

Each answer is scored numerically:

0 = low/negative

1 = medium/neutral

2 = high/positive

Mood Scoring Logic:
The total score is calculated by summing all six responses:

total_score = sleep + energy + stress + motivation + focus + social


Mood classification is done based on total score:

Sad: total_score ≤ 5

Neutral: 6 ≤ total_score ≤ 9

Happy: total_score ≥ 10

Quote Selection:
Each mood has a list of predefined motivational quotes stored in a Python dictionary:

quotes = {
    "Sad": ["This too shall pass.", ...],
    "Neutral": ["You’re doing okay, keep going.", ...],
    "Happy": ["Your positivity is powerful!", ...]
}


A random quote from the corresponding mood list is displayed.

Dynamic Result Display:
The result page shows:

The user’s mood

The total score

A random motivational quote

A background color corresponding to the mood for a better visual experience

🖥️ File Structure
mood-quote-generator/
│
├── app.py              # Main Flask app containing all the backend logic
├── templates/
│   ├── quiz.html       # Mood quiz page with input questions
│   └── result.html     # Displays mood, score, and a quote
└── README.md           # Documentation (this file)

🔧 Code Explanation
1. app.py

Imports required modules: Flask, render_template, request, random.

Defines a dictionary of quotes for each mood.

Sets up a Flask app and handles GET/POST requests:

GET request: displays the quiz form.

POST request: calculates total score, determines mood, selects a quote, and renders the result page.

total_score = sleep + energy + stress + motivation + focus + social

if total_score <= 5:
    mood = "Sad"
elif total_score <= 9:
    mood = "Neutral"
else:
    mood = "Happy"

quote = random.choice(quotes[mood])

2. quiz.html

HTML page with a simple form asking six mood-related questions.

Each question has a <select> dropdown with three options (0–2).

Form submits data via POST to the Flask app.

Includes CSS styling for a clean, centered layout.

3. result.html

Displays the user’s mood, score, and quote dynamically using Jinja2 templating:

<p class="mood">Mood: {{ mood }}</p>
<p>Score: {{ score }}</p>
<p class="quote">“{{ quote }}”</p>


Background color changes based on the mood to give visual feedback:

Sad → Light red (#f8d7da)

Neutral → Light yellow (#fff3cd)

Happy → Light green (#d4edda)

⚡ How to Run Locally

Clone the repository:

git clone https://github.com/your-username/mood-quote-generator.git
cd mood-quote-generator


Install Flask:

pip install flask


Run the app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000

🌟 Features

Mood detection using simple scoring

Dynamic quote display based on mood

Friendly, clean UI

Color-coded feedback for mood visualization

Randomized quotes for variety
