from app import client
from models import Video


def test_get():
    res = client.get('/tutorials')

    assert res.status_code == 200
    assert len(res.get_json()) == len(Video.query.all())
    assert res.get_json()[0]['id'] == 2


def test_post():
    data = {
        'name': 'Unit tests',
        'description': 'Pytest tutorial'
    }
    res = client.post('/tutorials', json=data)

    assert res.status_code == 200
    assert res.get_json()['name'] == data['name']


def test_put():
    res = client.put('/tutorials/2', json={'name': 'UPD'})
    assert res.status_code == 200
    assert Video.query.get(2).name == 'UPD'


def test_delete():
    res = client.delete('/tutorials/2')
    assert res.status_code == 204
    assert Video.query.get(2) is None

