from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, unique=False, default=False)


@app.route('/', methods=['GET'])
def get_task():
    if request.method == 'GET':
        allTodo = Todo.query.all()
        allTasks = []
        for singleTask in allTodo:
            allTasks.append({"sno": singleTask.sno, "task": singleTask.title, "description": singleTask.desc,
                             "status": "completed" if singleTask.status else "incomplete", "created_on": singleTask.date_created})

        return jsonify(allTasks)


@app.route('/create', methods=['POST'])
def create_task():
    if request.method == 'POST':
        title = request.json['title']
        desc = request.json['desc']
        newTodo = Todo(title=title, desc=desc)
        db.session.add(newTodo)
        db.session.commit()
        return "task created successfully"


@app.route('/delete/<int:sno>/', methods=['DELETE'])
def delete_task(sno):
    if request.method == 'DELETE':
        requiredTask = Todo.query.get_or_404(sno)
        db.session.delete(requiredTask)
        db.session.commit()
        return "task deleted successfully"


@app.route('/update/<int:sno>/', methods=['PATCH'])
def update_task(sno):
    if request.method == 'PATCH':
        requiredTask = Todo.query.get_or_404(sno)
        title = request.json['title']
        desc = request.json['desc']

        requiredTask.title = title
        requiredTask.desc = desc
        db.session.add(requiredTask)
        db.session.commit()
        return "task updated successfully"


@app.route('/markCompleted/<int:sno>/', methods=['PATCH'])
def mark_completed(sno):
    if request.method == 'PATCH':
        requiredTask = Todo.query.get_or_404(sno)
        requiredTask.status = True
        db.session.add(requiredTask)
        db.session.commit()
        return "marked as completed"


@app.route('/markIncompleted/<int:sno>/', methods=['PATCH'])
def mark_incompleted(sno):
    if request.method == 'PATCH':
        requiredTask = Todo.query.get_or_404(sno)
        requiredTask.status = False
        db.session.add(requiredTask)
        db.session.commit()
        return "marked as incompleted"


if __name__ == "__main__":
    app.run(debug=True)
