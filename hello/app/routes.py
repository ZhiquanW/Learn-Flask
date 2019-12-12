from app import app
from flask import render_template
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
