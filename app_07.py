from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def news():
    context = [
        {'name': 'Китай в третий раз запустил военный многоразовый космический самолет'},
        {
            'description':
                '14 декабря Китай в третий раз запустил свой'
                ' многоразовый космический самолет, соблюдая строгую секретность.'
                ' Корабль был запущен с помощью ракеты Чанчжэн-2F, которая взлетела с космодрома'
                ' Цзюцюань в пустыне Гоби.'},
        {'date': '14-12-2023',
         }
    ]
    return render_template('news.html', news=context)


if __name__ == '__main__':
    app.run()
