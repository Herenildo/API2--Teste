from django.forms import ModelChoiceField
from rest_framework import serializers
from escola.models import Aluno, Curso
import io
from rest_framework.parsers import JSONParser

class AlunoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=30)
    rg = serializers.CharField(max_length=9)
    cpf = serializers.CharField(max_length=11)
    data_nascimento = serializers.DateField()

    def create(self,validated_data):
        return Aluno.objects.create(**validated_data)
    

    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.rg = validated_data.get('rg', instance.rg)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)

class CursoSerializer(serializers.Serializer):
    id=serializers.IntegerField(Read_only=True)
    codigo_curso=serializers.CharField(max_length=10)
    descricao=serializers.CharField(max_length=100)
    nivel=serializers.CharField(max_length=1,choices=(('B','Basico'),('I','Intermediario'),('A','Avancado')), blank=False,null=False,default='B')


    def create(self, validated_data):
        return Curso.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.codigo_curso = validated_data.get('codigo_curso', instance.codigo_curso)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.nivel = validated_data.get('nivel', instance.nivel)
    