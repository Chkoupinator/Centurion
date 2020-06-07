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


def get_url_v3(arg):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0"}

    search = arg.replace(" ", "+")
    url = f"https://www.pornpics.com/?q={search}&date=latest"
    page = requests.get(url, headers=headers)
    soup = bs(page.content, "lxml")
    links = []

    imgs = soup.find_all('img')
    imgs.pop(0)
    imgs.pop(0)
    for i in imgs:
        links.append(i['data-src'])

    return random.choice(links)


def get_forbidden_words_joke():
    jokes = [
        "Your ass must be pretty jealous of all the shit that comes out of your mouth",
        "Remember when I asked for your opinion? Me neither",
        "If you’re waiting for me to care, I hope you brought something to eat, ‘cause it’s gonna be a really long time",
        "Some day you’ll go far and I really hope you stay there",
        "I’m trying my absolute hardest to see things from your perspective, but I just can’t get my head that far up my ass",
        " Sometimes it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt",
        "You only annoy me when you’re breathing, really",
        "Do yourself a favor and ignore anyone who tells you to be yourself. Bad idea in your case",
        "I don’t know what your problem is, but I’m guessing it’s hard to pronounce",
        "Do your parents even realize they’re living proof that two wrongs don’t make a right?",
        "Remember that time I said I thought you were cool? I lied",
        "I can’t help imagining how much awesomer the world would be if your dad had just pulled out",
        "Everyone’s entitled to act stupid once in awhile, but you really abuse the privilege",
        "Do you ever wonder what life would be like if you’d gotten enough oxygen at birth?",
        "Please, save your breath. You’ll probably need it to blow up your next date",
        "Can you die of constipation? I ask because I’m worried about how full of shit you are",
        "Good story, but in what chapter do you shut the fuck up?",
        "Don’t hate me because I’m beautiful. Hate me because your boyfriend thinks so",
        "Were you born on the highway? That is where most accidents happen",
        "If I wanted to hear from an asshole, I’d fart",
        "Your mom might love you, but everyone else definitely thinks you’re an idiot",
        "Sorry, I didn’t get that. I don’t speak bullshit",
        "The only way you’ll ever get laid is if you crawl up a chicken’s ass and wait",
        "If ignorance is bliss, you must be the happiest person on the planet",
        "Are you always such an idiot, or do you just show off when I’m around?",
        "There are some remarkably dumb people in this world. Thanks for helping me understand that",
        "I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said",
        "I was pro life. Then I met you",
        "You’re about as useful as a window on a submarine",
        "It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence",
        "Please just tell me you don’t plan to home-school your kids",
        "I’d tell you to go fuck yourself, but that would be cruel and unusual punishment",
        "The village called. They’d like their idiot back. You better get going",
        "You’re about as useful as an ashtray on a motorcycle",
        "People like you are the reason I’m on medication",
        "I believed in evolution until I met you",
        "If I threw a stick, you’d leave, right?",
        "You’ll never be the man your mom is",
    ]

    return random.choice(jokes)


def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    page = requests.get(url)
    soup = bs(page.content, "lxml")

    joke = soup.find('p', class_="subtitle")
    return joke.contents[0]


def check_stupid(message, word_list):

    while message[0] == "*" or message[0] == " ":
        message = message[1:]
    while message[-1] == "*" or message[-1] == " ":
        message = message[:-1]

    message = message.split()
    res = False
    if len(list(set(word_list).intersection(message))) > 0:
        res = True
    return res


def check_pp_size():

    smoll_pp_jokes = ["smoll pp fag", "gay trans", "autistic faggot", "homosexual monkey", "lol u have a tota",
                      "F", "RIP", "virgin fag", "i bet u let ppl fuck u for free", "ever thought of killing yourself ?"]
    big_pp_jokes = ["are you black ?", "noice", "bet whamen drill all over dat dick", "not bad", "plz fuck me daddy",
                    "if i had a dick like dat i would never stop fappin", "( ͡ ͡° ͜ ʖ ͡ ͡°)", "Brazzers wants to know your location", "ever considered making porn ?"]

    pp = random.randint(0, 20)

    if pp == 0:
        joke = "You have a vagina not a pp"

    elif pp <= 15:
        joke = smoll_pp_jokes[random.randint(0, len(smoll_pp_jokes))-1]

    else:
        joke = big_pp_jokes[random.randint(0, len(big_pp_jokes))-1]

    out = [pp, joke]
    return out


print(get_dad_joke())
