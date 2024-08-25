from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet,CursoViewSet, ListaAlunosMatriculados, ListaMatriculaAluno, MatriculaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos',AlunoViewSet, basename='Alunos')
router.register('cursos',CursoViewSet, basename='Cursos')
router.register('Matricula',MatriculaViewset,basename='Matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/',ListaMatriculaAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
