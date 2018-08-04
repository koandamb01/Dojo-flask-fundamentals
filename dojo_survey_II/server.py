from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'laviedemamerecestpascommecalavie'

@app.route('/')
def index():
    return render_template('index.html', **session)

@app.route('/process', methods=['POST'])
def process():
    # validate name
    if len(request.form['name']) < 1:
        flash('*Name is required', 'name_msg')
    
    #validate location
    if len(request.form['location']) < 1:
        flash('*Location is required', 'location_msg')
    
    #validate language
    if len(request.form['language']) < 1:
        flash('*Language is required', 'language_msg')

    #validate comment:
    if len(request.form['comment']) < 1:
        flash('*Comment is required', 'comment_msg')
    
    #validate if comment is more than 120 characters
    if len(request.form['comment']) > 120:
        flash('*Comment exceeds 120 characters', 'comment_msg')

    session['name'], session['location'], session['language'], session['comment'] = request.form.values()

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html', **session)


@app.route('/go_back')
def go_back():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug = True)