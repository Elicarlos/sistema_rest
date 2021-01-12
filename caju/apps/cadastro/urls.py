from django.urls import path
from .import views
from caju.core.views import IndexView


urlpatterns = [
    path('dashboard/', IndexView.as_view(), name="dashboard"),
    path('produtos/', views.produto_list),
    path('produtos/<int:pk>/', views.produto_detail),
    path('fornecedor/', views.fornecedor_list)
]