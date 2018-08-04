from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'laviedemamerecestpascommecalavie'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def results():
    content = {
        'name': session['name'],
        'location': session['location'],
        'language': session['language'],
        'comment': session['comment']
    }
    return render_template('result.html', **content)

if __name__ == '__main__':
    app.run(debug = True)