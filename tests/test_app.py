import json


def test_health(client):
    check = client.get('/healthcheck')
    assert check.status == '200 OK'
    assert check.data == b"It's ok!"


def test_add(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'x': 1,
        'y': 2,
    }
    url = '/api/add'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.data == b'3.0'


def test_subtract(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'x': 2,
        'y': 1,
    }
    url = '/api/subtract'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.data == b'1.0'


def test_divide(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'x': 4,
        'y': 2,
    }
    url = '/api/divide'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.data == b'2.0'


def test_divide_by_zero(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'x': 4,
        'y': 0,
    }
    url = '/api/divide'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.data == b'Cannot divide by 0'




def test_multiply(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'x': 4,
        'y': 2,
    }
    url = '/api/multiply'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.data == b'8.0'

