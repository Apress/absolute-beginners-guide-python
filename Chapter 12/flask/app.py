from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a Flask Web App'

@app.route('/shop')
def shop():
    return 'This is the shop page'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
