"""
File: app.py
Author: Ammar Najjar
Email: najjarammar@gmail.com
Github: https://github.com/najjarammar
Description: Simple Flask note taking app.
"""

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
