from flask import Flask, render_template

from flask_bootstrap import Bootstrap5



from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print("Form submitted")
        print(f"Email: {login_form.email.data}")
        print(f"Password: {login_form.password.data}")
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            print("Login successful")
            return render_template('success.html')
        else:
            print("Login failed")
            return render_template('denied.html')
    else:
        print("Form not submitted or validation failed")
        print(login_form.errors)
    return render_template('login.html', form=login_form)
if __name__ == '__main__':
    app.run(debug=True)
