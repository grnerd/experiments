'''
import pyautogui as p
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

o = Options()
o.headless = True
browser = webdriver.Firefox(options=o)

browser.implicitly_wait(5)
browser.get("https://www.speedtest.net/")
browser.find_element_by_class_name("start-text").click()
browser.implicitly_wait(50)
h = browser.page_source
output = h.split('<span data-download-status-value="0.07" class="result-data-large number result-data-value download-speed">')[1].split('<')[0]
print(output)
'''

import bs4
import requests
import lxml


res=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup=bs4.BeautifulSoup(res.text, 'lxml')
# for i in soup.select('.mw-headline'):
# 	print(i.text)
for i in soup.select('.toctext'):
	print(i.text)
