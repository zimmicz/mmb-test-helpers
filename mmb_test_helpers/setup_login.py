import requests

def login(url, username, password):
    """
    Login user and get authorization token.

    :param url
    :param username
    :param password
    """
    r = requests.post(url, json={'username': username, 'password': password})
    json = r.json()
    token = json['access_token']

    return {
        'Authorization': 'Bearer {}'.format(token),
        'Content-type': 'application/json'
    }

