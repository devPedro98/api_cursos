import jsonpath
import requests

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(resultados)

# rimeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')

# print(primeira)

# nota_data = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')

# print(nota_data)

# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')

# print(curso_id)

# todos os nomes das pessoas que avaliaram o curso

nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)
