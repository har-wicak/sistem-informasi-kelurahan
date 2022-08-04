from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', page_title = "Web Kelurahan KKN")
    else:
        return "Unsupported Request Method"

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html', page_title = "Dashboard")
    else:
        return "Unsupported Request Method"

@app.route('/articles', methods=['GET', 'POST'])
def articles():
    if request.method == 'GET':
        return render_template('articles.html', page_title = "Articles")
    else:
        return "Unsupported Request Method"

@app.route('/profil', methods=['GET', 'POST'])
def profil():
    if request.method == 'GET':
        return render_template('profil.html', page_title = "Profil")
    else:
        return "Unsupported Request Method"

@app.route('/article', methods=['GET', 'POST'])
def article():
    if request.method == 'GET':
        return render_template('ind_article.html', page_title = "Article")
    else:
        return "Unsupported Request Method"

# @app.route('/pemerintahan')
# def pemerintahan():
#     return render_template('pemerintahan.html', page_title = "Laman Pemerintahan Desa")

# @app.route('/profil')
# def profil():
#     return render_template('profil.html', page_title = "Profil Desa")

# @app.route('/kontak')
# def kontak():
#     return render_template('kontak.html', page_title = "Kontak Kami")

if __name__ == "__main__":
    app.run(debug=True)