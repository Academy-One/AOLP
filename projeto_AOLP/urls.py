from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrando',views.cadastrando,name='cadastrando'),
    path('login/', views.login, name='login'),
    path('logando/', views.logando, name='logar'),
    path('logout/', views.logout, name='logout'),
    path('upload/', views.upload, name='upload'),
    path('uploading/', views.uploading, name='uploading'),
    path('deletar_vars/',views.del_vars, name='del_vars'),
    path('img/',views.verificar_imagem, name='ver_img'),
    path('usuarios/',views.lista_usuarios,name='lista_usuarios'),
    path('api/', include('api.urls'))
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
