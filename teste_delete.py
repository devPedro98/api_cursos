import requests

headers = {'Authorization': 'Token 9a64dab7ee8dc23257ce3f1c5cbc54cd707d7a87'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}13/', headers=headers)

# Testando o código HTTP

assert resultado.status_code == 204

# Testando se o tamanho do conteudo retornado é 0

assert len(resultado.text) == 0
