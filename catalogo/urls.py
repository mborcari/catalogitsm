from django.urls import path, re_path, include
from . import views
app_name = 'catalogo'

urlpatterns = [
    re_path(r'^$', views.list_categorias_iniciais, name='list_categorias_iniciais'),
    re_path(r'(?P<categoria_id>^\d{2,20}$)', views.list_categorias, name='list_categorias'),
    re_path(r'^config$', views.detail_config, name='detail_config'),

    re_path(r'^config_categoria/(?P<categoria_id>\d+)', views.detail_config_categoria, name='detail_config_categoria'),
    re_path(r'^config_categoria', views.config_categoria, name='config_categoria'),
    
    re_path(r'^config_propriedade/(?P<prop_id>\d+)', views.detail_config_propriedade, name='detail_config_propriedade'),
    re_path(r'^config_propriedade', views.config_propriedade, name='config_propriedade'),
    

    re_path(r'^carrega_categorias', views.carrega_categorias),
    re_path(r'^deleta_categorias', views.deleta_categorias)
]