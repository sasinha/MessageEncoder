from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/operate.html', methods=['POST'])
def operate():
    plain_input = request.form['plain']
    return plain_input



if __name__ == "__main__":
    app.debug = True
    app.run()

