from django.urls import include, path
from .views import ProdutoViewSet, CategoriaViewSet # Importe a nova view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet) # Registre a nova rota

urlpatterns = [
    path('', include(router.urls)),
]