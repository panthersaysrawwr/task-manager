from flask import Flask
from app.routes import app

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Task Manager API!"

if __name__ == '__main__':
    app.run(debug=True)
