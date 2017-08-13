from flask import Flask, render_template
app = Flask(__name__)


@app.route("/" or "/list")
def index():
    return render_template("list.html")


@app.route("/story")
def create():
    return render_template("form.html")


@app.route("/story/<story_id>")
def update():
    return render_template("form.html", )


if __name__ == "__main__":
    app.run()