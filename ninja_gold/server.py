from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = 'laviedemamerecetcommecalavie'

@app.route('/')
def index():

    # check if the activites key exits in session dictionary
    if bool(session) :
        pass # acitivities key exits
    else:
        # no activities key, so create one
        session['gold_earn'] = 0
        session['activities'] = []

    return render_template('index.html', **session)

@app.route('/process_money', methods=['POST'])
def process_money():
    # Set the date and time
    today = datetime.datetime.now()
    today = today.strftime('%Y/%m/%d %X %p')

    # record which house user play
    building = request.form['building']

    # check if user choose farm
    if building == 'farm':
        session['result'] = 'win'
        farm = random.randrange(10, 21) # farm random number 10 - 20
        session['gold_earn'] += farm
        session['activities'].append("<p class='text-success'>Earned " + str(farm) + " goals from the farm! (" + today + ")</p>")
    # check if user choose cave
    elif building == 'cave':
        session['result'] = 'win'
        cave = random.randrange(5, 10) # cave random number 5 - 10
        session['gold_earn'] += cave
        session['activities'].append("<p class='text-success'>Earned " + str(cave) + " goals from the cave! (" + today + ")</p>")

    # check if user choose house
    elif building == 'house':
        session['result'] = 'win'
        house = random.randrange(2, 5) # house random number 2 - 5
        session['gold_earn'] += house
        session['activities'].append("<p class='text-success'>Earned " + str(house) + " goals from the house! (" + today + ")</p>")

    # check if user choose casino
    else:
        session['result'] = 'lost'
        temp = session['gold_earn']
        casino = random.randrange(-50, 50) # casino random number 10 - 20

        if casino == 0:
            session['activities'].append("<p class='text-warning'>Earned " + str(casino) + " goals from the casino! (" + today + ")</p>")
        # casino is a negative
        elif casino < 0:
            temp += casino
            casino = session['gold_earn'] - temp
            session['gold_earn'] = temp
            session['activities'].append("<p class='text-danger'>Earned a casino and lost " + str(casino) + " goals... Ouch! (" + today + ")</p>")

        # casino is a positive
        else:
            session['gold_earn'] += casino
            session['activities'].append("<p class='text-success'>Earned " + str(casino) + " goals from the casino! (" + today + ")</p>")

    return redirect('/') 

if __name__ == '__main__':
    app.run(debug = True)

