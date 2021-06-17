import requests

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print('Success!', response)
        print(f'Content {response.text}')
    else:
        print(f'Whoops ada kesalahan {response.status_code}')
except Exception as e:
    print('This is an error', e)
print('Program ended')
