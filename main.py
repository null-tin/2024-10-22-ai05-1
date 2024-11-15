from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'name':'ケイスケ', 'age':22},
        {'name':'ダイキ', 'age':25},
        {'name':'セイジ', 'age':18},
    ]
    return render_template(
            'users.html',
            users=users)

@app.route('/page')
def page():
    users = [
        {'name':'ケイスケ', 'age':22},
    ]
    return render_template(
            'users.html',
            users=users)

@app.route('/page2')
def page2():
    users = [
        {'name':'ダイキ', 'age':25},
    ]
    return render_template(
            'users.html',
            users=users)

@app.route('/page3')
def page3():
    users = [
        {'name':'セイジ', 'age':18},
    ]
    return render_template(
            'users.html',
            users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
