from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('profesor/', views.ProfesorView.as_view(), name='profesor'),
   path('eliminar/<int:pk>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('eliminar/profesor/<int:pk>/', views.eliminar_profesor, name='eliminar_profesor'),
]


