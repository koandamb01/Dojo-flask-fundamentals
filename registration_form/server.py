from flask import Flask, render_template, request, redirect, session, flash
import datetime, re

app = Flask(__name__)
app.secret_key = "Medmed"

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def home():
    return render_template('registration.html', **session)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', **session)

@app.route('/go_back')
def go_back():
    session.clear()
    return redirect('/')

@app.route('/registration', methods=['POST'])
def registration():
    # set today date
    today = datetime.datetime.now()
    today = today.strftime('%m/%d/%Y')

    # validate firstname
    if not len(request.form['firstname']) < 1:
        if request.form['firstname'].isalpha():
            pass
        else:
            flash('*Alphabets characters only', 'firstname')
    else:
        flash('*First Name is required', 'firstname')

    # validate lastname
    if not len(request.form['lastname']) < 1:
        if request.form['lastname'].isalpha():
            pass
        else:
            flash('*Alphabets characters only', 'lastname')
    else:
        flash('*Last Name is required','lastname')

    # Validate birthday
    if len(request.form['birthday']) < 1:
        flash('*Birthday is required', 'birthday')
    
    # Validate email
    if not len(request.form['email']) < 1:
        if EMAIL_REGEX.match(request.form['email']):
            pass
        else:
            flash('*Email is invalid', 'email')
    else:
        flash('*Email is required', 'email')

    # Validate password
    if not len(request.form['password']) < 1:
        if len(request.form['password']) > 8:
            if request.form['password'] == request.form['confirm_password']:
                pass
            else:
                flash('*Password must match', 'confirm_password')
        else:
            flash('*Password must be at least 8 characters')
    elif len(request.form['confirm_password']) < 1:
        flash('*Password is required', 'password')
        flash('*Confirm_Password is required', 'confirm_password')
    else:
        flash('*Password is required', 'password')
    
    # Record form information to sessions
    session['firstname'], session['lastname'], session['birthday'], session['email'], session['password'], session['confirm_password'] = request.form.values()
    
    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/welcome')

if __name__ == '__main__':
    app.run(debug = True)