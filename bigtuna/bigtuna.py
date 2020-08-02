#!/usr/bin/env python3

#ok, this might be huge, but you got this!! we got it!
import os, sys
import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


#TKR.py
url = [['https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/msft/analysis?p=msft', 'https://www.msn.com/en-us/money/stockdetails/analysis/nas-msft/fi-a1xzim', 'https://www.macrotrends.net/stocks/charts/MSFT/microsoft/free-cash-flow'], ['https://finance.yahoo.com/quote/FB/?p=FB', 'https://finance.yahoo.com/quote/FB/analysis?p=FB', 'https://www.msn.com/en-us/money/stockdetails/analysis/nas-fb/fi-a1slm7', 'https://www.macrotrends.net/stocks/charts/fb/facebook/free-cash-flow'], ['https://finance.yahoo.com/quote/amzn/?p=amzn', 'https://finance.yahoo.com/quote/AMZN/analysis?p=AMZN', 'https://www.msn.com/en-us/money/stockdetails/analysis/nas-amzn/fi-a1nhlh', 'https://www.macrotrends.net/stocks/charts/AMZN/amazon/free-cash-flow'], ['https://finance.yahoo.com/quote/GOOG/?p=GOOG', 'https://finance.yahoo.com/quote/goog/analysis?p=goog', 'https://www.msn.com/en-us/money/stockdetails/analysis/nas-goog/fi-a1u3p2', 'https://www.macrotrends.net/stocks/charts/goog/google/free-cash-flow'], ['https://finance.yahoo.com/quote/aapl/?p=aapl', 'https://finance.yahoo.com/quote/AAPL/analysis?p=AAPL', 'https://www.msn.com/en-us/money/stockdetails/analysis/nas-aapl/fi-a1mou2', 'https://www.macrotrends.net/stocks/charts/aapl/apple/free-cash-flow']]


