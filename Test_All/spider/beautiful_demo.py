import requests
from bs4 import BeautifulSoup

d1 = {}

for page in range(1, 15):
    url = f"https://www.cnblogs.com/wupeiqi/default.html?page={page}"

    html = requests.get(url, ).text
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all('a', class_='postTitle2')
    for li in res:
        title = li.get_text().strip()
        href = li.attrs['href'].strip("")
        print(title, href)
        d1[title] = href

print(d1)
