from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


quote_page = 'https://www.amazon.in/BassHeads-225-Super-Extra-Headphones/dp/B01M9C51T9/ref=zg_bs_electronics_6?_encoding=UTF8&psc=1&refRID=8ZQC04R246AH7877MFZD'
page=  urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')
Product_title = soup.find('span', attrs={'class':'a-size-large'})
title=Product_title.text.strip()


print(title)
dataArr = [title]

with open('index.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(dataArr)
#sys.exit()
csvFile.close()
