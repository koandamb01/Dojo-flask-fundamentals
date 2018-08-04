from flask import Flask, render_template, redirect, request as req, session, flash
import re

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# create a regular expression object that we can use run operations oncopy
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    
    # validations for name!
    if len(req.form['name']) < 1:
        flash("Name is required", 'name')
    else:
        flash(f"Success! your name is {req.form['name']}", 'name')
    
    # validation for email
    if len(req.form['email']) < 1:
        flash("Email is required", 'email')
    
    elif not EMAIL_REGEX.match(req.form['email']):
        flash("invalid email address", 'email')
    else:
        flash(f"Success! your is {req.form['email']}", 'email')
    

    # check if error exits or not
    if '_flashes' in session.keys():
        return redirect('/')
    else:
        pass
        # redirect to a diffirent route
        # return redirect("/success")

if __name__=="__main__":
    app.run(debug=True)