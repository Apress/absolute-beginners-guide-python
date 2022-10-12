from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html', title="Windows 10", price="£12.99")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
