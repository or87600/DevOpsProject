import requests
res = requests.put('http://127.0.0.1:5000/users/3', json={"user_name": "testtest"})
if res.ok:
    print(res.json())
else:
    print("Status Code:", res.status_code)
    print(res.text)
