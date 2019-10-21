from django.forms import ModelForm
from django import forms
from .models import Propriedade, Categoria, Config

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(BaseForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                if type(field) == forms.CharField:
                    field.widget.attrs['class'] = 'form-control'

class FormPropriedade(BaseForm):
    class Meta:
        model = Propriedade
        fields = '__all__'

class FormCategoria(BaseForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormConfig(BaseForm):
    class Meta:
        model = Config
        fields = '__all__'
