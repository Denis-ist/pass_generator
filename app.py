from random import choice
from flask import Flask, render_template, request
from data.forms import Passwords

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_!*&$^#%%^&*#%^!%T'


@app.route('/')
def index():
    return render_template('index.html', title="Главная")


@app.route('/generator', methods=['GET', 'POST'])
def pass_gen():
    password_object = Passwords()
    if password_object.validate_on_submit():
        numbers = '1234567890'
        chars = '+-/*!&$#?=@<>_'
        letters = 'abcdefghijklnopqrstuvwxyz'
        password_chars = numbers + chars + letters + letters.upper()
        passwords = []
        for n in range(password_object.count.data):
            password = ''
            for i in range(password_object.length.data):
                password += choice(password_chars)
            passwords.append(f'{n + 1}: {password}')
        print(passwords)
        return render_template('pass.html', passwords=passwords, password_object=password_object)
    return render_template('pass.html', password_object=password_object)


if __name__ == '__main__':
    app.run()
