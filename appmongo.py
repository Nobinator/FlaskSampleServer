from flask import Flask;
from flask_pymongo import PyMongo

app = Flask(__name__);
app.config['MONGO_DBNAME'] = "flasko";
app.config['MONGO_URI'] = 'mongodb://Flasko:Flasko@ds163034.mlab.com:63034/flasko'

mongo = PyMongo(app);

@app.route('/add')
def add():
    # Если коллекции .users нету, то она добавиться автоматически
    user = mongo.db.users
    user.insert({'name' : 'Kir'})
    return 'Added user'

if __name__ == '__main__':
    app.run(debug=True)