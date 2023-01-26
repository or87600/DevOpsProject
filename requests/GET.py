import requests
res = requests.get('http://127.0.0.1:5000/users/3')
if res.ok:
    print(res.json())
else:
    print("Status Code:", res.status_code)