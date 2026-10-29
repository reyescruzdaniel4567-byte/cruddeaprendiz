from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='bases'),  
    path('crear_aprendiz/', views.crear_aprendiz, name='crear_aprendiz'),
    path('editar_aprendiz/<str:documento>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('eliminar_aprendiz/<str:documento>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),

]  

