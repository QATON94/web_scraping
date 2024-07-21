import re


def get_description(description):
    soup = re.findall('>\n?(.*)<br/>?<br/>|\n?(.*)</div>|\n(.*)<br/>?<br/>|\n(.*?)\n', str(description))
    data = ''
    for i in soup:
        for j in i:
            if j != '':
                data += j
    return data


def get_brand(brand):
    soup = re.findall('>\n?(.*)<br/>?<br/>|\n?(.*)</div>|\n(.*)<br/>?<br/>|\n(.*?)\n', str(brand))
    data = []
    for i in soup:
        for j in i:
            word = re.findall('\w.*', j)
            if word:
                data.append(word[0])
    return data


def get_text(text_html):
    soup = re.findall('(Text_[1-5])|class=\"\w*\">(.*?)</div>', str(text_html))
    print(soup)
    data = {}
    key = ''
    value = ''
    for i in soup:
        for j in i:
            print(j)
            print(re.findall('(Text_[1-5])', j))
            if "Text_" in j:
                key = j
                print('key=', j)
            elif not "Text_" in j and j != '':
                value = j
                print('value=', value)
            if key != '' and value != "":
                data[key] = value


    return data
