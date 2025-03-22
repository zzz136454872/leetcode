import requests

# 获取百度首页内容
url = 'http://www.baidu.com'
response = requests.get(url)
html_content = response.text

print(html_content)

# 计算字符数
char_count = len(html_content)

# 输出结果
print(f'百度首页的字符数为: {char_count}')
