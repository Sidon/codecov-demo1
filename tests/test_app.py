def test_health(client):
    check = client.get('/healthcheck')
    assert check.status == '200 OK'
    assert check.data == b"It's ok!"





