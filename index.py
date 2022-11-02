from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Selamat Datang di server Python Flask"


@app.route('/users')
def getUser():
    return "Get User"


if __name__ == '__main__':
    app.run(debug=False)
