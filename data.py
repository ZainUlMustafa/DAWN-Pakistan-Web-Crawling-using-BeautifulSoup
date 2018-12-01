from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta

dataset = []

for i in range(0,500):
	date = str(datetime.today().date() - timedelta(days=i))

	url = 'https://www.dawn.com/newspaper/business/'+date
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')

	title_cont = soup.find_all('div', class_='col-sm-10')

	for title in title_cont:
		data = date+','+title.h2.text
		dataset.append(data)
	print(date,'-> extracted')

print(type(dataset[0]))
with open('dataset.txt', 'w') as f:
	for item in dataset:
		f.write('%s\n' % item)
