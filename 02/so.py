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
        title = html.find('a', {'class':'s-link stretched-link'}).get_text()
    return {'title':title}

def extract_jobs(last_page):
    jobs = []
    for page in range(1,last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f'{URL}&pg={page+1}',str(headers))
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'flex--item fl1'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs