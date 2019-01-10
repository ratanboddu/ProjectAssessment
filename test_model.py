dict_add_no = {
    "selectedid": 44426495382941689493289587869381099512,
    "classleader": "No",
    "name": "Archit Masurkar"
}
dict_add_yes = {
    "selectedid": 62426495382941689493289587869381066556,
    "classleader": "Yes",
    "name": "Aamir Shaikh"
}
dict_update_data_no = {
    "newName": "Sarvesh D Deshmukh",
    "oldClassId": 44426495382941689493289587869381099512,
    "studentId": 128133200461758240586121768451546423427,
    "classleader": "No",

}
dict_update_data_yes = {
    "newName": "Sarvesh D Deshmukh",
    "oldClassId": 44426495382941689493289587869381099512,
    "studentId": 128133200461758240586121768451546423427,
    "classleader": "Yes",

}
dict_delete_data = {

    "studentid": 246714335622455588435087160597237604483,
    "classid": 44426495382941689493289587869381099512

}
dict_delete_data_exception = {

    "studentid": 274535724957053534432097441674764886147,
    "classid": 56426495382941689493289587869381088534

}

dict_update_record = {
    "studentid": 2272902444848516369510609141741002883

}
dict_show_class = {
    "selectedid": 44426495382941689493289587869381099512
}


# To display class details
def test_show_class(test_resp_code):
    abc = test_resp_code
    resp = abc.post('/show_class', data=dict_show_class)
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









