import requests
import json


def get_request(url):

    try:
        reqs = requests.get(url)
        reqs.raise_for_status()

        text = reqs.text

        data = json.loads(text)

        for i in range(3):
            print(data["links"][i])
            get_request(data["links"][i])

    except requests.exceptions.RequestException as e:
        exit()


get_request(
    "https://static.cookpad.com/hr/screen/summer-intern-2022/ac7d359d66.json")
