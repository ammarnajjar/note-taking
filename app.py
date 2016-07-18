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

# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import os


class IdeaForm(Form):
     idea_name = StringField('Idea name', validators=[DataRequired()])
     submit_button = SubmitField('Add idea')


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    # in real app use Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['DATABASE_URL'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class Idea(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        idea_name = db.Column(db.String(255), unique=True)

        def __init__(self, idea_name):
            self.idea_name = idea_name

        def __repr__(self):
            return '<Idea name: %r>' % self.idea_name

    db.create_all()
    return app

app = create_app()

@app.route("/", methods=['GET', 'POST'])
def index():
    form = IdeaForm()
    submitted_idea = '<No idea submitted>'
    if form.validate_on_submit():
        idea = Idea(form.idea_name.data)
        db.session.add(idea)
        db.session.commit()
    # list_of_ideas = Idea.query.all()
    list_of_ideas = Idea.query
    return render_template('index.html', form=form, list_of_ideas=list_of_ideas)

if __name__ == "__main__":
    app.run(debug=True)
