from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste estudante UM',
            email = 'testeestudanteUM@gmail.com',
            cpf = '51225544041',
            data_nascimento = '2004-01-02',
            celular = '81 99999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste estudante DOIS',
            email = 'testeestudante01@gmail.com',
            cpf = '75102534033',
            data_nascimento = '2003-01-02',
            celular = '81 98888-8888'
        )

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance = dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        """Teste de requisição POST para um estudante"""
        dados = {
            'nome': 'teste',
            'email': 'teste@gmail.com',
            'cpf': '49519815058',
            'data_nascimento': '1999-10-04',
            'celular': '81 99999-9999'
        }
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED )