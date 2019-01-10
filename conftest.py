import pytest
import flask
from flask_sqlalchemy import SQLAlchemy
import myflask
from myflask import db as _db
#
# # Connection to the database
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/testcheck'
# app.config['SECRET_KEY'] = "ratanboddu"
# db = SQLAlchemy(app)
#
# #
# @pytest.yield_fixture(scope="session")
# def create_app(request):
#     # Connection to the database
#     test_app = flask.Flask(__name__)
#     test_app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost/pytest'
#     test_app.config['SECRET_KEY'] = "ratanboddu"
#     ctx = test_app.app_context()
#     ctx.push()
#
#     yield test_app
#
#     ctx.pop()
#
#
# @pytest.fixture(scope="session")
# def testapp(create_app):
#     return create_app.test_client()
#
#
#
#
# @pytest.yield_fixture(scope='session')
# def db_call(create_app):
#     _db.app = create_app
#
#     _db.init_app(create_app)
#     _db.create_all()
#
#     yield _db
#
#     _db.drop_all()
#
#
# @pytest.fixture(scope='function', autouse=True)
# def session(db_call):
#     connection = db_call.engine.connect()
#     transaction = connection.begin()
#
#     options = dict(bind=connection, binds={})
#     session_ = db_call.create_scoped_session(options=options)
#
#     db_call.session = session_
#
#     yield session_
#
#     transaction.rollback()
#     connection.close()
#     session_.remove()


    # app.config['SECRET_KEY'] = "ratanboddu"
    # db = SQLAlchemy(app)
    # db.create_all()
    # yield db
    #
    # @request.addfinalizer
    # def drop():
    #     db.drop_all()




@pytest.fixture(scope='session')
def test_resp_code():
    test_app = myflask.app
    client = test_app.test_client()
    # with test_app.app_context():
    #     myflask.db.create_all()
    #
    #     yield client  # this is where the testing happens!
    #     myflask.db.drop_all()
    #     return myflask.db
    myflask.db.create_all()
    yield client
    myflask.db.drop_all()



