import requests

xss_payload = "<script>alert('XSS')</script>"

def scan_xss(url):

    params = {"q": xss_payload}

    response = requests.get(url, params=params)

    if xss_payload in response.text:
        return True

    return False