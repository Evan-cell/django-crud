from django.forms import ModelForm

from .models import Todos


class todosForm(ModelForm):
    class Meta:
        model = Todos
        fields = ['title','description']
    def __init__(self, *args, **kwargs):
        super(todosForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'input'})
        self.fields['description'].widget.attrs.update({'class':'input'})
              