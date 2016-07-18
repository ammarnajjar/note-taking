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

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IdeaForm(Form):
     idea = StringField('Idea', validators=[DataRequired()])
     submit_button = SubmitField('Add idea')

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    # in real app use Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    return app

app = create_app()

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = IdeaForm()
    submitted_idea = '<No idea submitted>'
    if form.validate_on_submit():
        submitted_idea = form.idea.data
    return render_template('index.html', form=form, submitted_idea=submitted_idea)

if __name__ == "__main__":
    app.run(debug=True)
