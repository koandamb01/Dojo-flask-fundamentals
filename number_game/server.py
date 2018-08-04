from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'laviedemamerecestpascommecalavie'

@app.route('/')
def index():
    #check if session exits
    if bool(session):
        # session exits
        pass
    else:
        # no session
        session['try'] = 0
        session['guess_number'] = random.randrange(1, 101)

    print(session)
    return render_template('index.html', **session)

@app.route('/check', methods = ['POST'])
def check():
    # increment the number of user guesses
    session['try'] += 1
    guess = int(request.form['user_number'])
    print("user guess: ", guess)

    # check if the user guess the right number
    if guess == session['guess_number']:
        session['answer'] = 'right'
    else:
        session['answer'] = 'wrong'

        #check if the user guess is too low/high
        if guess > session['guess_number']:
            session['hint'] = 'Too high!'
        else:
            session['hint'] = 'Too low!'
    
    #redirect information to home route
    return redirect('/')


@app.route('/replay')
def replay():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug = True)