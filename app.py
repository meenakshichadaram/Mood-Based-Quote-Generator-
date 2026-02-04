from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = {
    "Sad": [
        "This too shall pass.",
        "Be kind to yourself.",
        "Bad days don’t last forever."
    ],
    "Neutral": [
        "You’re doing okay, keep going.",
        "Balance brings clarity.",
        "One step at a time."
    ],
    "Happy": [
        "Your positivity is powerful!",
        "Keep smiling.",
        "Great energy ahead!"
    ]
}

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        sleep = int(request.form["sleep"])
        energy = int(request.form["energy"])
        stress = int(request.form["stress"])
        motivation = int(request.form["motivation"])
        focus = int(request.form["focus"])
        social = int(request.form["social"])

        total_score = sleep + energy + stress + motivation + focus + social

        if total_score <= 5:
            mood = "Sad"
        elif total_score <= 9:
            mood = "Neutral"
        else:
            mood = "Happy"

        quote = random.choice(quotes[mood])

        colors = {
            "Sad": "#f8d7da",
            "Neutral": "#fff3cd",
            "Happy": "#d4edda"
        }

        return render_template(
            "result.html",
            mood=mood,
            quote=quote,
            score=total_score,
            bg_color=colors[mood]
        )

    return render_template("quiz.html")

if __name__ == "__main__":
    app.run(debug=True)
