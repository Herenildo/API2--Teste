from rest_framework import viewsets
from escola import serializers
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer,MatriculaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os Alunos"""
    queryset=Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos"""
    queryset=Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewset(viewsets.ModelViewSet):
    """ Exibindo todas as matriculas"""
    queryset=Matricula.objects.all()
    serializer_class = MatriculaSerializer


