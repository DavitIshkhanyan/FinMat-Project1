from django.shortcuts import render
from django.http import HttpResponse
import requests
import sched, time
from bs4 import BeautifulSoup
import schedule
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, mpld3
import time
import datetime
import plotly.io
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.dates as mdates
import matplotlib as mpl

# from .models import Articles
# #from .forms import  Articleforms
from django.views.generic import DetailView
# Create your views here.

# def index(request):
#     # return HttpResponse("<h4>Hello</h4>")
#     return render(request, 'main/index.html')
tk1 = ''
per1 = 1
interval1 = '1d'
def index(request,tk,per,interval):
    global tk1,per1, interval1
    tk1 = tk
    per1 = per
    interval1 = interval
    # return HttpResponse("<h4>Hello</h4>")
    return render(request, 'main/index.html',{'tk':tk,'per':per,'interval':interval})
# class TickerData(DetailView):
#     # model = Articles
#     template_name = 'main/index.html'
#     context_object_name = 'article'

def about(request):
    # return HttpResponse("<h4>About</h4>")
    return render(request, 'main/about.html')

price = 0
diag = 0
def priceTracker():
    global price, diag, data_loaded
    url = f'https://finance.yahoo.com/quote/{tk1}?p={tk1}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')

    # price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].findAll('span')[3].text
    # price = soup.find_all('div', {'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].find('span').text
    price = soup.find_all('div', {'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].find('fin-streamer').text
    # obj = open('price.json', 'wb')
    # obj.write({'price': price})
    # obj.close
    # data = {'price': price}
    # import json
    # with open('price.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    # with open('price.json') as data_file:
    #     data_loaded = json.load(data_file)
    # print(data_loaded)
    # print(price)

    # diag = soup.find_all('div', {'smartphone_Mt(40px)'})
    # diag = soup.find_all('canvas')

    
    return price

    # while True:
    #     print('Current Price of Apple: ', priceTracker())
    #     time.sleep(60)

import io
import base64

def hist_data():
    # ticker = 'AAPL'
    ticker = tk1
    days = per1
    # period1 = int(time.mktime(datetime.datetime(2021, 11, 1, 23, 59).timetuple()))
    # period2 = int(time.mktime(datetime.datetime(2021, 11, 30, 23, 59).timetuple()))
    period2 = int(time.mktime(datetime.datetime.now().timetuple()))
    period1 = int(time.mktime((datetime.datetime.now() - datetime.timedelta(days)).timetuple()))
    interval = interval1 # 1d, 1wk, 1mo

    # query_string = f'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1607670746&period2=1639206746&interval=1d&events=history&includeAdjustedClose=true'
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    df = pd.read_csv(query_string)
    return df
# amis, tari, 5 tari

def fig():
    df = hist_data()
    plt.rcParams["figure.figsize"] = (11, 6)
    # fig = plt.figure()
    # ax = plt.axes()
    fig, ax = plt.subplots()
    # np.random.seed(1)

    # N = 100
    # y = np.random.rand(N)

    y = df['Close']
    x = df['Date']
    # x_arr = df['Date'].tolist()
    # print(x[-1])
    x = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in x]
    # fig = go.Figure()
    plt.plot(x, y)
    # Add traces, one for each slider step####################################################
    # for step in x:
    #     fig.add_trace(
    #         go.Scatter(
    #             visible=False,
    #             line=dict(color="#00CED1", width=6),
    #             name="Date = " + str(step),
    #             x= x,
    #             y= y))

    # Make 10th trace visible
    # fig.data[10].visible = True

    # Create and add slider
    # steps = []
    # for i in range(len(fig.data)):
    #     step = dict(
    #         method="update",
    #         args=[{"visible": [False] * len(fig.data)},
    #               {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    #     )
      #  step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        #steps.append(step)

    # sliders = [dict(
    #     #active=10,
    #     currentvalue={"prefix": "Frequency: "},
    #     pad={"t": 50},
    #     #steps=steps
    # )]
    #
    # fig.update_layout(
    #     sliders=sliders
    # )

    # fig.show()
    ############################################
    # ax = plt.gca()

    # formatter = mdates.DateFormatter("%Y-%m-%d")
    #
    # ax.xaxis.set_major_formatter(formatter)

    #locator = mdates.DayLocator()

    # ax.xaxis.set_major_locator(locator)

    # days1 = per1
    # interval = 1 if interval1=='1d' else 7 if interval1=='1wk' else 30
    # x = np.linspace(df['Date'][0],df['Date'][y.size],30)
    # print(x)
    # now = datetime.datetime.now()
    # then = now + datetime.timedelta(days=y.size)
    # days = mdates.drange(now, then, datetime.timedelta(days=1))

    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    # plt.plot(x, y)
    # plt.gcf().autofmt_xdate()

    # plt.plot(x,[1,2,3])
    # print(df['Close'].array)

    # x = np.arange(0, 10, 0.005)
    # y = np.exp(-x / 2.) * np.sin(2 * np.pi * x)

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # ax.set_xlim(now, then)
    # ax.set_ylim(-1, 1)
    return mpld3.fig_to_html(fig)
    # fig = plotly.io.to_json(fig)
    # return fig

def fig_to_base64(fig):
    fig = fig()
    return mpld3.fig_to_dict(fig)
    # img = io.BytesIO()
    # fig.savefig(img, format='png',
    #             bbox_inches='tight')
    # img.seek(0)

    # return base64.b64encode(img.getvalue())
# encoded = fig_to_base64(fig)
# encoded = fig_to_base64(1)
# my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))

def refresh(request):
    global price, diag
    # schedule.every(30).seconds.do(priceTracker)
    priceTracker()

    # encoded = fig_to_base64(fig)
    # my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
    # while True:
    #     schedule.run_pending()
    #     time.sleep(30)
    # schedule.run_all()
    # context = 
    # print(price)
    # res = price+my_html
    # res = '{"price":',price, ',' '"diag":', my_html, '}'
    diag = fig()

    res = {'price': price, 'diag': diag}
    res = json.dumps(res)
    return HttpResponse(res)
    # return data_loaded
    # return render(request, 'main/index.html', data_loaded)
    # return render(request, 'main/index.html')




