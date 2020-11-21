from bs4 import BeautifulSoup
import requests

page = requests.get("https://cv.ee/search?limit=50&offset=0&categories%5B0%5D=INFORMATION_TECHNOLOGY&towns%5B0%5D=312&isHourlySalary=false").text

soup = BeautifulSoup(page, 'lxml')
jobs = soup.find_all('li', class_='jsx-3752991021 jsx-1193941219 vacancies-list__item')

for job in jobs:
    date = job.find('span', class_='jsx-1471379408 secondary-text').text.split(' ', 1)[1]
    title = job.find('span', class_='jsx-1471379408 vacancy-item__title').text
    company = job.find('div', class_='jsx-1471379408 vacancy-item__info-main').text.split('—',1)[0]
    print(f'''
    Company Name: {company}
    Position: {title}
    Date: {date}
    ''')
