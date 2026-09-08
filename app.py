from flask import Flask,request,redirect,render_template,url_for,flash
app = Flask(__name__)

app.secret_key = "mysecretkey"

students = {
    'pbka123' : {
        'Name' : 'Vansh Tyagi',
        'ID' : 101,
        'Course' : 'B.Tech AI & ML' 
    },

    'payal123' : {
        'Name' : 'Payal Tyagi',
        'ID' : 102,
        'Course' : 'MCA'
    }
}

teachers = {
    'teach_1' : {
        'Name' : 'Vaishali',
        'ID' : 77,
        'Mob' : '81XXXXXXXX',
        'Address' : 'Haridwar',
        'Teach_subject' : 'Python'
    }
}

@app.route("/")
def interface():
    return render_template('first_interface.html')

@app.route("/role",methods = ['POST','GET'])
def role():
    if request.method == 'POST':
        role = request.form.get('role')

        if role == 'student':
            return render_template('Student.html')
        elif role == 'teacher':
            return render_template('Teacher.html')
        else:
            flash("Pls enter role only teacher or student")
            return redirect(url_for('interface'))

@app.route("/student",methods = ['POST','GET'])
def student_form():
    if request.method == "POST":
        id = int(request.form.get('userID'))
        pwd = request.form.get('pwd')

        if pwd in students:
            student = students[pwd]

            if student["ID"] == id:
                return render_template('details.html',student=student)
            else:
                flash('Invalid ID')
                return render_template('Student.html')
        else:
            flash("Incorrect Password")
            return render_template('Student.html')
    return render_template("Student.html")

@app.route("/teacher",methods = ['POST','GET'])
def teacher_form():
    if request.method == "POST":

        id = int(request.form.get('teacherID'))
        pwd = request.form.get('teacherPWD')

        if pwd in teachers:
            teacher = teachers[pwd]
            if teacher['ID'] == id:
                return render_template('details.html',teacher = teacher)
            else:
                flash("Invalid ID")
                return render_template('Teacher.html')
        else:
            flash("Incorrect Password")
            return render_template('Teacher.html')
    return render_template('Teacher.html')
