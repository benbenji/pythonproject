'''
从alpha_vantage下载股票数据,然后用pandas进行数据处理,最后用matplotlib进行数据可视化
'''
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# 从alpha_vantage下载股票数据
def download_stock_data(symbol):
    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    return data

# 数据处理
def process_data(data):
    data['date'] = data.index
    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    return data

# 数据可视化
def visualize_data(data):
    data['4. close'].plot()
    plt.title('Intraday Times Series for the MSFT stock (1 min)')
    plt.show()

if __name__ == '__main__':
    data = download_stock_data('MSFT')
    data = process_data(data)
    visualize_data(data)
