import requests
res = requests.delete('http://127.0.0.1:5000/users/1')
if res.ok:
    print(res.json())
else:
    print("Status Code:", res.status_code)