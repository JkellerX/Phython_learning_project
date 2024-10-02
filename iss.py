import requests, json, turtle
url = 'http://api.open-notify.org/iss-now.json'
odpowiedz = requests.get(url)
if (odpowiedz.status_code == 200):
    odpowiedz_slownik = json.loads(odpowiedz.text)
    polozenie = odpowiedz_slownik['iss_position']
    print('Wspolrzedne ISS to' + polozenie['latitude'] + ' ,' + polozenie['longitude'])
else:
    print("Huston, mamy problem:", odpowiedz.status_code)

