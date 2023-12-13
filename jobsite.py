import requests
from bs4 import BeautifulSoup

url = 'https://www.cybersecurityjobsite.com/jobs/?Keywords=Cyber+Security+Analyst'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}


def extract_max_page():

    js_request = requests.get(url, headers=headers)
    js_soup = BeautifulSoup(js_request.text, 'html.parser')
    pages = js_soup.find('ul', {'class': 'paginator__items'}).find_all('a')
    last_page = int(pages[-3].text)
    return last_page


def extruct_job(html):
    title = html.find('h3').find('a').find('span').text
    Company = html.find('ul').find(
        'li', {'class': 'lister__meta-item--recruiter'}).text
    Location = html.find('ul').find(
        'li', {'class': 'lister__meta-item--location'}).text

    link_element = html.find(
        'a', {'class': 'js-clickable-area-link'})
    Link = link_element['href'] if link_element and 'href' in link_element.attrs else None
    # print(Link)

    return {'title': title, 'Company': Company, 'Location': Location, 'Link': Link.strip()}


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        # print(f'page = {page}')
        result = requests.get(f'{url}&page={page}', headers=headers)
        print(f'Jobsite: Scraiping {page}')
        # print(f'{result.status_code} page={page}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'lister__details'})
        for result in results:
            # title = result.find('h3').text
            # print(result)
            job = extruct_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    max_page = extract_max_page()
    jobs = extract_jobs(max_page)
    return jobs
