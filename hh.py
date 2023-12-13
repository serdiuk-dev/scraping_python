import requests
from bs4 import BeautifulSoup

url = 'https://www.irishjobs.ie/jobs/cyber-security/in-ireland'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}


def extract_max_page():

    hh_request = requests.get(url, headers=headers)
    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

    pages = []

    paginator = hh_soup.find('ul', {'class': 'res-f7vubm'})

    if paginator:
        for page_link in paginator.find_all('a'):
            page_text = page_link.text.strip()
            if page_text:  # Проверка на пустую строку
                pages.append(int(page_text))

    return pages[-1]


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        #     print(f'page={page}')
        result = requests.get(f'{url}&page={page}', headers=headers)
        print(f'Indeed:Scraiping {page}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('h2', {'class': 'res-4cffwv'})
        for result in results:
            title = result.find('div').text
            link = result.find('a')['href']

            company_div = result.find('div', {'class': 'res-kjrpl6'})
            if company_div:
                company = company_div.find('a').text
            else:
                # или любое значение по умолчанию
                company = "==I didn`t get the Company name(=="

            job = {'title': title, 'company': company, 'link': link}
            jobs.append(job)
    # print(jobs)
    return jobs


def get_jobs():
    max_page = extract_max_page()
    jobs = extract_jobs(max_page)
    return jobs
