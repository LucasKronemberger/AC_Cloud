from rest_framework import serializers
from .models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']

class ProdutoSerializer(serializers.ModelSerializer):
    # Opcional: exibe o nome da categoria no JSON para facilitar a leitura
    categoria_nome = serializers.ReadOnlyField(source='categoria.nome')

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'imagem', 'data_criacao', 'categoria', 'categoria_nome']