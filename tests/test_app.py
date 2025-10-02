from http import HTTPStatus


def test_root_dev_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'tonhaodev',
            'email': 'luis@tonhao.dev',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'tonhaodev',
        'email': 'luis@tonhao.dev',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'tonhaodev',
                'email': 'luis@tonhao.dev',
                'id': 1,
            }
        ]
    }
