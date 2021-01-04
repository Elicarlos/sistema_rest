from django.urls import path
from .import views


urlpatterns = [
    path('produtos/', views.produto_list),
    path('produtos/<int:pk>/', views.produto_detail)
]