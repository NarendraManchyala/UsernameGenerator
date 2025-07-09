from flask import Blueprint,render_template, request
from UsernameGenerator import generate_username

bp = Blueprint("main",__name__)

@bp.route("/", methods=["GET","POST"])
def index():
    usernames = []
    if request.method == "POST":
        choice = request.form.get("choice")
        first_name = request.form.get("first_name", "")
        last_name = request.form.get("last_name", "")
        nick_name = request.form.get("nick_name", "")
        usernames = generate_username(choice, first_name, last_name, nick_name)
    return render_template("index.html",usernames=usernames)