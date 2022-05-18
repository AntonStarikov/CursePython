import requests
import lxml.html
from lxml import etree

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())
ul = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[3]')

for li in ul:
    a = li.find('a')
    print(a.text)