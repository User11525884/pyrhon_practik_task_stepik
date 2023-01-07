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


def task_1_4():
    resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html')  # скачиваем файл
    html = resp.read().decode('utf8')  # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.findAll('a', href=True):
        print(a['href'])

def task_1_4_1():
    resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html')  # скачиваем файл
    html = resp.read().decode('utf8')  # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

def task_1_4_2():
    import re
    from urllib.request import urlopen
    html = str(urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8'))
    regular = re.findall(r'<a.*?href="([^"]*?)"', html)
    print(*regular, sep='\n')

def task_1_4_3():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    # href = soup.find_all('a')
    # print(*[c["href"] for c in href if c.get("href") is not None], sep='\n')
    # Или так как в видео
    href = soup.find_all('a', href=True)
    print(*[c["href"] for c in href], sep='\n')

if __name__ == '__main__':
    task_1_4_3()
