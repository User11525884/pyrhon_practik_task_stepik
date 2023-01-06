from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html ").read().decode('utf-8')
s = str(html)
pos = s.find('<a href=')
while pos != -1:
    posquote = s.find('"', pos + 9)
    href = s[pos + 9:posquote]
    print(href)
    pos = s.find('<a href=', pos + 1)

