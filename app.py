"""
File: app.py
Author: Ammar Najjar
Email: najjarammar@gmail.com
Github: https://github.com/ammarnajjar
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

app = Flask(__name__)
# in real app use Flask-Appconfig
app.config['SECRET_KEY'] = 'devkey'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_CHANGE_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL'] = False
app.config['SECRET_FLASH_MESSAGES'] = True

Bootstrap(app)
db = SQLAlchemy(app)

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idea_name = db.Column(db.String(140))

    def __init__(self, idea):
        self.idea_name = idea

    def __repr__(self):
        return '<Idea : %r>' % self.id

db.create_all()


@app.route("/", methods=['GET', 'POST'])
def index():
    form = IdeaForm()
    if form.validate_on_submit():
        idea = Idea(form.idea_name.data)
        db.session.add(idea)
        db.session.commit()
    # list_of_ideas = Idea.query.all()
    list_of_ideas = Idea.query
    return render_template('index.html', form=form, list_of_ideas=list_of_ideas)

if __name__ == "__main__":
    app.run(debug=True)
