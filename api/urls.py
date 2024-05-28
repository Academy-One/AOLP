from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.ExampleAPIView.as_view(), name='example'),
    path('usuarios/', views.usuarios_lista, name='usuarios_lista'),
    path('usuarios/<str:pk>', views.usuario_detail, name="usuario_detail")
]