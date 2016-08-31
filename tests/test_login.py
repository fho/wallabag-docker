import requests


URL = 'http://127.0.0.1:80'


def test_login_page():
    r = requests.get(URL, allow_redirects=True)

    assert r.status_code == 200
    assert 'Login' in r.text
    assert 'Password' in r.text
    assert 'Register' in r.text
    assert 'Username' in r.text


def test_login():
    with requests.Session() as s:

        data = {
            '_username': 'wallabag',
            '_password': 'wallabag'
        }

        r = s.post(URL + '/login_check', data=data)
        print(r.text)
