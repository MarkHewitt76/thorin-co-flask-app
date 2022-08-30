"""
os module for getting IP and PORT
environment variables
"""
import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """
    Homepage view
    """
    return "Hello, World!"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
