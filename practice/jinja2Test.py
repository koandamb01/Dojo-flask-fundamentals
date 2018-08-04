from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    student_info = (
        {'name': 'Mohamed', 'age': 23},
        {'name': 'Moussa', 'age': 50},
        {'name': 'Ali', 'age': 52},
        {'name': 'Habibou', 'age': 53}
    )
    return render_template("index.html", students=student_info)

if __name__ == "__main__":
    app.run(debug = True)