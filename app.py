from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

#where the database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#Database
db = SQLAlchemy(app)

#Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"

@app.route("/", methods = ['GET', 'POST'])
def todo():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            print('Error while adding task!')
        
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks= tasks)


if __name__ == "__main__":
    with app.app_context():   
        db.create_all()
    app.run(debug=True)