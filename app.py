from enum import unique
from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, BooleanField, ValidationError, EqualTo, Length
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/users'

# app.config['SECRET_KEY'] = ""

# db = SQLAlchemy(app)

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)

#     password_hash = db.Column(db.String(128))
    

@property
def password(self):
    raise AttributeError("Incorrect Password!")

@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)

def verify_password(self, password):
    return check_password_hash(self.password_hash, password)


def __repr__(self):
    return '<Name %r>' % self.name


class login(FlaskForm):
    name= StringField("Enter your Username", validators=[DataRequired()])
    email= StringField("Enter your Email", validators=[DataRequired()])
    password= PasswordField("Enter your Password", validators=[DataRequired(), EqualTo('password_hash2', message="Passwords Must Match!")])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit= SubmitField("Submit")
    
class Userform(FlaskForm):
    name= StringField("Enter your Username") 
    email= StringField("Enter your Email", validators=[DataRequired()])
    password= PasswordField("Enter your Password", validators=[DataRequired(), EqualTo('password_hash2', message="Passwords Must Match!")])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit= SubmitField("Submit")

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     form = Userform()
#     name_to_update = Users.query.get_or_404(id)
#     if request.method == "POST":
#         name_to_update.name = request.form["name"]
#         name_to_update.email = request.form["email"]
#         try:
#             db.session.commit()   
#             flash("User Updated Succesfully")
#             return render_template('user.html', form=form, name_to_update=name_to_update)
#         except:
#             flash('User Update Failed')
#             return render_template('user.html', form=form, name_to_update=name_to_update)
#     else:
#         return render_template('user.html', form=form, name_to_update=name_to_update)


@app.route('/')

def index():

    return render_template('main.html')

# @app.route('/user/add', methods=['GET', 'POST'])
# def add_user(name):
#     name = None
#     form = Userform()
#     if form.validate_on_submit():
#         user = Users.query.filter_by(email=form.email.data).first()
#         if user is None:
#             user = Users(name=form.name.data, email=form.email.data)
#             db.session.add(user)
#             db.session.commit()
#         name = form.name.data
#         form.name.data = ""
#         form.email.data = ""
#         form.password.data = ""
       
#         flash("User Added Successfully!")
#     our_users = Users.query.order_by(Users.date_added)
#     return render_template('user.html', form=form, name=name, our_users=our_users)

@app.route('/user/login.html', methods=['GET', 'POST'])
def name():
    name = None
    form = login()
    if form.validate_on_submit():
            name = form.name.data
            form.name.data = ""
            form.email.data = ""
            form.password_hash= ""
            flash('Log in was successful')
    
    return render_template("login.html", name=name, form=form) 

