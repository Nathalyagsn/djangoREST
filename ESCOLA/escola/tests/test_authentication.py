from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
    
    def test_auteticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um user com as credenciais corretas"""
        usuario = authenticate(username = 'admin',password= 'admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_auteticacao_username_incorreto(self):
        """Teste que verifica a autenticação de um username incorreto"""
        usuario = authenticate(username = 'adni',password= 'admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_auteticacao_password_incorreta(self):
        """Teste que verifica a autenticação de um password incorreto"""
        usuario = authenticate(username = 'admin',password= 'adm')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
