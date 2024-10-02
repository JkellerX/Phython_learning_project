import requests, json, turtle
url = 'http://api.open-notify.org/iss-now.json'
odpowiedz = requests.get(url)
if (odpowiedz.status_code == 200):
    print(odpowiedz.text)
else:
    print("Huston, mamy problem:", odpowiedz.status_code)
    
