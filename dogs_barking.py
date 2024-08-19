#Przekształcenie kodu w funkcje:

print('Prepare the dogs')
    
def barking(dog_name, weight):
    if weight > 10:
        print(dog_name, 'Wof, wof')
    else:
        print(dog_name, 'Wof, Wof')

barking("Tokio", 2)
barking("Neli", 3)
barking("Jessie", 8)
barking("Rex", 15)

print("ok, that's enought")

#Fukcja z wartością zwrotną:

def download_barking(weight):
    if weight > 10:
        return 'Wof, Wof'
    else:
        return 'wof, Wof'

#Wywolanie funkcji z wartościa zwrotną:

toki_barking = download_barking(40)
print("Tokio is barking", toki_barking)
