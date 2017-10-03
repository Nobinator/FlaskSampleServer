from flask import Flask, jsonify, render_template, request
from flask import json

app = Flask(__name__);

@app.route('/o')
def name():
    return "default";


# GET POST data : https://stackoverflow.com/a/25268170
@app.route('/echo')
def echo():
    return request.query_string\

@app.route('/echo1')
def echo1(): # http://127.0.0.1:5000/echo1?hello=val&va=co
    return  request.args.get("hello"); # val


@app.route('/')
def render():
    return render_template('index.html', content1 = "Hello", data = loadData())

def loadData():
    data = list();
    with open('data.txt', encoding='utf-8') as f:
        for rawline in f: data.append(rawline.strip());
    return data;

@app.route('/file')
def file():

    return loadData();

@app.route('/about')
def about():
    return "about"

@app.route('/json1')
def summary():
    data = "hello" #make_summary()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/json2')
def get_current_user():
    return jsonify(
        username="username",
        email="mail@b.com",
        id=999
    )


if __name__ == '__main__':
    app.run(debug=True)