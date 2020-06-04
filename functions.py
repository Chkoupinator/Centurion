import requests
from bs4 import BeautifulSoup as bs
import random


def get_url(arg):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0"}

    search = arg.replace(" ", "+")
    url = f"https://www.pornpics.com/?q={search}"
    page = requests.get(url, headers=headers)
    soup = bs(page.content, "lxml")
    links = []

    imgs = soup.find_all('img')
    imgs.pop(0)
    imgs.pop(0)
    for i in imgs:
        links.append(i['data-src'])

    return random.choice(links)


def get_url_v2(arg):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0"}

    search = arg.replace(" ", "+")
    url = f"http://nastypornpics.com/?q={search}"
    page = requests.get(url, headers=headers)
    soup = bs(page.content, "lxml")
    links = []

    imgs = soup.find_all('img')
    for i in imgs:
        links.append(i.get('data-src'))

    links = links[7:-5]
    return random.choice(links)


def check_stupid(message, word_list):
    res = any(ele in message for ele in word_list)
    return res