from flask import Flask 
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return '<h1>Mohamed First Flask server yeahhh!</h1>'


def hello_world():
    return 'Hello World!'
if __name__=="__main__":
    app.run(debug=True)
