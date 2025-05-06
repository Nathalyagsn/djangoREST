from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.create(
            codigo = 'ACD',
            descricao = 'Teste de texto para curso 01',
            nivel = 'B'
        )
        self.curso_02 = Curso.objects.create(
            codigo = 'BBC',
            descricao = 'Teste de texto para curso 02',
            nivel = 'A'
        )

    def test_de_requisicao_para_testar_lista_de_curso(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_de_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE um curso"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_de_requisicao_put_para_atualizar_um_curso(self):
        """Testte de requisição PUT para um curso"""
        dados = {
            'codigo': 'CCD',
            'descricao': 'Teste para atualizar',
            'nivel': 'B'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code,status.HTTP_200_OK)