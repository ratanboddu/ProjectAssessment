import time
from flask import Flask, flash, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

# Connection to the database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/testcheck'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


# Creating Table Student
class Student(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
    # Assigning Foreign Key
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    createdon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
    updatedon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)


# Creating Table Class
class Class(db.Model):
    id = db.Column('id', db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
    class_leader = db.Column(db.Integer, db.ForeignKey('student.id'))
    # Making us of foreign_keys to handle multiple JOIN paths
    student = db.relationship("Student", backref='classname', foreign_keys='Student.class_id')
    createdon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
    updatedon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)


# Homepage for CRUD operations
@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        ts = time.gmtime()
        createdon = time.strftime("%x %X", ts)
        classiddetail = request.form.get("selectedid")
        detail = Class.query.filter_by(id=classiddetail).first()
        classleader = request.form.get("classleader")

        if classleader == "Yes":
            studentdet = Student(name=request.form.get("name"), class_id=classiddetail, createdon=createdon,
                                 classname=detail)
            classinfo = Class.query.filter_by(id=classiddetail).first()
            classinfo.class_leader = studentdet.id

            tsu = time.gmtime()
            updateTime = time.strftime("%x %X", tsu)
            classinfo.updatedon = updateTime
            db.session.add(studentdet)
            db.session.add(classinfo)
            db.session.commit()

        else:
            studentdet = Student(name=request.form.get("name"), class_id=classiddetail, createdon=createdon,
                                 classname=detail)
            db.session.add(studentdet)
            db.session.commit()

    students = Student.query.all()
    return render_template("homepage.html", students=students)


# Add a new student record
@app.route("/add_new_record", methods=["GET", "POST"])
def add():
    return render_template("addrecord.html", classdetails=Class.query.all())


# Perform Update Operation
@app.route("/update", methods=["GET", "POST"])
def update():

    newName = request.form.get("newName")
    oldClassId = request.form.get("oldClassId")
    studentId = request.form.get("studentId")
    classleader = request.form.get("classleader")

    if classleader == "Yes":
        studentUpdate = Student.query.filter_by(id=studentId).first()
        classUpdate= Class.query.filter_by(id=oldClassId).first()
        classUpdate.class_leader = studentId
        studentUpdate.name = newName

        tsu = time.gmtime()
        updateTime = time.strftime("%x %X", tsu)
        studentUpdate.updatedon = updateTime
        classUpdate.updatedon = updateTime

        db.session.commit()
        return redirect("/")

    else:
        studentUpdate = Student.query.filter_by(id=studentId).first()

        studentUpdate.name = newName

        tsu = time.gmtime()
        updateTime = time.strftime("%x %X", tsu)
        studentUpdate.updatedon = updateTime
        db.session.commit()
        return redirect("/")


# Perform Update Operation
@app.route('/updaterecord', methods=["POST"])
def updaterecord():
    studentId=request.form.get("studentid")
    studentUpdate = Student.query.filter_by(id=studentId).first()
    return render_template("updaterecord.html", students=studentUpdate, classdet=Class.query.all())


# Perform Delete Operation
@app.route("/delete", methods=["POST"])
def delete():
    studentid = request.form.get("studentid")
    student = Student.query.filter_by(id=studentid).first()
    try:
        db.session.delete(student)
        db.session.commit()
        return redirect("/")
    except:
        flash('The Student you are trying to delete is the current Class Leader. Kindly appoint another Class Leader and try again.')
        return redirect("/")



# Display Class details
@app.route('/show_class', methods=["GET", "POST"])
def show_details():
    selectedid = request.form.get("selectedid")
    return render_template("show_class.html", students=Class.query.filter_by(id=selectedid).first(), classdet=Class.query.all())


if __name__ == "__main__":
    app.run(debug=True)