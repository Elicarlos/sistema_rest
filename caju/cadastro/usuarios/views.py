from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.models import User

## Cria a view


class IndexView(TemplateView):
    template_name = 'index.html'

class UsuarioCreate(CreateView):
    template_name = "cadastro/form.html"
    model = User
    fields = ['username', 'email', 'password']