from flask import Flask, render_template, session
from data.forms import Passwords
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_!*&$^#%%^&*#%^!%T'


@app.route('/')
def index():
    return render_template('index.html', title="Главная")


@app.route('/generator', methods=['GET', 'POST'])
def pass_gen():
    password_object = Passwords()
    chars = '+-/*!&$#?=@<>_'
    letters_number = password_object.length.data
    passwords_number = password_object.count.data
    password_chars = string.ascii_letters + string.digits + string.ascii_letters.upper() + chars
    passwords = []
    rand = random.SystemRandom()
    for n in range(passwords_number):
        password = ''
        for i in range(letters_number):
            password += rand.choice(password_chars)
        passwords.append(password)
    return render_template('pass.html', passwords=passwords, password_object=password_object)



if __name__ == '__main__':
    app.run()
