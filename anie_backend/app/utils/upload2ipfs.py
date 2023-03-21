import json

import requests

SECRETE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJlNmY5YWVjNi0wNDk3LTQxOGItOTY1OC0wNzA2MjUzNzNmMjIiLCJlbWFpbCI6ImExODIwMjIxMzk1M0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJpZCI6IkZSQTEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX0seyJpZCI6Ik5ZQzEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiYzlkMDU3NDk3NTk1MmI0NzgxMzgiLCJzY29wZWRLZXlTZWNyZXQiOiI0NGQ1ODI4NDg3NjdmNjIzNDk5ZTViNzA1ZjQ3N2QzNDc5NmYyYmQwNGNlYjgyNmQ2MjNlYzg0NDg0Mzk2OTZjIiwiaWF0IjoxNjc4NDI3OTE4fQ.Fn4CNGgTpKfZC07bWc8uL-yzejS_IQlK42JZbAP7vPQ"


def pin_file(filename):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    payload = {'pinataOptions': '{"cidVersion": 1}',
               'pinataMetadata': '{"name": "MyFile", "keyvalues": {"company": "Pinata"}}'}
    files = [
        ('file', ('cat.JPG', open(filename, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'Authorization': f'Bearer {SECRETE_KEY}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    resp = response.json()
    return f"ipfs://{resp['IpfsHash']}"


def pin_json(data):
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    payload = json.dumps({
        "pinataOptions": {
            "cidVersion": 1
        },
        "pinataContent": data
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SECRETE_KEY}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    resp = response.json()
    return f"ipfs://{resp['IpfsHash']}"
