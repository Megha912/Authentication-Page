import pyrebase
from flask import *

app = Flask(__name__)
#add your firebase account keys 
#refer readme file how to get it
config = {
    'apiKey': "AIzaSyBMwykFldUr12v0U2DNt6vUtj2By7ezPwU",
    'authDomain': "pr301-c0e5d.firebaseapp.com",
    'databaseURL': "https://pr301-c0e5d.firebaseio.com",
    'projectId': "pr301-c0e5d",
    'storageBucket': "pr301-c0e5d.appspot.com",
    'messagingSenderId': "541325376379",
    'appId': "1:541325376379:web:222ebce3a89bdd63535bde",
    'measurementId': "G-7ESQRVSYWT"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


@app.route('/', methods=['GET', 'POST'])
def index():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('index.html', s=successful)
        except:
            return render_template('index.html', us=unsuccessful)

    return render_template('index.html')


@app.route('/signup_form', methods=['GET', 'POST'])
def signup_form():
    unsuccessful = 'Please check your credential'
    successful = 'verification link send to your email'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken'])
            return render_template('inex.html', s=successful)
        except:
            return render_template('index.html', us=unsuccessful)
    return render_template('signup.html')

@app.route('/forget_form', methods=['GET', 'POST'])
def forget_form():
    unsuccessful = 'Please check your email'
    successful = 'reset link send to your email'
    if request.method == 'POST':
        email = request.form['mail']
        try:
            user = auth.send_password_reset_email(email)
            return render_template('index.html', s=successful)
        except:
            return render_template('index.html', us=unsuccessful)
    return render_template('forget.html')

if __name__ == '__main__':
    app.run()
