from dataclasses import fields
from django.forms import ModelChoiceField
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
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
        instance.save()
        return instance
class CursoSerializer(serializers.Serializer):
    NIVEL = (
    ('B', 'Basico'),
    ('I', 'Intermediario'),
    ('A', 'Avancado')
)
    id = serializers.IntegerField(read_only=True)
    codigo_curso=serializers.CharField(max_length=10)
    descricao=serializers.CharField(max_length=100)
    nivel=serializers.ChoiceField(choices=NIVEL, default='B')


    def create(self, validated_data):
        return Curso.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.codigo_curso = validated_data.get('codigo_curso', instance.codigo_curso)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.nivel = validated_data.get('nivel', instance.nivel)
        instance.save()
        return instance

class MatriculaSerializer(serializers.Serializer):

    PERIODO=(
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )
    id=serializers.IntegerField(read_only=True)
    aluno=serializers.PrimaryKeyRelatedField(queryset=Aluno.objects.all())
    curso=serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all())
    periodo=serializers.ChoiceField(choices=PERIODO, default='M')

    def create(self, validated_data):
        return Matricula.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.aluno=validated_data.get('aluno',instance.aluno)
        instance.curso=validated_data.get('curso',instance.curso)
        instance.periodo=validated_data.get('periodo', instance.periodo)
        instance.save()
        return instance
    
class ListaMatriculasAlunoSerializer(serializers.Serializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo=serializers.SerializerMethodField()
    class Meta:
        model= Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()
    
# ...

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']