import requests


def getResponseJSON(endpoint_url):
    response = None
    if endpoint_url is None or endpoint_url == '':
        return response
    else:
        response = requests.get(endpoint_url)
        status_code = response.status_code
        if status_code == 200:
            response_json = response.json()
            response = response_json
    return response