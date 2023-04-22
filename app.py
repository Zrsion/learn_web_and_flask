from flask import Flask, render_template, jsonify

app = Flask(__name__)

list = [
    {
    'id':1,
    'title':"first",
    'text':'from the first one',
    'value':"100"
    },
    {
    'id':2,
    'title':"second",
    'text':"from the second one",
    'value':"200"
    }
]


@app.route("/")
def Try():
    return render_template('home.html',list = list)

@app.route("/list")
def list_json():
    return jsonify(list)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)