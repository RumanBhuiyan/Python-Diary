# in this python file i note down about requests module to work with
# external APIS how to make get request , with parameters, and getting data back
# in many formats like plain text, json , html format etc
import requests
url = 'https://icanhazdadjoke.com/search'

# res = requests.get(url)

# print(f'Response status code {res.status_code}')
# print(f'Response.txt  {res.text}')

# headers can be like "Accept" : "text/plain"
# headers can be like "Accept" : "text/html"
# headers can be like "Accept" : "application/json"

# res = requests.get(url,headers={"Accept": "text/plain"})
# print(res.text)

joke_term = input("Enter a word on which you wanna hear a joke : ")
jokes_number = int(input("How many jokes you wanna hear : "))

res = requests.get(url, 
                    headers={"Accept": "application/json"},
                    params={
                        "term" : joke_term,
                        "limit" : jokes_number
                    }
)
data = res.json()

print(data['results'][0]['joke'])
