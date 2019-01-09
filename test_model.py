

#def test_student(new_home):
#    assert new_home.name == "BodduBhai"



def test_class(new_home_class):
    #assert new_home_class.name == "10th B"
    client = app.test_client()
    response = new_home_class('/')
    assert response.status_code == 200








