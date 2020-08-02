import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://ycharts.com/indicators/moodys_seasoned_aaa_corporate_bond_yield"

headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
html_page = requests.get(url)
soup = BeautifulSoup(html_page.content, 'lxml')
date = []
rate = []
with open("AAA.csv", "w") as file:
    writer = csv.writer(file)
    for i in range(1,10):
        time.sleep(4)
        table = soup.find_all("table", class_="histDataTable")[0].find_all("tr")[i].find_all("td")[0].get_text().strip()
        date.append(table)
    writer.writerow(date)
    for i in range(1,10):
        time.sleep(4)
        table = soup.find_all("table", class_="histDataTable")[0].find_all("tr")[i].find_all("td")[1].get_text().strip()
        rate.append(table)
    writer.writerow(rate)
file.close()

