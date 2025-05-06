from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Matricula, Estudante, Curso

class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.create(
            nome='João da Silva',
            cpf='12345678900',
            data_nascimento='2000-01-01'
        )

        self.curso = Curso.objects.create(
            codigo='C001',
            descricao='Curso de Python',
            nivel='B'
        )

        Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='Noturno'
        )

        Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='Diurno'
        )

    def test_de_requisicao_get_para_listar_matricula(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_de_requisicao_delete_uma_matricula(self):
        """Teste de requisição DELETE uma matricula"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_de_requisicao_put_para_atualizar_um_curso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            'codigo': 'CPOO1',
            'descricao': 'Curso de Python Orientação à Objetos 01',
            'nivel': '1'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
