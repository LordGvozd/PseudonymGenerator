from bs4 import BeautifulSoup as BS

import requests


def get_english_adj():
    url = "https://www.englishdom.com/ua/skills/glossary/wordset/top100-prilagatelnyx/"
    html = requests.get(url)
    soup = BS(html.text, "lxml")

    all_adj = soup.find_all("p", class_="word")

    all_adj_str = ""

    for i in all_adj:
        all_adj_str += " " + i.text

    return all_adj_str


def get_english_noun():
    url = "https://www.englishdom.com/skills/glossary/wordset/top100-sushhestvitelnyx/"
    html = requests.get(url)
    soup = BS(html.text, "lxml")

    all_adj = soup.find_all("p", class_="word")

    all_adj_str = ""

    for i in all_adj:
        all_adj_str += " " + i.text

    return all_adj_str


def get_english_names(url):
    html = requests.get(url)

    soup = BS(html.text, "lxml")

    all_names = soup.find_all("td", class_="column-1")
    all_names_str = ""

    for i in all_names:
        all_names_str += " " + i.text

    return all_names_str

def save():
    with open("Words/adj_en", "w") as f:
        f.write(get_english_adj())

    with open("Words/noun_en", "w") as f:
        f.write(get_english_noun())

    with open("Words/male_name_en", "w") as f:
        f.write(get_english_names("https://english4life.ru/muzhskie-anglijskie-imena.html"))

    with open("Words/female_name_en", "w") as f:
        f.write(get_english_names("https://english4life.ru/zhenskie-anglijskie-imena.html"))

    with open("Words/last_name_en", "w") as f:
        f.write(get_english_names("https://english4life.ru/anglijskie-familii.html"))


if __name__ == "__main__":
    save()


