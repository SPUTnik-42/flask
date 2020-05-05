import datetime 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template('index.html',new_year=new_year)


@app.route('/bye')
def bye():
    headline ="goodbye"
    return render_template('index.html', headline= headline)
@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return f"hello {name}"


if __name__ == "__main__":
    app.run(debug=True)

