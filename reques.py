import requests
req_res = requests.post(url='http://127.0.0.1:8000/Account/',json={"firstName":"rr","lastName":"rrr","phoneNumber":"09915631899","password":"0928007634","repeatPassword":"0928007634"})
print(req_res.status_code)