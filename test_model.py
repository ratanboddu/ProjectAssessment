import myflask
import falcon


dict_add_no = {
    "selectedid": 101,
    "classleader": "No",
    "name": "Viona Gonsalves"
}
dict_update_data_no = {
    "newName": "Viona Gonsalves",
    "oldClassId": 102,
    "studentId": 12,
    "classleader": "No",

}

dict_delete_data = {

    "studentid": 12


}


def test_home(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/', data=dict_add_no)
    assert resp.status_code == 200

#
# def test_home(test_resp_code):
#     abc = test_resp_code
#     resp = abc.post('/', data=dict_add_yes)
#     assert resp.status_code == 200

def test_show_class(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/show_class')
    assert resp.status_code == 200


def test_show_update(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update', data=dict_update_data_no)
    assert resp.status_code == 302


#
# def test_show_update(test_resp_code):
#     abc = test_resp_code
#     resp = abc.post('/update', data=dict_update_data_yes)
#     assert resp.status_code == 302


def test_show_delete(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/delete', data=dict_delete_data)
    assert resp.status_code == 302

#
# def test_show_delete(test_resp_code):
#     abc = test_resp_code
#     resp = abc.post('/delete', data=dict_delete_data_exception)
#     assert resp.status_code == 302


def test_show_update_record(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/updaterecord', data=dict_delete_data)
    assert resp.status_code == 200



