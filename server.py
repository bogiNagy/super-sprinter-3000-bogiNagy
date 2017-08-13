from flask import Flask, render_template
app = Flask(__name__)


@app.route("/" or "/list")
def index():
    return "User Story Manager"


@app.route("/story")
def create():
    return render_template("main.html")


@app.route("/story/<story_id>")
def update():
    return render_template("main.html", )


if __name__ == "__main__":
    app.run()