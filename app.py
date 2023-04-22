from flask import Flask, render_template

app = Flask(__name__)

list = [
    {
    'id':1,
    'title':"first",
    'text':"from the first one"
    },
    {
    'id':2,
    'title':"second",
    'text':"from the second one"
    }
]


@app.route("/")
def Try():
    return render_template('home.html',list = list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)