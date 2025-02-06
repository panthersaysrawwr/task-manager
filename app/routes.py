from flask import Flask, jsonify

app = Flask(__name__)  # Create the Flask app

tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Use Git Properly", "done": False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)
