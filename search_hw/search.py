import requests
from bs4 import BeautifulSoup
# Исходные данные
query = input('Введите запрос: ')
query = query.replace(' ', '+')
results = int(input('Введите кол-во результатов: '))
output = str(input('P - вывод на экран, C - Файл CSV: '))
gurl = f"https://google.com/search?q={query}&num={results}"
headers = {'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox/50.0'}
source = requests.get(gurl, headers=headers).text
soup = BeautifulSoup(source, "html.parser")
search_div = soup.find_all(class_='r')  # поиск по всему содержащим результат
for result in search_div:
    y = result.h3.string  # значиния заголовков h3
    z = result.a.get('href')  # значиния ссылок
    if output == 'P':
        print(y, ':', z)  # вывод в консоль
    elif output == 'C':
        dat = '"', y, '"', ',', z
        f = "out.csv"
        print(dat, file=open(f, "a", encoding="utf-8"))  # вывод в файл csv
    else:
        print('Неверный ввод данных')
