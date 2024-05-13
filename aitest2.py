'''
爬取全国天气数据并可视化
'''
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

# 爬取全国天气数据
def get_weather_data():
    url = 'https://e.weather.com.cn/mweather/101010100.shtml'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

# 数据处理
def process_data(data):
    weather_data = data.get('weatherinfo', {})
    df = pd.DataFrame(weather_data, index=[0])
    return df

# 数据可视化
def visualize_data(data):
    if 'temp' in data:
        data['temp'].plot()
        plt.title('Temperature Trend')  # 更改标题以更好地反映数据内容
        plt.show()
    else:
        print("No temperature data to plot.")

if __name__ == '__main__':
    data = get_weather_data()
    data = process_data(data)
    visualize_data(data)