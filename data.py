from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta
from textblob import TextBlob

dataset = []
sentiment_index = 0.0

for i in range(0,500):
	date = str(datetime.today().date() - timedelta(days=i))

	try:
		url = 'https://www.dawn.com/newspaper/business/'+date
		res = requests.get(url)

		soup = BeautifulSoup(res.text, 'html.parser')

		title_cont = soup.find_all('div', class_='col-sm-10')

		for title in title_cont:
			text = title.h2.text
			if text[-1] == '\n':
				text = text[:-1]
			blob = TextBlob(str(text))
			for sentence in blob.sentences:
				sentiment_index = sentence.sentiment.polarity

			data = date+','+text+','+str(round(sentiment_index,3))
			dataset.append(data)
		print(i,':',date,'-> extracted')
	except:
		print(i,':',date,'-> unextracted')

print(type(dataset[0]))
with open('dataset.txt', 'w') as f:
	for item in dataset:
		f.write('%s\n' % item)
