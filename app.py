from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Привет! Это мой первый сайт на Flask!'

if __name__ == '__main__':
    app.run(debug=True)