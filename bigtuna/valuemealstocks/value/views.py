from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.

def home(request):
    return render(request, 'value/home.html')


def msft(request):
    with open('Results.csv', newline='') as csvfile:
        data = [row for row in csv.reader(csvfile)]
        dict_MSFT = {'MSFT_piv': data[1][1], 'MSFT_earnings': data[1][3], 'MSFT_sales': data[1][4], 'MSFT_book': data[1][5], 'MSFT_ev': data[1][6], 'MSFT_cashflow': data[1][7], 'MSFT_graham_w': data[1][8], 'MSFT_earnings_w': data[1][9], 'MSFT_sales_w': data[1][10], 'MSFT_book_w': data[1][11], 'MSFT_ev_w': data[1][12], 'MSFT_cashflow_w': data[1][13], 'MSFT_avg': data[1][14], 'MSFT_avg_w': data[1][15], 'MSFT_price': data[1][16], 'MSFT_margin': "{:.2f}".format(0.8 * float(data[1][15]))}

    return render(request, 'value/msft.html', dict_MSFT)

def fb(request):
    with open('Results.csv', newline='') as csvfile:
        data = [row for row in csv.reader(csvfile)]
        dict_FB = {'FB_piv': data[2][1], 'FB_earnings': data[2][3], 'FB_sales': data[2][4], 'FB_book': data[2][5], 'FB_ev': data[2][6], 'FB_cashflow': data[2][7], 'FB_graham_w': data[2][8], 'FB_earnings_w': data[2][9], 'FB_sales_w': data[2][10], 'FB_book_w': data[2][11], 'FB_ev_w': data[2][12], 'FB_cashflow_w': data[2][13], 'FB_avg': data[2][14], 'FB_avg_w': data[2][15], 'FB_price': data[2][16], 'FB_margin': "{:.2f}".format(0.8 * float(data[2][15]))}

    return render(request, 'value/fb.html', dict_FB)

def amzn(request):
    with open('Results.csv', newline='') as csvfile:
        data = [row for row in csv.reader(csvfile)]
        dict_AMZN = {'AMZN_piv': data[3][1], 'AMZN_earnings': data[3][3], 'AMZN_sales': data[3][4], 'AMZN_book': data[3][5], 'AMZN_ev': data[3][6], 'AMZN_cashflow': data[3][7], 'AMZN_graham_w': data[3][8], 'AMZN_earnings_w': data[3][9], 'AMZN_sales_w': data[3][10], 'AMZN_book_w': data[3][11], 'AMZN_ev_w': data[3][12], 'AMZN_cashflow_w': data[3][13], 'AMZN_avg': data[3][14], 'AMZN_avg_w': data[3][15], 'AMZN_price': data[3][16], 'AMZN_margin': "{:.2f}".format(0.8 * float(data[3][15]))}

    return render(request, 'value/amzn.html', dict_AMZN)

def goog(request):
    with open('Results.csv', newline='') as csvfile:
        data = [row for row in csv.reader(csvfile)]
        dict_GOOG = {'GOOG_piv': data[4][1], 'GOOG_earnings': data[4][3], 'GOOG_sales': data[4][4], 'GOOG_book': data[4][5], 'GOOG_ev': data[4][6], 'GOOG_cashflow': data[4][7], 'GOOG_graham_w': data[4][8], 'GOOG_earnings_w': data[4][9], 'GOOG_sales_w': data[4][10], 'GOOG_book_w': data[4][11], 'GOOG_ev_w': data[4][12], 'GOOG_cashflow_w': data[4][13], 'GOOG_avg': data[4][14], 'GOOG_avg_w': data[4][15], 'GOOG_price': data[4][16], 'GOOG_margin': "{:.2f}".format(0.8 * float(data[4][15]))}

    return render(request, 'value/goog.html', dict_GOOG)

def aapl(request):
    with open('Results.csv', newline='') as csvfile:
        data = [row for row in csv.reader(csvfile)]
        dict_AAPL = {'AAPL_piv': data[5][1], 'AAPL_earnings': data[5][3], 'AAPL_sales': data[5][4], 'AAPL_book': data[5][5], 'AAPL_ev': data[5][6], 'AAPL_cashflow': data[5][7], 'AAPL_graham_w': data[5][8], 'AAPL_earnings_w': data[5][9], 'AAPL_sales_w': data[5][10], 'AAPL_book_w': data[5][11], 'AAPL_ev_w': data[5][12], 'AAPL_cashflow_w': data[5][13], 'AAPL_avg': data[5][14], 'AAPL_avg_w': data[5][15], 'AAPL_price': data[5][16], 'AAPL_margin': "{:.2f}".format(0.8 * float(data[5][15]))}

    return render(request, 'value/aapl.html', dict_AAPL)

def analysis(request):
    return render(request, "value/analysis.html")

def aboutme(request):
    return render(request, "value/aboutme.html")

def terms(request):
    return render(request, "value/terms.html")
