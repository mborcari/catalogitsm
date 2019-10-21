from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Categoria, Propriedade, Config
from .forms import FormCategoria, FormPropriedade, FormConfig

def list_categorias_iniciais(request):
    '''
    View para index do catálogo comas categorias que não tem pais.
    '''
    categorias_retornadas = Categoria.objects.filter(parent__isnull=True)
    dados = {"categorias" : categorias_retornadas }
    return render(request, 'catalogo/index.html', dados)

def list_categorias(request, categoria_id):
    '''
    View para categorias filhas da categoria pai informada no argumento categoria_id.
    '''
    categorias_retornadas = Categoria.objects.filter(parent__id=categoria_id)
    dados = {"categorias" : categorias_retornadas }
    if categorias_retornadas.count() > 0:
        return render(request, 'catalogo/index.html', dados )
    else:
        propriedades_retornadas = Propriedade.objects.filter(categoria=categoria_id)
        dados = {"propriedades" : propriedades_retornadas }
        return render(request, 'catalogo/detail_cr.html', dados )

###### Detail da configuração de integração
def detail_config(request):
    config_retornadas = Config.objects.all()
    dados = {}
    dados["form"] = FormConfig
    dados["categorias"] = config_retornadas
    return render(request, 'catalogo/detail_config.html', dados )


###### View da configuração de categoria
def config_categoria(request):
    categorias_retornadas = Categoria.objects.all()
    dados = {}
    dados["form"] = FormCategoria
    dados["categorias"] = categorias_retornadas
    return render(request, 'catalogo/list_config_categoria.html', dados )

def detail_config_categoria(request, categoria_id):
    categoria_instance = Categoria.objects.get(pk=categoria_id)
    dados = {}
    dados["form"] = FormCategoria(instance=categoria_instance)
    return render(request, 'catalogo/detail_config_categoria.html', dados)



###### View da configuração de propriedade
def config_propriedade(request):
    propriedades_retornadas = Propriedade.objects.all()
    dados = {}
    dados["form"] = FormPropriedade
    dados["propriedades"] = propriedades_retornadas
    return render(request, 'catalogo/list_config_propriedade.html', dados )

def detail_config_propriedade(request, prop_id):
    prop_instance = Propriedade.objects.get(pk=prop_id)
    dados = {}
    dados["form"] = FormPropriedade(instance=prop_instance)
    return render(request, 'catalogo/detail_config_propriedade.html', dados)



def detail_cr(request, categoria_id):
    '''
    Tela de abertura de chamado
    '''
    return render(request, 'catalogo/detail_cr.html')

def carrega_categorias(request):
    '''
    Função para carregar as categorias usando csv
    '''
    path = 'C:\\Users\\matheus.santana\\OneDrive - MICROCITY\\mypython\\itsm\\csv\\'
    arquivo = 'carga_catalogo.csv'
    path_full = path + arquivo  
    import csv
    from sys import exc_info
    try:
        with open (path_full, encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter = ';')
            line_count = 0
            for row in reader:
                if line_count == 0:
                    line_count += 1
                    continue
                if row[0] and not row[2]:
                    object_temp = None
                    object_temp = Categoria(
                        nome = row[0],
                        icone = row[1],
                        parent = None,
                        in_flag = row[3],
                        cr_flag = row[4],
                        grupo_ca  = row [5],
                        id_ca = row[6],
                        script=row[7],
                        servico_final_flag = row[8]
                    )
                else:
                    ins_parent = Categoria.objects.get(nome=row[2])
                    object_temp = None
                    object_temp = Categoria(
                        nome = row[0],
                        icone = row[1],
                        parent = ins_parent,
                        in_flag = row[3],
                        cr_flag = row[4],
                        grupo_ca  = row [5],
                        id_ca = row[6],
                        script=row[7],
                        servico_final_flag = row[8]
                    )
                try:
                    object_temp.save()
                except Exception as e:
                    print(exc_info()[1])
                    print(e)
                finally:
                    line_count += 1
        categoria_inseridas = ", </BR>".join(cat.nome for cat in Categoria.objects.all())
        return HttpResponse('Carga de categorias realizada com sucesso: </BR>' +  categoria_inseridas)
    except Exception as e:
        print(exc_info()[1])
        return HttpResponse('Falha ao ler arquivo CSV: %s. Erro %s' % (arquivo, str(exc_info()[1])))

def deleta_categorias(request):
    from sys import exc_info
    from time import sleep
    try:
        categoria_deleta = ", </BR>".join(cat.nome for cat in Categoria.objects.filter(parent__isnull=False))
        Categoria.objects.filter(parent__isnull=False).delete()
        Categoria.objects.filter(parent__isnull=True).delete()
        return HttpResponse('Categorias deletas do banco de dados com sucesso: <BR>' + categoria_deleta)
    except Exception as e:
        return HttpResponse('Falha deletar categorias, erro: %s' % (str(exc_info()[1])) )
