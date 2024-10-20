from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'andreluizsilv'

# Data de nascimento
data_nascimento = datetime(1976, 3, 11)


@app.route('/')
def index():
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    return render_template('index.html', idade=idade)


if __name__ == '__main__':
    app.run(debug=False)
