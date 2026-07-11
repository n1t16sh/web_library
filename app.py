from flask import Flask,request,render_template,redirect,url_for
from databse import database

app=Flask(__name__)
db=database()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register_page():
    if request.method=='POST':
        name=request.form.get("name")
        email=request.form.get("email_input")
        password=request.form.get("pass")
        response=db.register_user(name,email,password)
        if response :
            return redirect(url_for('login_page'))
        else:
            return render_template('register.html',message='email or password is incorrect')
    else:
        return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login_page():
    if request.method=='POST':
        email=request.form.get("email_input")
        password=request.form.get("pass")
        response=db.login_user(email,password)
        if response :
            return render_template('home.html')
        else:
            return render_template('login.html',message='email or password is incorrect')
    else:
        return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)