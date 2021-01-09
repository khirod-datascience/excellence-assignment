from flask import Flask, render_template, request, redirect, url_for, session 
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import mysql.connector



app = Flask(__name__)  
app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'excellence'


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE excellence")
mydbu = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="excellence"
)
mycursor = mydbu.cursor()
#mycursor.execute("CREATE TABLE users (username VARCHAR(255),password VARCHAR(255), address VARCHAR(1000))")

@app.route('/')
def formq():
    return render_template('form.html')

@app.route('/', methods =['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password'] 
        address = request.form['address']
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="excellence"
        )
        
        mycursor = mydb.cursor()
        
        sql = "INSERT INTO users (username,password,address) VALUES (%s,%s,%s)"
        val = (username, password,address)
        mycursor.execute(sql, val)
        mydb.commit()
        msg="record updated successfully"
        return render_template('login.html', msg = msg)
    return render_template('login.html')
  
mysql1 = MySQL(app)
@app.route('/login', methods =['GET', 'POST']) 
def login():
   
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
        username = request.form['username'] 
        password = request.form['password'] 
        cursor = mysql1.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM users WHERE username = % s AND password = % s', (username, password, )) 
        account = cursor.fetchone() 
        if account: 
            session['loggedin'] = True
            session['username'] = account['username'] 
            msg = ' you have Logged in successfully !'
            user=username
            return render_template('update.html', msg = msg,user = user) 
        else: 
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg) 

@app.route('/update', methods =['GET', 'POST'])
def update():
    if request.method == 'POST':
        oaddress = request.form['oaddress'] 
        naddress = request.form['naddress'] 

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="excellence"
        )
        
        mycursor = mydb.cursor()
        
        sql = "UPDATE users SET address = %s WHERE address = %s"
        val = (naddress,oaddress)
        mycursor.execute(sql, val)
        mydb.commit()
        msg="record updated successfully"
        return render_template('update.html', msg = msg)

    return render_template('update.html')

    
    
    
if __name__ == "__main__":
    app.run(debug = True)
    


