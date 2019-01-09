import myflask
import falcon


#def test_student(new_home):
#    assert new_home.name == "BodduBhai
dict_add_yes = {
    "selectedid": 102,
    "classleader": "Yes",
    "name": "Viona"
}
dict_add_no = {
    "selectedid": 102,
    "classleader": "No",
    "name": "Viona"
}
dict_update_data_no = {
    "newName": "Viona Gonsalves",
    "oldClassId": 102,
    "studentId": 57,
    "classleader": "No",

}
dict_update_data_yes = {
    "newName": "Rishi Kambil",
    "oldClassId": 103,
    "studentId": 57,
    "classleader": "Yes",

}
dict_delete_data = {

    "studentid": 57

}
dict_delete_data_exception = {

    "studentid": 57

}

dict_add_yes = {
    "selectedid": 103,
    "classleader": "Yes",
    "name": "Rishi"
}
def test_home(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/', data=dict_add_no)
    assert resp.status_code == 200


def test_home(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/', data=dict_add_yes)
    assert resp.status_code == 200

def test_show_class(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/show_class?id=100')
    assert resp.status_code == 200


def test_show_update(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update', data=dict_update_data_no)
    assert resp.status_code == 302



def test_show_update(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update', data=dict_update_data_yes)
    assert resp.status_code == 302


def test_show_delete(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/delete', data=dict_delete_data)
    assert resp.status_code == 302

def test_show_delete(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/delete', data=dict_delete_data_exception)
    assert resp.status_code == 302


def test_show_update_record(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/updaterecord', data=dict_delete_data)
    assert resp.status_code == 200



