from bs4 import BeautifulSoup
import requests

def fish_parser():
    find_name_1 = input('Что ищем?  ')
    find_name_2 = input('Выбери тип катушек  ')

    req_1 = requests.get('https://spinningline.ru')
    soup = BeautifulSoup(req_1.content, 'lxml')
    res_1 = soup.find('a', alt = find_name_1)
    linc_first = res_1.get('href')

    req_2 = requests.get('https://spinningline.ru' + linc_first)
    soup = BeautifulSoup(req_2.content, 'lxml')
    res_1 = soup.find('a', alt = find_name_2)
    print(res_1.get('href'))




fish_parser()
