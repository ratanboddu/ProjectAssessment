import myflask


#def test_student(new_home):
#    assert new_home.name == "BodduBhai


def test_home(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/?name="Ratan"')
    assert resp.status_code == 200


def test_show_class(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/show_class/?id=102')
    assert resp.status_code == 200


def test_show_update(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update')
    assert resp.status_code == 500


#def test_add():







