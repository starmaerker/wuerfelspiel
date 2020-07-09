from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from random import randrange

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    result = randrange(1, 7)
    url = f'../static/img/wuerfel{result}.png'
    return render_template('index.html', url=url)


if __name__ == '__main__':
    app.run()
