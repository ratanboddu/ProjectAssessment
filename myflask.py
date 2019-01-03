import time
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/testcheck'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    createdon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
    updatedon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)

    #def __repr__(self, name, id, class_id, createdon, updatedon):
    #   self.name = name
    #    self.id = id
    #    self.class_id = class_id
    #    self.createdon = createdon
    #    self.updatedon = updatedon
    #    return "<Name: {}, Id: {}, Class Id: {}, Created On:{}>".format(self.name, self.id, self.class_id, self.createdon)


class Class(db.Model):
    id = db.Column('id', db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
    student = db.relationship("Student", backref='classname')
    createdon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
    updatedon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)




@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        ts = time.gmtime()
        createdon = time.strftime("%x %X", ts)
        classiddetail = request.form.get("selectedid")
        detail = Class.query.filter_by(id=classiddetail).first()
        #detail = Class(id=classiddetail, name="10th B")
        studentdet = Student(name=request.form.get("name"), class_id=classiddetail, createdon=createdon, classname=detail)
        db.session.add(studentdet)
        db.session.commit()

    students = Student.query.all()
    return render_template("homepage.html", students=students)

@app.route("/add_new_record", methods=["GET", "POST"])
def add():
    return render_template("addrecord.html", classdetails=Class.query.all())


@app.route("/update", methods=["GET", "POST"])
def update():

    newName = request.form.get("newName")
    oldName = request.form.get("oldName")

    newClassId = request.form.get("newClassId")
    oldClassId = request.form.get("oldClassId")

    studentId = request.form.get("studentId")

    studentUpdate = Student.query.filter_by(id=studentId).first()

    studentUpdate.name = newName
    studentUpdate.class_id = newClassId

    tsu = time.gmtime()
    updateTime = time.strftime("%x %X", tsu)
    studentUpdate.updatedon = updateTime
    db.session.commit()
    return redirect("/")



@app.route("/delete", methods=["POST"])
def delete():
    studentid = request.form.get("studentid")
    student = Student.query.filter_by(id=studentid).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")


@app.route('/updaterecord', methods=["POST"])
def updaterecord():
    currentid=request.form.get("name")
    currentclassidd=request.form.get("studentclassid")
    studentId=request.form.get("studentid")
    studentUpdate = Student.query.filter_by(id=studentId).first()

    return render_template("updaterecord.html", students=studentUpdate, classdet=Class.query.all())


@app.route('/show_class', methods=["GET", "POST"])
def show_details():
    selectedid = request.form.get("selectedid")
    return render_template("show_class.html", students=Class.query.filter_by(id=selectedid).first(), classdet=Class.query.all())


if __name__ == "__main__":
    app.run(debug=True)