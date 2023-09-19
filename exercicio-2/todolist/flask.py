from flask import Flask, request, Response
from .model import TodoItem, db
import os

app = Flask(__name__)

def getenv(name: str) -> str:
    val = os.getenv(name)
    if val is None:
        raise ValueError('Missing environment variable {}'.format(name))

@app.before_first_request
def create_tables():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.init_app(app)
    with app.app_context():
        db.create_all()

@app.route('/')
def list_todos():
    todos = db.session.query(TodoItem).all()
    todos_list = [todo.as_dict() for todo in todos]
    print(todos_list)
    todos_list = sorted(todos_list, key=lambda t: t['done'], reverse=True)
    return {'todos': todos_list}

@app.route('/criar', methods=['POST'])
def criar_todo():
    texto = request.form['texto']
    todo = TodoItem(text=texto)
    db.session.add(todo)
    db.session.commit()
    return todo.as_dict()

@app.route('/pronto/<int:todo_id>')
def pronto_todo(todo_id):
    item = db.session.query(TodoItem).filter_by(id=todo_id).one_or_none()
    if not item:
        return Response({'msg': 'missing todo item'}, status=404)
    item.done = True
    db.session.commit()
    return {'msg': 'ok'}
