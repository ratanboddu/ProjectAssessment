import pytest
import myflask
import flask
from myflask import*
from flask.testing import FlaskClient

# Connection to the database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/testcheck'
app.config['SECRET_KEY'] = "ratanboddu"
db = SQLAlchemy(app)


@pytest.fixture(scope='module')
def new_home():
    student = Student(id=45, name="BodduBhai", class_id=102, createdon="null", updatedon="null")
    #classdet = Class(id=102, name="10th B", class_leader=45, createdon="null", updatedon="null")
    return student


@pytest.fixture(scope='module')
def new_home_class(request):
    app = create_app(__name__, settings_override)
    testjust = myflask.app.test_client()
    #flask_app = flask.Flask(__name__)
    #testing_client = flask_app.test_client()
    ctx = myflask.app.app_context()
    ctx.push()

    yield testjust

    ctx.pop()
    #student = Student(id=45, name="BodduBhai", class_id=102, createdon="null", updatedon="null")
    #classdet = Class(id=102, name="10th B", class_leader=45, createdon="null", updatedon="null")
    #return classdet


@pytest.fixture(scope='module')
def test_resp_code():
    client = myflask.app.test_client()
    return client



