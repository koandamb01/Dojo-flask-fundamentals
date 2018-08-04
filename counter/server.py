from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'laviedemamerecestpascommecalavie'

@app.route('/')
def index():
    if bool(session):
        # session already has a key
        session['counter'] += 1
    else:
        # no session key yet
        print("no keys")
        session['counter'] = 1
    print('session: ', session)
    return render_template('index.html', **session)

@app.route('/two')
def two():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)