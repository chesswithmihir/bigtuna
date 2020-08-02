import requests
from bs4 import BeautifulSoup
import time
import csv

urls = ["https://finance.yahoo.com/quote/AMZN/analysis?p=AMZN", "https://finance.yahoo.com/quote/GOOG/analysis?p=GOOG", "https://finance.yahoo.com/quote/msft/analysis?p=msft", "https://finance.yahoo.com/quote/AAPL/analysis?p=AAPL", "https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA"]
headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
tickers = ["AMZN - Amazon.com, Inc.", 'GOOG - Alphabet Inc.', 'MSFT - Microsoft Corporation', 'AAPL - Apple Inc.', 'TSLA - Tesla, Inc.']
with open("YahooAnalysis.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Stock Name', 'No. of Analysts(Earnings)', 'Average Estimate(Earnings)', 'Low Estimate(Earnings)', 'High Estimate(Earnings)', 'Year Ago EPS(Earnings)', 'No. of Analysts(Revenue)', 'Avg. Estimate(Revenue)', 'Low Estimate(Revenue)', 'High Estimate(Revenue)', 'Year Ago Sales(Revenue)', 'Sales Growth(year/est)(Revenue)', 'EPS Est.(Earnings)', 'EPS Actual(Earnings)', 'Difference(Earnings)', 'Surpirse %(Earnings)', 'Current Estimate(EPS Trend)', '7 Days Ago(EPS Trend)', '30 Days Ago(EPS Trend)', '60 Days Ago(EPS Trend)', '90 Days Ago(EPS Trend)', 'Up Last 7 days(EPS Revisions)','Up Last 30 days(EPS Revisions)','Down Last 7 days(EPS Revisions)','Down Last 30 days(EPS Revisions)', 'Current Qtr (Growth Estimates)', 'Next Qtr (Growth Estimates)','Current Year (Growth Estimates)','Next Year (Growth Estimates)','Next 5 Years (per annum) (Growth Estimates)','Past 5 Years (per annum) (Growth Estimates)'])

    for url in range(0, 5):
        stock = []
        html_page = requests.get(urls[url])
        soup = BeautifulSoup(html_page.content, 'lxml')
        ticker = tickers[url]
        stock.append(ticker)
        perma = "W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)"
        for i in range(1,6):
            value = soup.find_all("table", class_ = perma)[0].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
        for i in range(1,7):
            value = soup.find_all("table", class_ = perma)[1].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
        for i in range(1,5):
            value = soup.find_all("table", class_ = perma)[2].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
        for i in range(1,6):
            value = soup.find_all("table", class_ = perma)[3].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
        for i in range(1,5):
            value = soup.find_all("table", class_ = perma)[4].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
        for i in range(1,7):
            value = soup.find_all("table", class_ = perma)[5].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
        writer.writerow(stock)
        time.sleep(5)
        # print("The next 5 years, {} is predicted to increase by {} per year.".format(tickers[0], next_5_years))

