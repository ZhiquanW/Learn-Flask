from flask import render_template
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'zhiquan'}
    posts = [{
        'author': {'username': 'zhiquan0'},
        'body': 'beautiful day in Portaland'
    },
        {
        'author': {'username': 'Susan'},
        'body': "the aaasdasd"
    }
    ]
    return render_template('index.html', user=user,postss=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign in',form = form)
    # return render_template('base.html')