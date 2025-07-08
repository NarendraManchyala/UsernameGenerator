from flask import Flask, render_template, request
import random as rd

app = Flask(__name__)

def generate_username(choice, first_name="", last_name="", nick_name=""):
    if choice == "1":  # Professional
        return "_".join([first_name, last_name])
    elif choice == "2":  # Gamer
        number = str(rd.randint(10, 99))
        return "_".join([nick_name, number])
    elif choice == "3":  # Fun
        words = ["cool", "happy", "fast", "enjoy", "blue", "sun", "cat", "star", "sky"]
        word1 = rd.choice(words)
        word2 = rd.choice(words)
        number = str(rd.randint(100, 999))
        return "_".join([word1, word2, number])
    elif choice == "4":  # Anonymous
        letters = "abcdefghijklmnopqrstuvwxyz1234567890"
        return "user_" + ''.join(rd.choice(letters) for _ in range(6))
    else:
        return "Invalid Choice"

@app.route("/", methods=["GET", "POST"])
def index():
    username = ""
    if request.method == "POST":
        choice = request.form.get("choice")
        first_name = request.form.get("first_name", "")
        last_name = request.form.get("last_name", "")
        nick_name = request.form.get("nick_name", "")
        username = generate_username(choice, first_name, last_name, nick_name)
    return render_template("index.html", username=username)

if __name__ == '__main__':
    app.run(debug=True)
