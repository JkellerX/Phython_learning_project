
# How to download the type of avatar's code? 

def download_type(question, defaul):
    request = question + ' [' + defaul + ']? '
    answer = input(request)
    if (answer == ''):
        answer = defaul
    print('You choose:', answer)
    return answer

hair_style = download_type('what is the hair color', 'brown')
lenght_hair = download_type('what is the length of the hair', 'short')
eyes = download_type('what is the eyes colour', 'blue')
gender = download_type('What is the gender', 'woman')
glasses = download_type('glasses', 'no')
beard = download_type('beard', 'no')
