import requests
from bs4 import BeautifulSoup

def get_forms(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    return soup.find_all("form")