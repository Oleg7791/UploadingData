import requests

# создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3 +json'}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

# сохранение API в переменной.
response_dict = r.json()

# обработка результатов
print(response_dict.keys())