from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta

#########################################################
''' calculate the date'''
date = str(datetime.today().date() - timedelta(days=2))
print(date)

#########################################################
'''get the html page'''
url = 'https://www.dawn.com/newspaper/business/'+date
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

title_cont = soup.find_all('div', class_='col-sm-10')

##########################################################
'''print all the titles found'''
for title in title_cont:
	print(title.h2.text)

##########################################################