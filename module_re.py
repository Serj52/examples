import re


def findall(regexp):
    text = 'b+=10faecbdc-=bbcdefab+=+10fdabecc-=b-101efdacbx-=yefdcab'

    return re.findall(regexp, text)

def calculate(data, findall):
    matches = findall('([abc])([+|-]?)=([abc]?\d*?)([+-]*\d*)')
    for v1, s, v2, n in matches:
        if s is '+' :
            data[v1] += data.get(v2, 0) + int(n or 0)
        elif s is '-':
            data[v1] -= data.get(v2, 0) + int(n or 0)
        else:
            data[v1] = data.get(v2, 0) + int(n or 0)

    return data

result = calculate({'a': 1, 'b': 2, 'c': 3}, findall)
correct = {"a": -98, "b": 196, "c": -686}
if result == correct:
    print ("Correct")
else:
    print ("Incorrect: %s != %s" % (result, correct))