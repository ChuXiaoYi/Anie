import json

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def add_to_polorstar():
    url = "https://admin.coolduck.cn/api/admin/interview/interview/add"


def get_list():
    id_list = list()
    page = 1
    stop = False
    while not stop:
        url = f"https://svc.eleduck.com/api/v1/posts?category=4&page={page}"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        resp = response.json()
        id_list.extend([item['id'] for item in resp['posts']])
        paginate = resp['pager']
        if paginate['total_pages'] == paginate['current_page']:
            stop = True
        page += 1
        print(id_list)
    return id_list


def get_details(pid):
    url = f"https://svc.eleduck.com/api/v1/posts/{pid}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    url = "https://admin.coolduck.cn/api/admin/interview/interview/add"
    payload = json.dumps({
        "title": response['post']['title'],
        "type_id": 2,
        "source_id": 2,
        "cover": "https://polestar1.oss-cn-shanghai.aliyuncs.com/app/2023-03-21/c565cb6c-5981-447b-985f-b54eceea8303_IMG_2909 2.JPG",
        "user_id": "2",
        "content": response['post']['content'],
        "tag_id": 2,
    })
    headers = {
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc1JlZnJlc2giOmZhbHNlLCJyb2xlSWRzIjpbIjEiXSwidXNlcm5hbWUiOiJhZG1pbiIsInVzZXJJZCI6MSwicGFzc3dvcmRWZXJzaW9uIjozLCJpYXQiOjE2NzkzODQ1NjksImV4cCI6MTY3OTM5MTc2OX0.zHrMQdu54o39PpJJYg3evhiO-o9kQYArdQRs0HkQ0-s',
        'Content-Type': 'application/json',
        'Cookie': 'locale=en-us'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(f"获取id：{pid}成功 - {response}")


def main():
    print(1111)
    pool = ThreadPoolExecutor(max_workers=10)
    res = []
    for pid in get_list():
        res.append(pool.submit(get_details, pid))

    for item in as_completed(res):
        print(item.result())


if __name__ == '__main__':
    main()
