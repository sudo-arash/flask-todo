from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import secrets
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth'

# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    auth_key = db.Column(db.String(16), unique=True, nullable=False)
    todos = db.relationship('Todo', backref='author', lazy=True)

    def __init__(self, full_name):
        self.full_name = full_name
        self.auth_key = secrets.token_hex(8)  # Generates a 16-character key

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        auth_key = request.form.get('auth_key')

        if 'register' in request.form and full_name:
            user = User(full_name=full_name)
            db.session.add(user)
            db.session.commit()
            flash(f'Your login key: {user.auth_key}', 'info')
            return redirect(url_for('auth'))

        if 'login' in request.form and auth_key:
            user = User.query.filter_by(auth_key=auth_key).first()
            if user:
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Invalid login key', 'danger')

    return render_template('auth.html')

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/toggle/<int:todo_id>', methods=['POST'])
@login_required
def toggle(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return render_template('todo_item.html', todo=todo)

@app.route('/delete/<int:todo_id>', methods=['DELETE'])
@login_required
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return ''

@app.route('/item/<int:todo_id>')
@login_required
def todo_item(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if todo.user_id != current_user.id:
        abort(403)
    return render_template('todo_item.html', todo=todo)

@app.route('/api/todos', methods=['GET'])
@login_required
def get_todos():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': todo.id, 'title': todo.title, 'completed': todo.completed} for todo in todos])

@app.route('/add', methods=['POST'])
@login_required
def add_todo():
    title = request.form.get('title')
    if title:
        new_todo = Todo(title=title, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
        return '<script>location.reload(true);</script>'
    return '', 400

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth'))

if __name__ == '__main__':
    app.run(debug=True)
