from bs4 import BeautifulSoup
import unittest

# Парсер реализован в виде функции parse, которая принимает на вход один параметр: path_to_file — путь до файла, содержащий html код страницы википедии.
# Гарантируется, что такой путь существует. Ваша задача — прочитать файл, пройтись Beautiful Soup по статье, найти её тело (это <div id="bodyContent">) и внутри него подсчитать:
#  - Количество картинок (img) с шириной (width) не меньше 200. Например: <img width="200">, но не <img> и не <img width="199">
#  - Количество заголовков (h1, h2, h3, h4, h5, h6), первая буква текста внутри которых соответствует заглавной букве E, T или C. Например: <h1>End</h1> или <h5><span>Contents</span></h5>, но не <h1>About</h1> и не <h2>end</h2> и не <h3><span>1</span><span>End</span></h3>
#  - Длину максимальной последовательности ссылок, между которыми нет других тегов, открывающихся или закрывающихся. Например: <p><span><a></a></span>, <a></a>, <a></a></p> - тут 2 ссылки подряд, т.к. закрывающийся span прерывает последовательность. <p><a><span></span></a>, <a></a>, <a></a></p> - а тут 3 ссылки подряд, т.к. span находится внутри ссылки, а не между ссылками.
#  - Количество списков (ul, ol), не вложенных в другие списки. Например: <ol><li></li></ol>, <ul><li><ol><li></li></ol></li></ul> - два не вложенных списка (и один вложенный)
#  - Результатом работы функции parse будет список четырех чисел, посчитанных по формулам выше.

def parse(path_to_file):

    with open(path_to_file, encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'lxml')
            imgs, headers, lists = 0, 0, 0
            res_div = soup.find("div", id = "bodyContent")
            listlink = []

            res_img = res_div.find_all('img', width = lambda x: int(x or 0) >= 200)
            res_h = res_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            res_ul_ol = res_div.find_all(['ul', 'ol'])
            res_a = res_div.find_all('a')

            for i in res_img:
                     imgs += 1

            for i in res_h:
                if i.text.istitle and (i.text[0] is 'C' or i.text[0] is 'E' or i.text[0] is 'T'):
                    headers += 1

            for i in res_a:
                len_link = 1
                res_siblings = i.find_next_siblings()
                for i in res_siblings:
                    if i.name is 'a':
                        len_link += 1
                    else:
                        break
                listlink.append(len_link)
            linkslen = max(listlink)

            for i in  res_ul_ol:
                if not i.find_parents(['ul','ol']):
                    lists += 1

            return [imgs, headers, linkslen, lists]

class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
