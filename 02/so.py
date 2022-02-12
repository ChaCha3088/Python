import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"
headers={"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}

def get_last_page():
    result = requests.get(URL,headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class':'s-pagination'}).find_all('a')
    last_page=pages[-2].get_text(strip=True)
    return int(last_page)

def extract_job(html):    
    title = html.find('a', {'class':'s-link stretched-link'})
    if title is not None:
        title = html.find('a', {'class':'s-link stretched-link'}).string
    
    company = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"})
    location = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"})
    if company and location is not None:
        company, location = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"}).find_all("span", recursive=False)

    company = company.get_text(strip=True)
    location = location.get_text(strip=True)

    job_id = html.find('div')['data-jobid']

    return {
        'title':title,
        'company':company,
        'location':location,
        'apply_link': f'https://stackoverflow.com/jobs/{job_id}'
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(1,last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f'{URL}&pg={page+1}',str(headers))
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'listResults'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs