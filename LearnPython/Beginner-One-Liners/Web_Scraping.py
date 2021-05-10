import urllib.request

search_phrase = 'crypto'

with urllib.request.urlopen('https://www.wired.com/') as response:
    html = response.read().decode('utf8')
    first_pos = html.find(search_phrase)
    print(html[first_pos-30:first_pos+30])

