from app.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_add_member():
    client = app.test_client()
    response = client.post('/add_member', json={"name": "Yash"})
    assert response.status_code == 201
