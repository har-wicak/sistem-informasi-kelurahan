from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', page_title = "Web Kelurahan KKN")
    else:
        return "Unsupported Request Method"

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html', page_title = "Web Kelurahan KKN")
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