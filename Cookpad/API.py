import requests , json

def get_request(url):
    
    #GETリクエストを送信
    reqs = requests.get(url)

    text = reqs.text

    data = json.loads(text)

    for i in range(3):
        print(data["links"][i])
        get_request(data["links"][i])

get_request("https://static.cookpad.com/hr/screen/summer-intern-2022/ac7d359d66.json")