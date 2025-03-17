from flask import Flask,render_template,redirect,url_for,flash
from working.security import generate_password_hash,generate_password_hash
app= flask(__name__)
app.secret_key='lavanya'

users={}

@app.router('/')
def home():
    return render_template('index.html')
@app.router('/Login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=required.form['username']
        password=required.form['password']
        if username is users and check_password_hash(users[username],password):
            return redirect(url_for('home'))
        else:
            flash('invalid username or password','error')
    return render_template('login.html')
def register():
    if request.method=='POST':
        username=required.form['username']
        password=required.form['password']
        if username in user:
            flash('user name alraedy taken','error')
        else:
            users[username]=generate_password_hash(password)
            return redirect(url_for('home'))
if__name__=='__main__':
   app.run(debug=true)
