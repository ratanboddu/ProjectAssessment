import pytest
import myflask
import flask
from myflask import*
from flask.testing import FlaskClient
#
# # Connection to the database
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/testcheck'
# app.config['SECRET_KEY'] = "ratanboddu"
# db = SQLAlchemy(app)
#
#


@pytest.fixture(scope="module")
def create_db():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/testingpytest'
    app.config['SECRET_KEY'] = "ratanboddu"
    dbname = SQLAlchemy(app)

    # Creating Table Student
    class StudentTest(dbname.Model):
        id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
        name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
        # Assigning Foreign Key
        class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
        createdon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
        updatedon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)

    # Creating Table Class
    class ClassTest(dbname.Model):
        id = db.Column('id', db.Integer, unique=True, nullable=False, primary_key=True)
        name = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
        class_leader = db.Column(db.Integer, db.ForeignKey('student.id'))
        # Making us of foreign_keys to handle multiple JOIN paths
        student = db.relationship("Student", backref='classname', foreign_keys='Student.class_id')
        createdon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)
        updatedon = db.Column(db.String(500), unique=False, nullable=True, primary_key=False)


    def createdb():
        dbname.create_all()





@pytest.fixture(scope='module')
def test_resp_code():
    client = myflask.app.test_client()
    return client



@pytest.fixture(scope='module')
def test_resp_code_new():
    client = myflask.app.test_client()
    return client


