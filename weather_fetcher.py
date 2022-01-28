import requests

# use specific api key by registering user from the website openweathermap.org
API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the name of the City... ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print("We met an error!!")
