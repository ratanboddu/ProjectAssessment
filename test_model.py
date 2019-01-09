dict_add_no = {
    "selectedid": 101,
    "classleader": "No",
    "name": "Viona Gonsalves"
}
dict_add_yes = {
    "selectedid": 102,
    "classleader": "Yes",
    "name": "Viona Gonsalves"
}
dict_update_data_no = {
    "newName": "Viona Gonsalves",
    "oldClassId": 101,
    "studentId": 30,
    "classleader": "No",

}
dict_update_data_yes = {
    "newName": "Viona Gonsalves",
    "oldClassId": 102,
    "studentId": 31,
    "classleader": "Yes",

}
dict_delete_data = {

    "studentid": 30


}
dict_delete_data_exception = {

    "studentid": 31


}

dict_update_record = {
    "studentid": 30

}
dict_stud_id = {
    "studentid": 1
}


# To display class details
def test_show_class(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/show_class')
    assert resp.status_code == 200


# To add new record when the classleader=No
def test_home(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/', data=dict_add_no)
    assert resp.status_code == 200


# To update a record when the classleader=No
def test_show_update(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update', data=dict_update_data_no)
    assert resp.status_code == 302


# To delete a record without exception
def test_show_delete(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/delete', data=dict_delete_data)
    assert resp.status_code == 302


# To check update record
def test_show_update_record(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/updaterecord', data=dict_update_record)
    assert resp.status_code == 200


# To test add new record
def test_add_new_record(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/add_new_record')
    assert resp.status_code == 200


#Test cases for classleader=Yes


# To add a record when the classleader=Yes
def test_home_yes(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/', data=dict_add_yes)
    assert resp.status_code == 200


# To update a record when the classleader=Yes
def test_show_update_yes(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/update', data=dict_update_data_yes)
    assert resp.status_code == 302


# To delete a record with exception
def test_show_delete_yes(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/delete', data=dict_delete_data_exception)
    assert resp.status_code == 302







