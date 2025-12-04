from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Item {self.title}>'


def create_tables():
    """Create database tables. Call this at app startup within an app context."""
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    items = Item.query.order_by(Item.id.desc()).all()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    content = request.form.get('content')
    if not title:
        return redirect(url_for('index'))
    item = Item(title=title, content=content)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Create DB tables at startup (requires app context)
    with app.app_context():
        create_tables()
    app.run(debug=True)
