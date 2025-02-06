from flask import Flask, jsonify, request
from app.database import add_task, get_tasks

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def fetch_tasks():
    return jsonify(get_tasks())

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = add_task(data)
    return jsonify(new_task), 201
