from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
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
def detail_config_integration(request):
    try:
        config_instanced = Config.objects.get(nome='DEFAULT')
    except Config.DoesNotExist:
        raise Http404("Configuração não encontrada.")
    if request.method == 'POST':
        form = FormConfig(request.POST, instance=config_instanced)
        if form.is_valid():
            form.save()
            return redirect('/')
    elif request.method == 'GET':
        form = {"form" : FormConfig(instance=config_instanced)}
        return render(request, 'catalogo/detail_config_integration.html', form)


###### View da configuração de categoria
def list_config_categoria(request):
    try:
        categorias_retornadas = Categoria.objects.all()
        dados = {"form" : FormCategoria, "categorias" : categorias_retornadas}
        return render(request, 'catalogo/list_config_categoria.html', dados )
    except Categoria.DoesNotExist:
        raise Http404("Falha ao recuperar registros no banco de dados.")

def detail_config_categoria(request, categoria_id):
    ''' Função para ver, atualizar ou deletar uma categoria.
    '''
    try:
        categoria_instanced = Categoria.objects.get(pk=categoria_id)
    except Categoria.DoesNotExist:
        raise Http404("Registro de categoria não existe.")
    # para atualizar
    if request.method == 'POST':
        form = FormCategoria(request.POST, instance=categoria_instanced)
        if form.is_valid():
            form.save()
            return redirect("catalogo:list_config_categoria" )
    # Para get
    elif request.method == 'GET':
        dados = {"form" : FormCategoria(instance=categoria_instanced), "categoria_id" : categoria_id }
        return render(request, 'catalogo/detail_config_categoria.html', dados)


def create_config_categoria(request):
    if request.method == 'POST':
        form = FormCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogo:list_config_categoria")
    elif request.method == 'GET':
        form = {"form" : FormCategoria}
        return render(request, 'catalogo/create_config_categoria.html', form)

def delete_config_categoria(request, categoria_id):
    ''' Função para deletar uma categoria.
    '''
    try:
        categoria_instanced = Categoria.objects.get(pk=categoria_id)
    except Categoria.DoesNotExist:
        raise Http404("Registro de categoria não existe.")
    # para atualizar
    if request.method == 'POST':
        categoria_instanced.delete()
        return redirect("catalogo:list_config_categoria" )

###### View da configuração de propriedade
def list_config_propriedade(request):
    propriedades_retornadas = Propriedade.objects.all()
    dados = {}
    dados["form"] = FormPropriedade
    dados["propriedades"] = propriedades_retornadas
    return render(request, 'catalogo/list_config_propriedade.html', dados )

def detail_config_propriedade(request, prop_id):
    try:
        prop_instanced = Propriedade.objects.get(pk=prop_id)
    except Categoria.DoesNotExist:
        raise Http404("Registro de categoria não existe.")
    if request.method == 'POST':
        form = FormPropriedade(request.POST, instance=prop_instanced)
        if form.is_valid():
            form.save()
            return redirect('catalogo:list_config_propriedade')
    elif request.method == 'GET':
        dados = {'form' : FormPropriedade(instance=prop_instanced), 'prop_id' : prop_id}
        return render(request, 'catalogo/detail_config_propriedade.html', dados)

def create_config_propriedade(request):
    if request.method == 'POST':
        form = FormPropriedade(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogo:list_config_propriedade")
    elif request.method == 'GET':
        form = {"form" : FormPropriedade}
        return render(request, 'catalogo/create_config_propriedade.html', form)

def delete_config_propriedade(request, prop_id):
    ''' Função para deletar uma categoria.
    '''
    try:
        prop_instanced = Propriedade.objects.get(pk=prop_id)
    except Propriedade.DoesNotExist:
        raise Http404("Registro da propriedade não existe.")
    if request.method == 'POST':
        prop_instanced.delete()
        return redirect("catalogo:list_config_propriedade" )


def detail_cr(request, categoria_id):
    '''
    Tela de abertura de chamado
    '''
    return render(request, 'catalogo/detail_cr.html')

def carrega_categorias(request):
 
    from os import getcwd, path
    print(__file__)
    print(path.abspath(__file__))
    print(path.dirname(path.abspath(__file__)))
    return
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
