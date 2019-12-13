from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totorsssssso!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return 'User Page %s' %name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='zhiquan'))
    print(url_for('test_url_for'))
    return 'Test Page'