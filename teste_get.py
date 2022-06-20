import requests

headers = {'Authorization': 'Token 3a92b0714186238fa87e81e4383ca5082837ea6e'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

# Testando se o endpoint está correto
print(resultado.status_code)
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 9

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Curso de Linux'
