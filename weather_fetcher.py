import requests

API_KEY = ""
BASE_URL = ""

city = input("Enter the name of the City... ")
request_url = f"{BASE_URL}?apiid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print("We met an error!!")
