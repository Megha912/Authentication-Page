import pyrebase

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

email = input("enter your email\n")
password = input("enter your password\n")
user = auth.create_user_with_email_and_password(email, password)
