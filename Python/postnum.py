import requests
import json

url = "https://zipcloud.ibsnet.co.jp/api/search"

postnum = input("7桁の郵便番号を入力してください: ")
    
param = {"zipcode": postnum}

data = requests.get(url, param)

text = data.text

data = json.loads(text)

if data["results"] is None:
    print('郵便番号が違います')

else:

    address = data["results"][0]

    print(address["address1"], address["address2"], address["address3"])
