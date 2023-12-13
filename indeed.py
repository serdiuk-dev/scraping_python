import cloudscraper
from bs4 import BeautifulSoup
# import requests
import pandas as pd


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept-Language': 'en-US,en;q=0.5', }
    url = f'https://ie.indeed.com/jobs?q=cyber+security&l=Ireland&start={page}'
    scraper = cloudscraper.create_scraper()
    r = scraper.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def transform(soup):
    divs = soup.find_all('div', {'class': 'job_seen_beacon'})
    # return len(divs)
    for item in divs:
        title = item.find('a').text
        company = item.find('div', {'class': 'css-t4u72d'}).text
        try:
            salary = item.find('div', {'class': 'css-1ihavw2'}).text
        except:
            salary = ''
        summary = item.find(
            'div', {'class': 'job-snippet'}).text.replace('\n', '')
        # print(summary)
    # return
        job = {
            'title': title,
            'Company': company,
            'Salary': salary,
            'Summary': summary
        }
        joblist.append(job)
    return


joblist = []

for i in range(0, 90, 10):
    # показывает в терминале как будут выводиться строки постранично
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)


def get_jobs():
    df = pd.DataFrame(joblist)
    jobs = df
    return jobs

# print(get_jobs())

# print(len(joblist))
# df = pd.DataFrame(joblist)

# print(df.head())
# df.to_csv('jobs.csv')
