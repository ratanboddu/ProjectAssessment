import myflask
import falcon


#def test_student(new_home):
#    assert new_home.name == "BodduBhai
dict_add = {
    "selectedid": 102,
    "classleader": "Yes",
    "name": "Viona"
}

dict_update_data = {
    "newName": "Sanjay Boddu Bhai",
    "oldClassId": 102,
    "studentId": 1,
    "classleader": "Yes",

}
dict_delete_data = {

    "studentId": 9

}

def test_home(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/', data=dict_add)
    assert resp.status_code == 200
    #assert resp.status_code == 200


def test_show_class(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/show_class?id=100')
    assert resp.status_code == 200


def test_show_update(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update', data=dict_update_data)
    assert resp.status_code == 302


def test_show_delete(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/delete', data=dict_delete_data)
    assert resp.status_code == 302

def test_show_update_record(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update', data=dict_update_data)
    assert resp.status_code == 302






