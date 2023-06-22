import requests
from bs4 import BeautifulSoup
import DB


def copy_site(site, encoding):
    """Обращаемся к сайту и получаем его код в виде текста"""
    req = requests.get(site)
    req.encoding = encoding
    return req.text


def parsing(site_text):
    """Парсим полученный в copy_site текст и записываем в список"""
    list_text = []
    soup = BeautifulSoup(site_text, "lxml")
    li_find = soup.find("div", class_="entry-content").findAll("li")
    for i in li_find:
        list_text.append(i.text)
    return list_text


def adding_site_to_database(url, encoding="UTF-8", page_name="", page_start=None, page_end=None):
    """Функция вызывает парсинг между странницами(если есть) и закидывает выходящие списки в БД"""
    if page_start or page_end == None:
        cp = copy_site(url, encoding)
        compliment_list = parsing(cp)
        for compliment in compliment_list:
            DB.mongo_add_data({"not_told": "true", "compliment": compliment})
    else:
        for number in range(page_start, page_end+1):
            url = url+page_name+str(number)
            cp = copy_site(url, encoding)
            compliment_list = parsing(cp)

            for compliment in compliment_list:
                DB.mongo_add_data({"not_told": "true", "compliment": compliment})
