import datetime 
from flask import Flask, render_template,request, session
from flask_session import Session 

app = Flask("__name__")


notes = []

@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template('index.html',new_year=new_year)


@app.route('/name')
def names():
    names = ['ushnik','utpal','mousumi','ushniha']
    return render_template('index.html', names = names )

@app.route('/bye')
def bye():
    headline ="goodbye"
    return render_template('index.html', headline= headline)

@app.route('/more')
def more():
    return render_template('more.html')

@app.route('/hello', methods=["GET","POST"] )
def hello():
    if request.method == "GET" :
        return "PLEASE SUBMIT THE FORM FROM /more"
    else:   
        name = request.form.get("name")
        return render_template('hello.html', name=name )

@app.route('/notes', methods =['GET','POST'])
def mnotes(): 
    if request.method == 'POST':
        note = request.form.get('note')
        notes.append(note)
    return render_template('monotes.html',notes = notes)





if __name__ == "__main__":
    app.run(debug=True)

