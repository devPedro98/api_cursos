import requests

headers = {'Authorization': 'Token 9a64dab7ee8dc23257ce3f1c5cbc54cd707d7a87'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum",
    "url": "https://www.geekuniversity.com.br/scrmum"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso) # noqa

# Testando o código de status HTTP 201

assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado

assert resultado.json()['titulo'] == novo_curso['titulo']
