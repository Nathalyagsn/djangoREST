from django.test import TestCase
from escola.models import Estudante, Curso, Matricula


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
        self.curso = Curso.objects.create (
            codigo = 'ABC',
            descricao = 'Teste de texto para uma descrição',
            nivel = 'A'
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'Matutino'
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'teste@modelo.com')
        self.assertEqual(self.estudante.cpf, '79454794485' )
        self.assertEqual(self.estudante.data_nascimento, '1999-10-14')
        self.assertEqual(self.estudante.celular, '81 99999-9999')

        """Teste que verifica os atributos do modelo de curso"""
        self.assertEqual(self.curso.codigo,'ABC' )
        self.assertEqual(self.curso.descricao, 'Teste de texto para uma descrição')
        self.assertEqual(self.curso.nivel, 'A')

        """Teste que verifica os atributos do modelo de matricula"""
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, 'Matutino')

    
       
        
    
