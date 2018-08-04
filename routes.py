from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is

# The "@" symbol designates a "decorator" which attaches the following
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
@app.route('/')
def index():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name 

@app.route('/repeat/<num>/<word>')
def times(num, word):
    output = ""
    for i in range(1, int(num)+1):
        output += word + " "
    return output

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
