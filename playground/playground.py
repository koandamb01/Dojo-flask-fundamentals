from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html', times=3)

@app.route('/play/<num>')
def playTimes(num):
    num = int(num)
    return render_template('play.html', times=num)


@app.route('/play/<num>/<col>')
def playTimesColor(num, col):
    num = int(num)
    return render_template('play.html', times=num, color=col)




if __name__ == '__main__':
    app.run(debug = True)

