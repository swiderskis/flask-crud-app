from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_completed = db.Column(db.DateTime, default=None)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return redirect('/error')

    else:
        tasks = Todo.query.filter_by(completed=False).order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/completed_tasks')
def completed_tasks():
    tasks = Todo.query.filter_by(completed=True).order_by(Todo.date_created).all()
    return render_template('completed_tasks.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return redirect('/error')

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')

        except:
            return redirect('/error')

    else:
        return render_template('update.html', task=task)

@app.route('/mark_complete/<int:id>', methods=['POST', 'GET'])
def mark_complete(id):
    task_to_complete = Todo.query.get_or_404(id)
    task_to_complete.completed = True
    task_to_complete.date_completed = datetime.utcnow()

    try:
        db.session.commit()
        return redirect('/')
        
    except:
        return redirect('/error')
        

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)