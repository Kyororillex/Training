import requests
import json

def get_request(url):

    reqs = requests.get(url)

    if reqs.status_code == 404:
        print('%s Not Found' % url)

    else:
        print('%s Exist' % url)

        text = reqs.text

        data = json.loads(text)

        for i in range(3):
            get_request(data["links"][i])


get_request("https://static.cookpad.com/hr/screen/summer-intern-2022/ac7d359d66.json")
