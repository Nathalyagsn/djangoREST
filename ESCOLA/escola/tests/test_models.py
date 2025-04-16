from django.test import TestCase
from escola.models import Estudante, Curso


class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('Teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "Teste de Modelo",
            email = 'teste@modelo.com',
            cpf = '79454794485',
            data_nascimento = '1999-10-14',
            celular = '81 99999-9999'
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'teste@modelo.com')
        self.assertEqual(self.estudante.cpf, '79454794485' )
        self.assertEqual(self.estudante.data_nascimento, '1999-10-14')
        self.assertEqual(self.estudante.celular, '81 99999-9999')


class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'ABC',
            descricao = 'Teste de texto para uma descrição',
            nivel = 'A'
        )
    
    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de curso"""
        self.assertEqual(self.curso.codigo,'ABC' )
        self.assertEqual(self.curso.descricao, 'Teste de texto para uma descrição')
        self.assertEqual(self.curso.nivel, 'A')
        