with open("/home/pi/mihir/bigtuna/bigtuna.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day Range', '52 Week Range', 'Volume', 'Avg. Volume', 'Market Cap', 'Beta (5Y Monthly)', 'PE Ratio', 'EPS (TTM)', 'Earnings Date' , 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est',  'No. of Analysts(Earnings)', 'Average Estimate(Earnings)', 'Low Estimate(Earnings)', 'High Estimate(Earnings)', 'Year Ago EPS(Earnings)', 'No. of Analysts(Revenue)', 'Avg. Estimate(Revenue)', 'Low Estimate(Revenue)', 'High Estimate(Revenue)', 'Year Ago Sales(Revenue)', 'Sales Growth(year/est)(Revenue)', 'EPS Est.(Earnings)', 'EPS Actual(Earnings)', 'Difference(Earnings)', 'Surpirse %(Earnings)', 'Current Estimate(EPS Trend)', '7 Days Ago(EPS Trend)', '30 Days Ago(EPS Trend)', '60 Days Ago(EPS Trend)', '90 Days Ago(EPS Trend)', 'Up Last 7 days(EPS Revisions)','Up Last 30 days(EPS Revisions)','Down Last 7 days(EPS Revisions)','Down Last 30 days(EPS Revisions)', 'Current Qtr (Growth Estimates)', 'Next Qtr (Growth Estimates)','Current Year (Growth Estimates)','Next Year (Growth Estimates)','Next 5 Years (per annum) (Growth Estimates)','Past 5 Years (per annum) (Growth Estimates)','Revenue', 'Net Income', 'Market Cap', 'Enterprise Value', 'Net Profit margin %', 'PEG Ratio', 'Beta', 'Forward P/E', 'Prices/Sales', 'Price/Book', 'EBITDA', 'Return on Captial %', 'Return on Equity %', 'Return on Assets', 'BVPS', 'Shares Outstanding', 'Last Split Factor(Date)', 'Last Dividend (Ex-Date)', 'Dividend Declaration Date', 'Sales (Revenue) Q/Q Growth', 'Sales (Revenue) Q/Q Growth INDUSTRY', 'Net Income YTD Growth', 'Net Income YTD Growth INDUSTRY', 'Net Income Q/Q Growth', 'Net Income Q/Q Growth INDUSTRY', 'Sales 5-Year Annual Average','Sales 5-Year Annual Average INDUSTRY', 'Net Income 5-Year Annual Average','Net Income 5-Year Annual Average INDUSTRY', 'Dividends 5-Year Annual Average','Dividends 5-Year Annual Average INDUSTRY', 'Gross Margin', 'Gross Margin INDUSTRY','Pre-Tax Margin', 'Pre-Tax Margin INDUSTRY', 'Net Profit Margin','Net Profit Margin INDUSTRY', 'Average Gross Margin 5-Year Annual Average','Average Gross Margin 5-Year Annual Average INDUSTRY', 'Average Pre-Tax Margin 5-Year Annual Average','Average Pre-Tax Margin 5-Year Annual Average INDUSTRY', 'Average Net Profit Margin 5-Year Annual Average','Average Net Profit Margin 5-Year Annual Average INDUSTRY', 'Current P/E Ratio','Current P/E Ratio INDUSTRY', 'P/E Ratio 5yr HI','P/E Ratio 5yr HI INDUSTRY', 'P/E Ratio 5yr LO','P/E Ratio 5yr LO INDUSTRY', 'Price/Sales','Price/Sales INDUSTRY', 'Price/Book Val','Price/Book Val INDUSTRY', 'Price/Cash Flow Ratio', 'Price/Cash Flow Ratio INDUSTRY','Debt/Quity Ratio','Debt/Quity Ratio INDUSTRY', 'Current Ratio','Current Ratio INDUSTRY', 'Quick Ratio', 'Quick Ratio INDUSTRY', 'Leverage Ratio','Leverage Ratio INDUSTRY', 'BVPS', 'BVPS INDUSTRY', 'Annual FCF Year 1', 'Annual FCF Year 2', 'Annual FCF Year 3', 'Annual FCF Year 4', 'Annual FCF Year 5'])
    #writer.writerow([])

    for a in range(0,5):
        stock = []


        #YahooSummary

        html_page = requests.get(url[a][0])
        soup = BeautifulSoup(html_page.content, 'lxml')

        header_info = soup.find_all("div", id="quote-header-info")[0]
        stock_title = header_info.find("h1").get_text()
        time.sleep(5)
        current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text().strip()
        stock.append(stock_title)
        stock.append(current_price)
        print(stock_title, file=sys.stderr)
        print(current_price, file=sys.stderr)
        table_info1 = soup.find_all("div", class_ = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")
        table_info2 = soup.find_all("div", class_ = "D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)")[0].find_all("tr")


        for i in range(0,8):
            time.sleep(5)
            value1 = table_info1[i].find_all("td")[1].get_text()
            stock.append(value1)
            print(value1, file=sys.stderr)

        # print("")
        for i in range(0,8):
            time.sleep(5)
            value2 = table_info2[i].find_all("td")[1].get_text()
            stock.append(value2)
            print(value2, file=sys.stderr)


        #YahooAnalysis
        time.sleep(5)
        html_page = requests.get(url[a][1])
        soup = BeautifulSoup(html_page.content, 'lxml')
        perma = "W(100%) M(0) BdB Bdc($seperatorColor) Mb(25px)"
        for i in range(1,6):
            value = soup.find_all("table", class_ = perma)[0].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
            print(value, file=sys.stderr)
            time.sleep(5)
        for i in range(1,7):
            value = soup.find_all("table", class_ = perma)[1].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
            print(value, file=sys.stderr)
            time.sleep(5)
        for i in range(1,5):
            value = soup.find_all("table", class_ = perma)[2].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
            print(value, file=sys.stderr)
            time.sleep(5)
        for i in range(1,6):
            value = soup.find_all("table", class_ = perma)[3].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
            print(value, file=sys.stderr)
            time.sleep(5)
        for i in range(1,5):
            value = soup.find_all("table", class_ = perma)[4].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
            print(value, file=sys.stderr)
            time.sleep(5)
        for i in range(1,7):
            value = soup.find_all("table", class_ = perma)[5].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(value)
            print(value, file=sys.stderr)
            time.sleep(5)
        time.sleep(5)





        #MSN Analysis Part 1
        time.sleep(5)
        html_page = requests.get(url[a][2])
        soup = BeautifulSoup(html_page.content, 'lxml')
        inspector = 'table-data-rows'

        for i in range(1,11):
            table_info3 = soup.find_all("div", class_ = inspector)[0].find_all("ul")
            value3 = table_info3[i].find_all('p')[1].get_text().strip()
            print(value3, file=sys.stderr)
            stock.append(value3)
            time.sleep(5)

        for i in range(1, 10):
            table_info4 = soup.find_all("div", class_ = inspector)[1].find_all("ul")
            value4 = table_info4[i].find_all('p')[1].get_text().strip()
            print(value4, file=sys.stderr)
            stock.append(value4)
            time.sleep(5)




        #MSN Analysis Part 2
        time.sleep(5)
        perma = "keyratioscontainer"
        for j in range(1,7):
            for i in range(1,3):
                table = soup.find_all("div", class_ = perma)[0].find_all("ul")[j].find_all("li")[i].get_text().strip()
                print(table, file=sys.stderr)
                stock.append(table)
                time.sleep(5)

        #Profitability Analysis Page
        for j in range(1,7):
            for i in range(1,3):
                table = soup.find_all("div", class_ = perma)[1].find_all("ul")[j].find_all("li")[i].get_text().strip()
                stock.append(table)
                print(table, file=sys.stderr)
                time.sleep(5)

        # Price Ratios Analysis Page
        for j in range(1,7):
            for i in range(1,3):
                table = soup.find_all("div", class_ = perma)[2].find_all("ul")[j].find_all("li")[i].get_text().strip()
                stock.append(table)
                print(table, file=sys.stderr)
                time.sleep(5)
        for j in range(1,6):
            for i in range(1,3):
                table = soup.find_all("div", class_ = perma)[3].find_all("ul")[j].find_all("li")[i].get_text().strip()
                stock.append(table)
                print(table, file=sys.stderr)
                time.sleep(5)



        #macrotrends FCF values
        html_page = requests.get(url[a][3])
        soup = BeautifulSoup(html_page.content, 'lxml')
        for i in range(1,6):
            header_info = soup.find_all("table", class_="historical_data_table table")[0].find_all("tr")[i].find_all("td")[1].get_text().strip()
            stock.append(header_info)
            time.sleep(5)
            print(header_info, file=sys.stderr)


        writer.writerow(stock)
        #writer.writerow([])













#AAA.py
time.sleep(5)
url = "https://ycharts.com/indicators/moodys_seasoned_aaa_corporate_bond_yield"
html_page = requests.get(url)
soup = BeautifulSoup(html_page.content, 'lxml')
date = []
rate = []
with open("/home/pi/mihir/bigtuna/AAA.csv", "w") as file:
    writer = csv.writer(file)
    for i in range(1,21):
        time.sleep(5)
        table = soup.find_all("table", class_="histDataTable")[0].find_all("tr")[i].find_all("td")[0].get_text().strip()
        date.append(table)
    writer.writerow(date)
    #writer.writerow([])

    for i in range(1,21):
        time.sleep(5)
        table = soup.find_all("table", class_="histDataTable")[0].find_all("tr")[i].find_all("td")[1].get_text().strip()
        rate.append(table)
    writer.writerow(rate)
    #writer.writerow([])














#TKR_PCR.py
time.sleep(5)

url = ["https://www.alphaquery.com/stock/MSFT/volatility-option-statistics/30-day/put-call-ratio-oi", "https://www.alphaquery.com/stock/FB/volatility-option-statistics/30-day/put-call-ratio-oi", "https://www.alphaquery.com/stock/AMZN/volatility-option-statistics/30-day/put-call-ratio-oi", "https://www.alphaquery.com/stock/GOOG/volatility-option-statistics/30-day/put-call-ratio-oi", "https://www.alphaquery.com/stock/AAPL/volatility-option-statistics/30-day/put-call-ratio-oi"]



today = datetime.now()


with open("/home/pi/mihir/bigtuna/PCR.csv", "a") as file:
    vals = []
    writer = csv.writer(file)
    writer.writerow(['MSFT', 'FB', 'AMZN', 'GOOG', 'AAPL', today])

    for c in range(0,5):
        html_page = requests.get(url[c])
        soup = BeautifulSoup(html_page.content, 'lxml')
        time.sleep(5)
        table = soup.find_all("tr", id="indicator-put-call-ratio-oi")[0].find_all("td")[1].get_text().strip()
        vals.append(table)
    writer.writerow(vals)
    #writer.writerow([])
















#results.csv
#graham intrinsic value


with open('/home/pi/mihir/bigtuna/AAA.csv', newline='') as csvfile:
    data = [row for row in csv.reader(csvfile)]
    bond_yield = float(data[1][0].split("%")[0])
csvfile.close()





with open('/home/pi/mihir/bigtuna/bigtuna.csv', newline='') as csvfile:
    data = [row for row in csv.reader(csvfile)]
    msft = (data[1][1])
    fb = (data[2][1])
    amzn = (data[3][1]).split(',')
    amzn = float(amzn[0] + amzn[1])
    goog = (data[4][1]).split(',')
    goog = float(goog[0] + goog[1])
    aapl = (data[5][1])
csvfile.close()

msft_fiv = (float(data[1][13])) * 4.4 * (8.5 + 2 * (float(data[1][45].split('%')[0]))) / float(bond_yield)
msft_piv = (msft_fiv / ((1.15) ** 5))

fb_fiv = (float(data[2][13])) * 4.4 * (8.5 + 2 * (float(data[2][45].split('%')[0]))) / float(bond_yield)
fb_piv = (fb_fiv / ((1.15) ** 5))

amzn_fiv = (float(data[3][13])) * 4.4 * (8.5 + 2 * (float(data[3][45].split('%')[0]))) / float(bond_yield)
amzn_piv = (amzn_fiv / ((1.15) ** 5))

goog_fiv = (float(data[4][13])) * 4.4 * (8.5 + 2 * (float(data[4][45].split('%')[0]))) / float(bond_yield)
goog_piv = (goog_fiv / ((1.15) ** 5))

aapl_fiv = (float(data[5][13])) * 4.4 * (8.5 + 2 * (float(data[5][45].split('%')[0]))) / float(bond_yield)
aapl_piv = (aapl_fiv / ((1.15) ** 5))

aapl_piv = float("{:.2f}".format(aapl_piv))
msft_piv = float("{:.2f}".format(msft_piv))
goog_piv = float("{:.2f}".format(goog_piv))
fb_piv = float("{:.2f}".format(fb_piv))
amzn_piv = float("{:.2f}".format(amzn_piv))









#Earnings
avg = 0
for i in range(2, 10, 2):
    avg += float(data[1][92])
avg /= 5

msft_earnings = (avg * float(data[1][13])) #MSFT earnings price

fb_earnings = (avg * float(data[2][13])) #FB earnings price

amzn_earnings = (avg * float(data[3][13])) #AMZN earnings

goog_earnings = (avg * float(data[4][13])) #GOOG earnings

aapl_earnings = (avg * float(data[5][13])) #AAPL earnings price


aapl_earnings = float("{:.2f}".format(aapl_earnings))
goog_earnings = float("{:.2f}".format(goog_earnings))
amzn_earnings = float("{:.2f}".format(amzn_earnings))
fb_earnings = float("{:.2f}".format(fb_earnings))
msft_earnings = float("{:.2f}".format(msft_earnings))




#Sales
# revenue * Price/Sales INDUTRY/ outgoing shares

# avg = float(data[2][97]) + float(data[4][97]) + float(data[6][97]) + float(data[8][97]) + float(data[10][97])
# avg = (avg/5)

msft_sales = ((float(data[1][48].split('B')[0]) * 1000000000 * float(data[1][98])) / ((float(data[1][63].split('B')[0]) * 1000000000)))

fb_sales = ((float(data[2][48].split('B')[0]) * 1000000000 * float(data[2][98])) / ((float(data[2][63].split('B')[0]) * 1000000000)))

amzn_sales = ((float(data[3][48].split('B')[0]) * 1000000000 * float(data[3][98])) / ((float(data[3][63].split('M')[0]) * 1000000)))

goog_sales = ((float(data[4][48].split('B')[0]) * 1000000000 * float(data[4][98])) / ((float(data[4][63].split('M')[0]) * 1000000)))

aapl_sales = ((float(data[5][48].split('B')[0]) * 1000000000 * float(data[5][98])) / ((float(data[5][63].split('B')[0]) * 1000000000)))

aapl_sales = float("{:.2f}".format(aapl_sales))
fb_sales = float("{:.2f}".format(fb_sales))
amzn_sales = float("{:.2f}".format(amzn_sales))
goog_sales = float("{:.2f}".format(goog_sales))
msft_sales = float("{:.2f}".format(msft_sales))





# Book value

msft_book = float("{:.2f}".format((float(data[1][62]) * float(data[1][100]))))
fb_book = float("{:.2f}".format((float(data[2][62]) * float(data[2][100]))))
amzn_book = float("{:.2f}".format((float(data[3][62]) * float(data[3][100]))))
goog_book = float("{:.2f}".format((float(data[4][62]) * float(data[4][100]))))
aapl_book = float("{:.2f}".format((float(data[5][62]) * float(data[5][100]))))






#EV/EBITDA
msft_ebitda = float(data[1][51].split('T')[0]) * 1000 / float(data[1][58].split('B')[0])
fb_ebitda = float(data[2][51].split('B')[0]) / float(data[2][58].split('B')[0])
amzn_ebitda = float(data[3][51].split('T')[0]) * 1000 / float(data[3][58].split('B')[0])
goog_ebitda = float(data[4][51].split('B')[0]) / float(data[4][58].split('B')[0])
aapl_ebitda = float(data[5][51].split('T')[0]) * 1000 / float(data[5][58].split('B')[0])

avg = (msft_ebitda) + (fb_ebitda) + (amzn_ebitda) + (goog_ebitda) + (aapl_ebitda)
avg = avg/5




msft_ev = "{:.2f}".format((float(data[1][58].split('B')[0]) * avg / ((float(data[1][63].split('B')[0])))))
msft_ev = float(msft_ev)

fb_ev = "{:.2f}".format((float(data[2][58].split('B')[0]) * avg / ((float(data[2][63].split('B')[0])))))
fb_ev = float(fb_ev)

amzn_ev = "{:.2f}".format((float(data[3][58].split('B')[0]) * avg * 1000 / ((float(data[3][63].split('M')[0])))))
amzn_ev = float(amzn_ev)

goog_ev = "{:.2f}".format((float(data[4][58].split('B')[0]) * avg * 1000  / ((float(data[4][63].split('M')[0])))))
goog_ev = float(goog_ev)

aapl_ev = "{:.2f}".format((float(data[5][58].split('B')[0]) * avg / ((float(data[5][63].split('B')[0])))))
aapl_ev = float(aapl_ev)





#Price/Cash flow

msft_cashflow = float(msft) / ((float(data[1][101]) / float(data[1][102])))
msft_cashflow = ("{:.2f}".format(msft_cashflow))

fb_cashflow = float(fb) / ((float(data[2][101]) / float(data[2][102])))
fb_cashflow = ("{:.2f}".format(fb_cashflow))

amzn_cashflow = float(amzn) / ((float(data[3][101]) / float(data[3][102])))
amzn_cashflow = ("{:.2f}".format(amzn_cashflow))

goog_cashflow = float(goog) / ((float(data[4][101]) / float(data[4][102])))
goog_cashflow = ("{:.2f}".format(goog_cashflow))

aapl_cashflow = float(aapl) / ((float(data[5][101]) / float(data[5][102])))
aapl_cashflow = ("{:.2f}".format(aapl_cashflow))










#write to results


msft_avg = (float(msft_piv) + float(msft_earnings) + float(msft_sales) + float(msft_book) + float(msft_ev) + float(msft_cashflow)) / 6
fb_avg = (float(fb_piv) + float(fb_earnings) + float(fb_sales) + float(fb_book) + float(fb_ev) + float(fb_cashflow)) / 6
goog_avg = (float(goog_piv) + float(goog_earnings) + float(goog_sales) + float(goog_book) + goog_ev + float(goog_cashflow)) / 6
amzn_avg = (float(amzn_piv) + float(amzn_earnings) + float(amzn_sales) + float(amzn_book) + float(amzn_ev) + float(amzn_cashflow)) / 6
aapl_avg = (float(aapl_piv) + float(aapl_earnings) + float(aapl_sales) + float(aapl_book) + float(aapl_ev) + float(aapl_cashflow)) / 6





msft_weighted_avg = "{:.2f}".format(float(msft_piv) * 0.1 + float(msft_earnings) * 0.25 + float(msft_sales) * 0.4 + float(msft_book) * .1 + float(msft_ev) * .05 + float(msft_cashflow) * .1)
fb_weighted_avg = "{:.2f}".format(float(fb_piv) * 0.1 + float(fb_earnings) * 0.25 + float(fb_sales) * 0.4 + float(fb_book) * .1 + float(fb_ev) * .05 + float(fb_cashflow) * .1)
goog_weighted_avg = "{:.2f}".format(float(goog_piv) * 0.1 + float(goog_earnings) * 0.25 + float(goog_sales) * 0.4 + float(goog_book) * .1 + float(goog_ev) * .05 + float(goog_cashflow) * 0.1)
amzn_weighted_avg = "{:.2f}".format(float(amzn_piv) * 0.1 + float(amzn_earnings) * 0.25 + float(amzn_sales) * 0.4 + float(amzn_book) * .1 + float(amzn_ev) * .05 + float(amzn_cashflow) * .1)
aapl_weighted_avg = "{:.2f}".format(float(aapl_piv) * 0.1 + float(aapl_earnings) * 0.25 + float(aapl_sales) * 0.4 + float(aapl_book) * .1 + float(aapl_ev) * .05 + float(aapl_cashflow) * .1)






amzn = "$" + str(amzn)
msft = "$" + str(msft)
aapl = "$" + str(aapl)
fb = "$" + str(fb)
goog = "$" + str(goog)




with open("/home/pi/mihir/bigtuna/Results.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Stock Name', 'Graham Present Intrinsic', 'Graham Future Intrinsic', 'Earnings Value',  'Sales Valuation', 'Book Valuation', 'EV/EBITDA valuation', 'Cash Flow Valuation', 'graham weighted', 'earnings weighted', 'sales weighted', 'book weighted', 'ev weighted', 'cashflow weighted', 'average', 'weighted average', 'Stock Price Today'])


    #MSFT
    writer.writerow(['MSFT', msft_piv, msft_fiv, msft_earnings, msft_sales, msft_book, msft_ev, msft_cashflow, float(msft_piv) * 0.1, float(msft_earnings) * 0.25, float(msft_sales) * 0.4, float(msft_book) * .1, float(msft_ev) * .05, float(msft_cashflow) * .1, msft_avg, msft_weighted_avg, msft])
    #writer.writerow([])
    #FB
    writer.writerow(['FB', fb_piv, fb_fiv, fb_earnings, fb_sales, fb_book, fb_ev, fb_cashflow, float(fb_piv) * 0.1, float(fb_earnings) * 0.25, float(fb_sales) * 0.4, float(fb_book) * .1, float(fb_ev) * .05, float(fb_cashflow) * .1, fb_avg,  fb_weighted_avg, fb])
    #writer.writerow([])
    #AMZN
    writer.writerow(['AMZN', amzn_piv, amzn_fiv, amzn_earnings, amzn_sales,amzn_book, amzn_ev, amzn_cashflow, float(amzn_piv) * 0.1, float(amzn_earnings) * 0.25, float(amzn_sales) * 0.4, float(amzn_book) * .1, float(amzn_ev) * .05, float(amzn_cashflow) * .1, amzn_avg,  amzn_weighted_avg, amzn])
    #writer.writerow([])
    #GOOG
    writer.writerow(['GOOG', goog_piv, goog_fiv, goog_earnings, goog_sales, goog_book, goog_ev, goog_cashflow, float(goog_piv) * 0.1, float(goog_earnings) * 0.25, float(goog_sales) * 0.4, float(goog_book) * .1, float(goog_ev) * .05, float(goog_cashflow) * .1, goog_avg,  goog_weighted_avg, goog])
    #writer.writerow([])
    #AAPL
    writer.writerow(['AAPL', aapl_piv, aapl_fiv, aapl_earnings, aapl_sales, aapl_book, aapl_ev,aapl_cashflow , float(aapl_piv) * 0.1, float(aapl_earnings) * 0.25, float(aapl_sales) * 0.4, float(aapl_book) * .1, float(aapl_ev) * .05, float(aapl_cashflow) * .1, aapl_avg,  aapl_weighted_avg, aapl])
    #writer.writerow([])
