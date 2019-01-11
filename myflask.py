""" CRUD OPERATIONS - Python Assessment"""
import uuid
import time
from flask import Flask, flash, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
# pylint: disable=missing-docstring, C0301
# pylint: disable=invalid-name


# Connection to the database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/crudtest'
app.config['SECRET_KEY'] = "ratanboddu"
db = SQLAlchemy(app)


# Creating Table Student
class Student(db.Model):  # pylint: disable=too-few-public-methods
    id = db.Column(db.String(500), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
    # Assigning Foreign Key
    class_id = db.Column(db.String(500), db.ForeignKey('class.id', name="student_key_fk", ondelete="CASCADE", onupdate="CASCADE"))
    created_on = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
    updated_on = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)


# Creating Table Class
class Class(db.Model):  # pylint: disable=too-few-public-methods
    id = db.Column('id', db.String(500), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
    class_leader = db.Column(db.String(500), db.ForeignKey('student.id', name="class_key_fk", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    # Making us of foreign_keys to handle multiple JOIN paths
    student = db.relationship("Student", foreign_keys='Student.class_id')
    created_on = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
    updated_on = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)


# Homepage for CRUD operations
@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        ts = time.gmtime()
        created_on = time.strftime("%x %X", ts)
        class_id_detail = request.form.get("selectedid")
        class_leader = request.form.get("classleader")
        if class_leader == "Yes":
            uid_id = uuid.uuid1()
            student_det = Student(id=uid_id.int, name=request.form.get("name"), class_id=class_id_detail, created_on=created_on)
            tsu = time.gmtime()
            update_time = time.strftime("%x %X", tsu)
            db.session.add(student_det)
            class_information = Class.query.filter_by(id=class_id_detail).first()
            class_information.class_leader = student_det.id
            class_information.updated_on = update_time
            db.session.add(class_information)
            db.session.commit()
        else:
            uid_id = uuid.uuid1()
            studentdet = Student(id=uid_id.int, name=request.form.get("name"), class_id=class_id_detail, created_on=created_on,
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
    class_leader = request.form.get("classleader")
    if class_leader == "Yes":
        student_update = Student.query.filter_by(id=student_id).first()
        class_update = Class.query.filter_by(id=old_class_id).first()
        class_update.class_leader = student_id
        student_update.name = new_name
        tsu = time.gmtime()
        update_time = time.strftime("%x %X", tsu)
        student_update.updated_on = update_time
        class_update.updated_on = update_time
        db.session.commit()
        return redirect("/")
    student_update = Student.query.filter_by(id=student_id).first()
    student_update.name = new_name
    tsu = time.gmtime()
    update_time = time.strftime("%x %X", tsu)
    student_update.updated_on = update_time
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
    student_id = request.form.get("studentid")
    selected_class_id = request.form.get("classid")
    student = Student.query.filter_by(id=student_id).first()
    class_lead_det = Class.query.filter_by(id=selected_class_id).first()
    if class_lead_det.class_leader == student.id:
        flash('The Student you are trying to delete is the current Class Leader.'
              ' Kindly appoint another Class Leader and try again.')
        return redirect("/")
    db.session.delete(student)
    db.session.commit()
    return redirect("/")


# Display Class details
@app.route('/show_class', methods=["GET", "POST"])
def show_details():
    selected_id = request.form.get("selectedid")
    return render_template("show_class.html", students=Class.query.filter_by(id=selected_id).first(), classdet=Class.query.all())


if __name__ == "__main__":
    app.run(debug=True)
