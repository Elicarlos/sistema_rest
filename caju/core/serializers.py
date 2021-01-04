from django.contrib.auth.models import User, Group
from rest_framework import serializers
from caju.core.models import Produto


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


""" class ProdutoSerializer(serializers.Serializer):
    id =  serializers.IntegerField(read_only=True)
    descricao = serializers.CharField(required=True, allow_blank=True, max_length=100)
    preco_compra = serializers.FloatField()
    preco_venda = serializers.FloatField()

    def create(self, validated_data):
        return Produto.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.preco_compra = validated_data.get('preco_compra', instance.preco_compra)
        instance.preco_venda = validated_data.get('preco_venda',instance.preco_venda)

        instance.save()

        return instance """

    
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'created', 'descricao', 'preco_compra', 'preco_venda']