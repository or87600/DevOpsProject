import requests
res = requests.post('http://127.0.0.1:5000/users/8', json={"user_name": "UserNumber8"})
if res.ok:
    print(res.json())

