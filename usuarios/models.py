from django.db import models
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=254,null=True,blank=True)
    #foto_perfil = models
    senha = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.nome
    
class FotoPerfil(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='perfil')
    
    def __str__(self):
        return self.id
    
class Logo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
