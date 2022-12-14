"""
os module for handling IP, PORT and other environment variables.
json library for handling json files.
flask library: Flask and render_template for handling routes and views,
request module for handling form data, flash function for flashed messages.
"""
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
"""
gets the SECRET_KEY environment variable
"""
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    """
    Homepage view
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    About page view
    """
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    """
    Individual company member view
    """
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Contact Page view
    """
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


@app.route("/careers")
def careers():
    """
    Careers Page view
    """
    return render_template("careers.html", page_title="Come Work With Us!")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
