from flask import Flask, render_template, redirect, url_for
from game_of_life import *

from forms import SizeForm


app = Flask(__name__)

app.config.from_mapping({'SECRET_KEY': 'dfgdfg'})


@app.route('/', methods=['get', 'post'])
def index():
    """Задание размера мира и его инициализация"""
    form_size = SizeForm()
    if form_size.validate_on_submit():
        width = form_size.width.data
        height = form_size.height.data

        GameOfLife(width, height)
        return redirect('/')
    return render_template('index.html', form_size=form_size)


@app.route('/live')
def live():
    """Присвоение переменной life раннее созданного мира и отправка в шаблон live.html"""
    life = GameOfLife()

    if life.counter > 0:
        life.form_new_generation()  # Генерация следующего поколения

    life.counter += 1
    return render_template('live.html', life=life)


if __name__ == '__main__':
    app.run(host='127.0.0.0', port=5000, debug=True)
