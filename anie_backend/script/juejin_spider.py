from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
import json


def add_to_polorstar(data):
    url = "https://admin.coolduck.cn/api/admin/hotspot/hotspot/add"
    payload = json.dumps(data)
    headers = {
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc1JlZnJlc2giOmZhbHNlLCJyb2xlSWRzIjpbIjEiXSwidXNlcm5hbWUiOiJhZG1pbiIsInVzZXJJZCI6MSwicGFzc3dvcmRWZXJzaW9uIjozLCJpYXQiOjE2Nzk1NTYyNzAsImV4cCI6MTY3OTU2MzQ3MH0.fEy-EEmUG0VUnMgCI-aMvpvoh1_1leBNAWjfwxj2Oi4',
        'Content-Type': 'application/json',
        'Cookie': 'locale=en-us'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(f"成功 - {response}")


def spider(cursor="0"):
    url = "https://api.juejin.cn/recommend_api/v1/short_msg/recommend"
    params = {
        "aid": "2608",
        "uuid": "6940524563542672904",
        "spider": "0"
    }

    payload = json.dumps({
        "id_type": 4,
        "sort_type": 300,
        "cursor": cursor,
        "limit": 20
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, params=params).json()
    pool = ThreadPoolExecutor(max_workers=10)
    res = []
    for item in response['data']:
        data = {
            "community_id": 1,
            "user_id": 1,
            "topic_id": 1,
            "content": item['msg_Info']['content'],

        }
        res.append(pool.submit(add_to_polorstar, data))

    for item in as_completed(res):
        print(item.result())


if __name__ == '__main__':
    spider()
