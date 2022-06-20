import requests


class TestCursos:
    headers = {'Authorization': 'Token 9a64dab7ee8dc23257ce3f1c5cbc54cd707d7a87'} # noqa
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}14/', headers=self.headers) # noqa
        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Novo Curso de Python rsrs",
            "url": "https://www.geekuniversity.com.br/novollllcurlsodedjango"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo) # noqa

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo curso de Ruby",
            "url": "www.geek.com.br/rsrsrkkkkks"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}15/', headers=self.headers, data=atualizado) # noqa
        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo curso de Django 2",
            "url": "http.//www.geekuniversity.com.br/novodjangorsrsrs"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}15/', headers=self.headers, data=atualizado) # noqa
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}15/', headers=self.headers) # noqa
        assert resposta.status_code == 204 and len(resposta.text) == 0
