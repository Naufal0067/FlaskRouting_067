from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/success/<name>')
def success(name):
    return f'Selamat Datang {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('index'))  # Mengarahkan ke halaman utama

if __name__ == '__main__':
    app.run(debug=True)
