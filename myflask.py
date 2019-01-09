""" CRUD OPERATIONS - Python Assessment"""
import time
from flask import Flask, flash, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
# pylint: disable=missing-docstring, C0301
# pylint: disable=invalid-name


# Connection to the database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/pytest'
app.config['SECRET_KEY'] = "ratanboddu"
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
    class_leader = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=True)
    # Making us of foreign_keys to handle multiple JOIN paths
    student = db.relationship("Student", foreign_keys='Student.class_id')
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
            student_det = Student(name=request.form.get("name"), class_id=classiddetail, createdon=createdon)
            # class_info = Class.query.filter_by(id=classiddetail).first()
            # class_info.class_leader = student_det.id

            tsu = time.gmtime()
            update_time = time.strftime("%x %X", tsu)

            db.session.add(student_det)

            class_information = Class.query.filter_by(id=classiddetail).first()
            class_information.class_leader = student_det.id
            class_information.updatedon = update_time
            db.session.add(class_information)
            db.session.commit()

        else:
            studentdet = Student(name=request.form.get("name"), class_id=classiddetail, createdon=createdon,
                                 )
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

    new_name = request.form.get("newName")
    old_class_id = request.form.get("oldClassId")
    student_id = request.form.get("studentId")
    classleader = request.form.get("classleader")

    if classleader == "Yes":
        student_update = Student.query.filter_by(id=student_id).first()
        class_update = Class.query.filter_by(id=old_class_id).first()
        class_update.class_leader = student_id

        student_update.name = new_name

        tsu = time.gmtime()
        update_time = time.strftime("%x %X", tsu)
        student_update.updatedon = update_time
        class_update.updatedon = update_time

        db.session.commit()
        return redirect("/")

    student_update = Student.query.filter_by(id=student_id).first()

    student_update.name = new_name

    tsu = time.gmtime()
    update_time = time.strftime("%x %X", tsu)
    student_update.updatedon = update_time
    db.session.commit()
    return redirect("/")


# Perform Update Operation
@app.route('/updaterecord', methods=["POST"])
def updaterecord():
    student_id = request.form.get("studentid")
    student_update = Student.query.filter_by(id=student_id).first()
    return render_template("updaterecord.html", students=student_update, classdet=Class.query.all())


# Perform Delete Operation
@app.route("/delete", methods=["POST"])
def delete():
    studentid = request.form.get("studentid")
    student = Student.query.filter_by(id=studentid).first()
    try:
        db.session.delete(student)
        db.session.commit()
        return redirect("/")
    except IntegrityError:
        flash('The Student you are trying to delete is the current Class Leader.'
              ' Kindly appoint another Class Leader and try again.')
        return redirect("/")


# Display Class details
@app.route('/show_class', methods=["GET", "POST"])
def show_details():
    selectedid = request.form.get("selectedid")
    return render_template("show_class.html", students=Class.query.filter_by(id=selectedid).first(), classdet=Class.query.all())


if __name__ == "__main__":
    app.run(debug=True)
