from flask import Flask, render_template, request,url_for,redirect,flash,send_from_directory
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager,login_user,login_required,current_user,logout_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)


# CONFIGURE FLASK-APP TO USE FLASK-LOGIN 
# table creation in the DATABASE
login_manager = LoginManager()
login_manager.init_app(app)

# configuring the table
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))




# CREATING INSYDER DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///insyder.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine("mysql+pymysql://user:pw@host/db", pool_pre_ping=True)


#CREATING A DATABASE(TABLE) FOR THE REGISTRATION(SIGN UP) PROCESS
# registeration table
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40), nullable = False)
    lastname = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40),nullable = False, unique=True)
    password = db.Column(db.String(30),nullable=False)
db.create_all()


# new_user = User(firstname="",lastname="",email="",password="")
# db.session.add(new_user)
# db.session.commit()

# THE SECRET KEY TO ACTIVATE WTFORM
app.secret_key = "My-Name-is"

# INDEX ROUTE
@app.route("/")
def index_page():
    return render_template("home.html")



# REGISTER FORM INHERITANCE
# form for the registration process
class RegisterForm(FlaskForm):
    firstname = StringField(label='Firstname',validators=[DataRequired()])
    lastname = StringField(label='Lastname',validators=[DataRequired()])
    email = StringField(label='Email',validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label='Register')

#REGISTER ROUTE
@app.route("/register",methods=["POST","GET"])
def register_page():

    form = RegisterForm()
    # register_form.validate_on_submit()
   

    if request.method == "POST":
        # TO CHECK IF RECORDS ALREADY IN DATABASE
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You've already Signed up with that email,Please log in Instead")
            return redirect(url_for('login_page'))

        # HASHING AND SALTING FOR AUTHENTICATION
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method = 'pbkdf2:sha256',
            salt_length = 8


        )
        # GETTING THE NEW_USER TO THE DATABADE 
        new_user = User(
            firstname = request.form.get('firstname'),
            lastname = request.form.get('lastname'),
            email = request.form.get('email'),
            password = hash_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()


        login_user(new_user)
        return redirect(url_for('secrets_page'))

    return render_template('register.html',form=form, logged_in=current_user.is_authenticated)







# LOGIN FORM INHERITANCE
# form for the login process
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label= 'Password',validators=[DataRequired()])
    submit = SubmitField(label='Log In')

# LOGIN ROUTE
@app.route("/login", methods=["POST","GET"])
def login_page():

    login_form = LoginForm()
    login_form.validate_on_submit()
    form=login_form



    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # CHECK FOR ERROR
        user = User.query.filter_by(email=email).first()
        # IF USER(NAME) IS INCORRECT
        if not user:
            flash("That email does not exist,Please try again")
            return redirect(url_for('login_page'))
            # PASSWORD INCORRECT
        elif not check_password_hash(user.password,password):
            flash("Incorrect Passord,Please Enter Correct Password")
            return redirect(url_for('login_page'))
            # BOTH ARE CORRECT
        else:
            login_user(user)
            return redirect(url_for('secrets_page'), 302)
    return render_template("login.html", login_form = LoginForm(), form=login_form, logged_in=current_user.is_authenticated)


@app.route("/mainz")
def mainz():
    return render_template("welcome.html")
     
@app.route("/secrets")
@login_required
def secrets_page():
    print(current_user.firstname)
    return render_template("login_welcome.html", name=current_user.firstname ,logged_in=True)



    
if __name__ == "__main__":
    app.run(debug=True)

# https://python.plainenglish.io/implementing-flask-login-with-hash-password-888731c88a99