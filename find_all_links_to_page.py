from urllib.request import urlopen
from bs4 import BeautifulSoup


def print_all_links():
    html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html ").read().decode('utf-8')
    s = str(html)
    pos = s.find('<a href=')
    while pos != -1:
        posquote = s.find('"', pos + 9)
        href = s[pos + 9:posquote]
        print(href)
        pos = s.find('<a href=', pos + 1)


def task_1_3():
    resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html')  # скачиваем файл
    html = resp.read().decode('utf8')  # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser')  # делаем суп
    table = soup.find('table', attrs={'class': 'wikitable sortable'})
    cnt = 0
    for tr in soup.find_all('tr'):
        cnt += 1
        for td in tr.find_all(['td', 'th']):
            cnt *= 2
    print(cnt)


if __name__ == '__main__':
    task_1_3()
