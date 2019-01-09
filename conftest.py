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
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/test'
    app.config['SECRET_KEY'] = "ratanboddu"
    dbname = SQLAlchemy(app)
    dbname.create_all()



@pytest.fixture(scope='module')
def test_resp_code():
    client = myflask.app.test_client()
    return client



