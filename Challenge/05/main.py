import os
import csv
import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from alba import name, gathering_name_and_link, extract_link, extract_details
from save import save_to_file

alba_url = "http://www.alba.co.kr"
gathered_results = gathering_name_and_link(alba_url)

name_list = []
link_list = []
details_list = []

for i in gathered_results:
    name1 = name(i)
    name_list.append(name1)

    link = extract_link(i)
    link_list.append(link)

    details = extract_details(link)

    save_to_file(name1, details)