import time
import myflask

#from myflask import home, Student, Class
"""

def add(x):
    return x+1


def system_error():
    raise SystemExit(1)


def test_exit():
    with pytest.raises(SystemExit):
        system_error()


def test_add():
    assert add(3) == 4

"""


def homekatesting(user_name, class_id_selected, classleader):

    if classleader is "Yes":
        ts = time.gmtime()
        createdon = time.strftime("%x %X", ts)
        studentdet = myflask.Student(name=user_name, class_id=class_id_selected, createdon=createdon)
        class_info = myflask.Class.query.filter_by(id=class_id_selected).first()
        class_info.class_leader = studentdet.id
        #myflask.db.session.add(studentdet)
        #myflask.db.session.add(class_info)
        #myflask.db.session.commit()
        return "Yes Successful"
    else:
        ts = time.gmtime()
        createdon = time.strftime("%x %X", ts)
        studentdet = myflask.Student(name=user_name, class_id=102, createdon=createdon)
        #myflask.db.session.add(studentdet)
        #myflask.db.session.commit()
        return "No Successful"


def test_home_yes():
    assert homekatesting("RatanBodduBhai", 102, "Yes") == "Yes Successful"


def test_home_no():
    assert homekatesting("RatanBodduBhai", 102, "No") == "No Successful"


def updatetesting(new_name, old_class_id, student_id, classleader):
    if classleader is "Yes":

        student_update = myflask.Student.query.filter_by(id=student_id).first()
        class_update = myflask.Class.query.filter_by(id=old_class_id).first()
        class_update.class_leader = student_id
        student_update.name = new_name
        tsu = time.gmtime()
        update_time = time.strftime("%x %X", tsu)
        student_update.updatedon = update_time
        class_update.updatedon = update_time
        #myflask.db.session.commit()
        return "Yes Successful"

    student_update = myflask.Student.query.filter_by(id=student_id).first()

    student_update.name = new_name

    tsu = time.gmtime()
    update_time = time.strftime("%x %X", tsu)
    student_update.updatedon = update_time
    #myflask.db.session.commit()
    return "No Successful"


def test_update_no():
    assert updatetesting("Bananas", 103, 3, "No") == "No Successful"


def test_update_yes():
    assert updatetesting("Bananas", 103, 3, "Yes") == "Yes Successful"
