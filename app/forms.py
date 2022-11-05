from django.forms import ModelForm

from .models import Todos


class todosForm(ModelForm):
    class Meta:
        model = Todos
        fields = ['title','description']