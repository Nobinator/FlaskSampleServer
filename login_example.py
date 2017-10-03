from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flasko'
app.config['MONGO_URI'] = 'mongodb://Flasko:Flasko@ds163034.mlab.com:63034/flasko'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session: #Проверяем поле username в текущей сессии
        return 'You are logged in as ' + session['username'] #Возвращаем логин, если зашли

    return render_template('index.html') # Иначе выдать форму index.html

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users # "Таблица юзеров"
    login_user = users.find_one({'name' : request.form['username']}) # Поиск в users по полю name

    if login_user: # Если юзер есть
        # И пароли совпадают
        if bcrypt.hashpw(
                request.form['pass'].encode('utf-8')
                ,login_user['password'])\
                == login_user['password']:
            session['username'] = request.form['username'] #Записываем имя в сессию
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']}) #Ищем пользователя

        if existing_user is None: #Если нету
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt()) #Генерируем hashpass
            users.insert({'name' : request.form['username'], 'password' : hashpass}) # Добавляем запись
            session['username'] = request.form['username']
            return redirect(url_for('index')) #Переводим в index
        
        return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)