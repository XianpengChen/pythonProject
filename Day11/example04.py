"""下面的例子演示了如何使用requests模块（封装得足够好的第三方网络访问模块）访问网络API获取国内新闻，
如何通过json模块解析JSON数据并显示新闻标题，这个例子使用了天行数据提供的国内新闻数据接口，
其中的APIKey需要自己到该网站申请。"""
import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()
