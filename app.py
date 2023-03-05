from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    email = request.form['email']
    session['name'] = name
    session['email'] = email
    return redirect(url_for('show_result'))

@app.route('/result')
def show_result():
    name = session.get('name')
    email = session.get('email')
    return render_template('result.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
