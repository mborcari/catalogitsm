from django.forms import ModelForm
from django import forms
from .models import Propriedade, Categoria, Config

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(BaseForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                if type(field) == forms.CharField:
                    field.widget.attrs['class'] = 'w3-input w3-border'

class FormPropriedade(BaseForm):
    class Meta:
        model = Propriedade
        fields = '__all__'

class FormCategoria(ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))
    parent = forms.ModelChoiceField(queryset=Categoria.objects.all(), label = 'Categoria Pai', widget=forms.Select(attrs={'class': 'form-control'} ))
    icone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }),  )
    in_flag = forms.BooleanField(label='Incidente?', widget=forms.CheckboxInput(attrs={'class': 'form-check'} ))
    cr_flag = forms.BooleanField(label='Solicitação?', widget=forms.CheckboxInput(attrs={'class': 'form-check'} ))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'rows': 5, 'cols': 30, 'class': 'form-control'}) )
    grupo_ca = forms.CharField(label = 'Grupo CA',widget=forms.TextInput(attrs={'class': 'form-control' } ) )
    persid_pcat_ca = forms.CharField( label='Categoria Persid CA',widget=forms.TextInput(attrs={'class': 'form-control' } ) )
    script = forms.CharField(label='Script automação',widget=forms.TextInput(attrs={'class': 'form-control' } ) )
    #last_date_mod = forms.DateField(label='Data da última alteração', disabled=True)
    class Meta:
        model = Categoria
        fields = '__all__'
        localized_fields  = '__all__'
        


class FormConfig(BaseForm):
    class Meta:
        model = Config
        fields = '__all__'