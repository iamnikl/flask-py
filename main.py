from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route("/")
def startPage():
    return render_template("index.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)