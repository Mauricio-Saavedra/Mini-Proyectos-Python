from flask import Blueprint, render_template, redirect, request, url_for, g
# from flask_login import login_required
from todor.auth import login_required
from .models import Todo, User
from todor import db

# El 1er parametro es el nombre del BP, en este caso [todo].
# El 2do parametro es la localización del archivo, en este caso [__name__] hace referencia a sí mismo.
# El 3er parametro hace referencia a la URL base de las siguientes vistas; si tomamos como ejemplo la siguiente ruta quedaría así: [ /todo/list ]
bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
@login_required
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos = todos)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(g.user.id, title, desc)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo

@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    todo = get_todo(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else False

        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/update.html', todo=todo)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))
