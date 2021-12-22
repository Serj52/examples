import requests
from datetime import datetime
import json

def calc_age(uid):
    pam_user = {'access_token':'', 'user_ids': uid}
    r = requests.get('https://api.vk.com/method/users.get?v=5.71', params = pam_user)
    response_user_id = json.loads(r.text)

    res_id = [i.get('id') for i in response_user_id['response']][0]
    pam_id = {'access_token':'','user_id': res_id, 'fields': 'bdate'}
    r = requests.get('https://api.vk.com/method/friends.get?v=5.71', params = pam_id)
    response_friend = json.loads(r.text)
    d1 = datetime.now()
    list1 = []

    for i in response_friend['response']['items']:
        try:
            d2 = datetime.strptime(i.get('bdate'), '%d.%m.%Y')
            res_y = d1.year - d2.year
            list1.append(res_y)
        except ValueError:
            continue
        except TypeError:
            continue
    res = [(i, list1.count(i)) for i in list1]
    return (sorted(set(res), key = lambda item: (-item[1], item[0])))

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)