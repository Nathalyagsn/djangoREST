from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import celular_invalido, nome_invalido, cpf_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'CPF':'O CPF deve ter um valor válido.'})
        
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'Nome':'O nome só pode conter letras.'})
        
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'Celular':'O celular precisa seguir o modelo: 99 99999-9999'})
        return dados
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude =  []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo =serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']