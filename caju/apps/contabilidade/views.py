from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework import permissions
from caju.core.serializers import UserSerializer, GroupSerializer, ProdutoSerializer, FornecedorSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from caju.core.models import Produto, Fornecedor

class IndexView(TemplateView):
    template_name = 'modelo.html'



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def produto_list(request):
    """ Lista todos os produtos ou cria um"""

    if request.method == 'GET':
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProdutoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def fornecedor_list(request):
    ''' Lista todos os fornecedores '''

    if request.method == 'GET':
        fornecedor = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedor, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FornecedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)



@csrf_exempt
def produto_detail(request, pk):
    """Recupere, atualize ou exclua um snippet de código."""

    try:
        produto = Produto.objects.get(pk=pk)
    
    except produto.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return JsonResponse(serializer.data)


    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProdutoSerializer(produto, datat=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)    
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        produto.delete()
        return HttpResponse(status=204)







