from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5


app = Flask(__name__)

Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about, methods=['GET']")
def about():
    return render_template("about.html")

@app.route("/contact, methods=['GET', 'POST']")
def contact():
    return render_template("contact.html")





if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")
