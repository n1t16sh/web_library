from flask import (Flask,request,render_template,redirect,url_for,session)
from databse import database
from auth import login_required,role_required

app=Flask(__name__)
app.secret_key='n1t16xsh'
db=database()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register_page():
    if request.method=='POST':
        name = request.form.get("name")
        email = request.form.get("email_input")
        password = request.form.get("pass")
        roll_number = request.form.get("roll_number")
        department = request.form.get("department")
        year = request.form.get("year")
        role = req.form.get("role")
        response=db.register_user(name,email,password,role,roll_number,department,year)
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
        user=db.login_user(email,password)
        if user:
            session["user_id"]= user[0]
            session["role"]=user[4]
            session["name"]=user[1]
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html',message='email or password is incorrect')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

@app.route('/dashboard')
@login_required
@role_required('admin')
def dashboard():
    return render_template('dashboard.html',name=session["name"],role=session["role"])

if __name__=='__main__':
    app.run(debug=True)