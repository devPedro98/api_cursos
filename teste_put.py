import requests

headers = {'Authorization': 'Token 9a64dab7ee8dc23257ce3f1c5cbc54cd707d7a87'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "https://www.geekuniversity.com.br/scrum3"
}

# Buscando o curso com ID 13
curso = requests.get(url=f'{url_base_cursos}13/', headers=headers)
print(curso.json())

# resultado = requests.put(url=f'{url_base_cursos}13/', headers=headers, data=curso_atualizado) # noqa

# Testando o código status de HTTP

# assert resultado.status_code == 200

# Testando o título

# assert resultado.json()['titulo'] == curso_atualizado['titulo']
