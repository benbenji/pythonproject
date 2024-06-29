'''
用python写一个从京东上爬取华为手机信息的程序，并将结果保存到excel文件中
'''
import requests
from bs4 import BeautifulSoup
import openpyxl
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 1.获取网页源代码
# url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA&enc=utf-8&pvid=4b6f7f7b1f4b4f1fbf6b7f7b1f4b4f1f'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
# html = response.text
# 设置ChromeDriver的路径
# chromedriver_path = 'D:\\msedgedriver.exe'

# 使用Selenium启动Chrome
driver = webdriver.Edge()

# 打开网页
driver.get('https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA&qrst=1&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&pvid=7f54dcc05f5e427fad8c4e9be6ff60b7&isList=0&page=1&s=1&click=1&log_id=1719020103210.5061')
username_input = driver.find_element(By.ID,'loginname')
username_input.send_keys('18846413749')

# 定位并输入密码
password_input = driver.find_element(By.ID, 'nloginpwd')
password_input.send_keys('18545017025pzy')

# 定位登录按钮并点击
login_button = driver.find_element(By.ID, 'loginsubmit')
login_button.click()
# 等待页面加载完成
time.sleep(20)  # 根据网速和网页响应速度调整等待时间

# 获取网页源代码
html = driver.page_source

# 你的解析和数据提取代码...

# 关闭浏览器
driver.quit()
# print(html)
# # 2.解析网页源代码
# soup = BeautifulSoup(html, 'html.parser')
# # 通过查看网页源代码，找到所有的商品信息
# goods_list = soup.find_all('li', class_='gl-item')

# # 3.提取商品信息
# # 创建一个excel文件
# wb = openpyxl.Workbook()
# # 创建一个工作表
# sheet = wb.active
# # 设置工作表的标题
# sheet.title = '华为手机信息'
# # 设置表头
# sheet.append(['商品名称', '价格', '评论数', '商家', '链接'])

# for goods in goods_list:
#     # 商品名称
#     name = goods.find('div', class_='p-name').em.text
#     # 价格
#     price = goods.find('div', class_='p-price').i.text
#     # 评论数
#     commit = goods.find('div', class_='p-commit').strong.a.text
#     # 商家
#     shop = goods.find('div', class_='p-shop').span.a.text
#     # 链接
#     link = goods.find('div', class_='p-name').a['href']
#     # 将商品信息保存到excel文件中
#     sheet.append([name, price, commit, shop, link])

# # 4.保存excel文件
# wb.save('华为手机信息.xlsx')
# print('保存成功！')
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 开始时间
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 结束时间
        print(f"{func.__name__} 运行时间: {end_time - start_time:.2f}秒")
        return result
    return wrapper

# 应用装饰器到提取商品信息的函数
@timeit
def extract_goods_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    goods_list = soup.find_all('li', class_='gl-item')
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '华为手机信息'
    sheet.append(['商品名称', '价格', '评论数', '商家', '链接'])
    for goods in goods_list:
        name = goods.find('div', class_='p-name').em.text
        price = goods.find('div', class_='p-price').i.text
        commit = goods.find('div', class_='p-commit').strong.a.text
        shop = goods.find('div', class_='p-shop').span.a.text
        link = goods.find('div', class_='p-name').a['href']
        sheet.append([name, price, commit, shop, link])
    wb.save('华为手机信息.xlsx')
    print('保存成功！')
extract_goods_info(html)
# 5.查看excel文件
# os.system('华为手机信息.xlsx')

