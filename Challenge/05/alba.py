import codecs
from unittest import result
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time



def gathering_name_and_link(URL):
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get(URL)
    time.sleep(2) 
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    results1 = soup.find('div', id = 'MainSuperBrand').find('ul', {'class':'goodsBox'}).find_all('li', class_='impact')
    return results1

def name(x):
    name = extract_name(x)
    ab = name.replace('/', '-')
    return ab

def link(x):
    link = extract_link(x)
    return link

def extract_name(x):
    name = '.'
    if x == None:
        name = '.'
    else:
        try:
            name = x.find("span", {'class':'company'}).string
        except:
            pass
    return name

def extract_link(x):
    if x == None:
        link = '.'
    else:
        link = x.find('a')['href']
    return link

def extract_details(x):
    result_list = []
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get(x)
    time.sleep(3)
    
    try:
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
    except:
        pass
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    try:
        results1 = soup.find('div', id = 'NormalInfo').find('table', class_=False).find('tbody').find_all('tr', class_="")
        results2 = soup.find('div', id = 'NormalInfo').find('table', class_=False).find('tbody').find_all('tr', class_="divide")
        results = results1+results2
    except:
        results = '.'

    for i in results:
        b = i.find('td').get_text()
        c = b.find('채용공고가 없습니다.')
        if c == -1:
            result_list.append(extract(i))
        else:
            result_list.append('채용공고가 없습니다.')
    return result_list
    
def extract(x):
    place = '1'
    title = '1'
    time = '1'
    pay = '1'
    date = '1'

    if place == None:
        pass
    else:
        place = x.find("td", {"class": "local first"}).get_text()

    if title == None:
        pass
    else:
        title = x.find("td", {"class": "title"}).get_text()
        title = title.strip("스크랩요약보기새창보기")

    if time == None:
        pass
    else:
        time = x.find("td", {"class": "data"}).get_text()

    if pay == None:
        pass
    else:
        pay = x.find("td", {"class": "pay"}).get_text()

    if date == None:
        pass
    else:
        date = x.find("td", {"class": "regDate last"}).get_text()

    
        
    return {
        'place': place,
        'title': title,
        'time': time,
        'pay': pay,
        'date': date
    }



def extract_jobs():
    jobs = []
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs



#메인 페이지에서 회사 이름과 그 링크를 추출
##반복문으로 이름과 링크 가져옴
###위 반복문 안에 링크 안에서 place, title, time, pay, date

