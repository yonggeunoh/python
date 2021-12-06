import os
import sys
import ssl
import urllib.request
import json

client_id = "BtJyySmwU45YQyOhfX7i" # 개발자센터에서 발급받은 Client ID 값
client_secret = "MppJpqRuxg" # 개발자센터에서 발급받은 Client Secret 값

langSource = 'en'
langTarget = 'ko'
translateText = "The piece of a brass instrument is also referred to in French as an embouchure."

url = "https://openapi.naver.com/v1/papago/n2mt"
data = "source="+langSource+"&target="+langTarget+"&text=" + urllib.parse.quote(translateText)
request = urllib.request.Request(url)
request.add_header("Content-Type","application/x-www-form-urlencoded; charset=UTF-8")
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
result = ''
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

jresult = json.loads(result)
jresult['message']['result']['translatedText']