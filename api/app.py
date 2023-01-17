from flask import Flask, render_template
from api import templates

app = Flask(__name__)
app.secret_key = 'andreluizsilv2960'

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

