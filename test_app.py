import app
import json 
import warnings


def test_hello_world():
    response = app.app.test_client().get('/hello')
    assert response.status_code == 200
    assert response.data == b'hello'

def test_chai():
    response = app.app.test_client().get('/chai')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    