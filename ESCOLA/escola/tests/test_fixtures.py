from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixures(self):
        """Teste que verifica o carremento da fixtures"""
        estudante = Estudante.objects.get(cpf= '77964248502')
        curso = Curso.objects.get(pk='7')
        self.assertEqual(estudante.celular, "46 98242-5147")
        self.assertEqual(curso.codigo, "CPOO3")