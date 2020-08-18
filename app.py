from flask import Flask
from flask import url_for, escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='ycy'))
    print(url_for('user_page', name='cy'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'