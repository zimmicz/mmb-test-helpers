import requests

def login(username, password):
    """
    Login user and get authorization token.

    :param url
    :param username
    :param password
    """
    r = requests.post('http://127.0.0.1/api/v1.0/account/login', json={'username': username, 'password': password})
    json = r.json()
    token = json['access_token']

    return {
        'Authorization': 'Bearer {}'.format(token),
        'Content-type': 'application/json'
    }

