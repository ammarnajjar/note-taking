"""
File: app.py
Author: Ammar Najjar
Email: najjarammar@gmail.com
Github: https://github.com/najjarammar
Description: Simple Flask note taking app.
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
