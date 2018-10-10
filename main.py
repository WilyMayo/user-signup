from flask import Flask, render_template, redirect, request
import string


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('web.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

@app.route('/', methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    spiderman = True

    if characters_need(username) == False:
        username_error = 'username not valid'
        spiderman = False

    if No_spaces(username) == False:
        username_error = 'no way'
        spiderman = False    

    if password_wrong(password, verify) == False:
        password_error = 'Not matching'
        spiderman = False

    if characters_need(password) == False:
        password_error = 'password not valid'
        spiderman = False

    if No_spaces(password) == False:
        password_error = 'password not valid'
        spiderman = False

    if characters_need(email) == False:
        email_error = 'You Need More Characters'
        spiderman = False 


    if email_valid(email) == False:
        email_error = 'email not cool'
        spiderman = False

    if spiderman == True:
        return redirect('/welcome?username={0}'.format(username))          

    return render_template('web.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
      
    

def No_spaces(text):
    if " " in text:
        return False
       

def characters_need(text):
    if len(text) < 3 or len(text) > 20:
        return False


def password_wrong(a, b):
    if a != b:
        return False


        
def email_valid(text):
    if '@' in text and '.' in text :
        return True
    else:
        return False    
     
        






app.run()
    