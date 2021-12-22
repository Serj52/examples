from bs4 import BeautifulSoup
from decimal import Decimal
import requests

# В функцию convert(amount, cur_from, cur_to, date, requests)
# будет передана сумма amount в валюте с кодом cur_from, и её требуется перевести в валюту cur_to через рубль (код: RUR).
# Для запроса к API нужно использовать переданный requests, точнее, его метод get().
#
# Все суммы и курсы требуется хранить в Decimal, т.к. для финансовых данных вычисления с фиксированной точкой подходят больше.
# Конечный результат нужно округлить до 4-х знаков, перед тем как вернуть его из функции. Посмотрите метод quantize().
# Для некоторых валют курс возвращается из расчета не на одну денежную единицу указанной валюты, а на 10 или даже 100,
# поэтому у курса валюты в XML есть не только Value, но и Nominal, и справедлива формула: Nominal ед. валюты = Value рублей.
# При проверке на сервере сеть недоступна. В функцию будет передан фейковый requests, его интерфейс и response аналогичны настоящему.
# Если его использовать в объеме, требуемом для задания, разницы не будет заметно


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?', params={'date_req': date})
    soup = BeautifulSoup(response.content, "xml")
    res_cur_to = soup.find('CharCode', text=cur_to)

    if cur_from == 'RUR':
        for i in res_cur_to.find_next_siblings():
            if i.name == 'Nominal':
                nom_b = i.text
            elif i.name == 'Value':
                val_b = i.text
        res = amount / (Decimal(val_b.replace(',', '.')) / (Decimal(nom_b)))
        return res.quantize(Decimal('1.0000'))

    else:
        res_cur_from = soup.find('CharCode', text=cur_from)

        for i in res_cur_from.find_next_siblings():
            if i.name == 'Nominal':
                nom_a = i.text
            elif i.name == 'Value':
                val_a = i.text

        for i in res_cur_to.find_next_siblings():
            if i.name == 'Nominal':
                nom_b = i.text
            elif i.name == 'Value':
                val_b = i.text

        res = (amount * (Decimal(val_a.replace(',', '.')) / Decimal(nom_a))) / (Decimal(val_b.replace(',', '.')) / (Decimal(nom_b)))
        return res.quantize(Decimal('1.0000'))


if __name__ == '__main__':
    convert(Decimal("1000"), 'USD', 'EUR', "05/10/2020", requests)
