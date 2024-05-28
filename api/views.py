from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from usuarios.models import Usuario
from .serializers import UsuarioSerializer

from django.db.models import Q

class ExampleAPIView(APIView):
    def get(self, request):
        data = {'message': 'Hello from DRF API!'}
        return Response(data)

@api_view(['GET','POST'])
def usuarios_lista(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        usuarios = Usuario.objects.filter(Q(nome__icontains=query) | Q(email__icontains=query))
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        usuarios = Usuario.objects.create(
            # id_usuario=request.data['id_usuario'],
            nome=request.data['nome'],
            email=request.data['email'],
            )
        
        serializer = UsuarioSerializer(usuarios, many=False)

        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def usuario_detail(request, pk):
    usuario = Usuario.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        usuario.nome = request.data['nome']
        usuario.email = request.data['email']

        usuario.save()
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        usuario.delete()
        return Response('usuario deletado')