from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! My first web app is running!"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! "

@app.route('/about')
def about():
    return "This is the About Page. Welcome to Flask learning!"

if __name__ == '__main__':
    app.run(debug=True)
