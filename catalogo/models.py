from django.db import models


class AbstractEntity(models.Model):
    ''' Infomações e campos comuns para as classes.
    '''
    nome = models.CharField(max_length=200, name='nome')
    last_date_mod = models.DateTimeField(auto_now=True, \
        verbose_name='Data de alteração')
    created_date = models.DateTimeField(auto_now_add=True, \
        verbose_name='Data de criação')

    class Meta:
        abstract = True
        ordering = ['nome']

    def __str__(self):
        return self.nome
        
class Categoria(AbstractEntity):
    '''
    Define as categorias de serviço ITSM. As categoria são organizadas de forma \
    hierarquica. Categorias finais, são categorias que definem o serviço e que \
    tem o persid da categoria do CA SDM.
    '''
    icone = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, \
        blank=True, null=True)
    in_flag = models.BooleanField(default=False, help_text='É valido para incidente?', \
        verbose_name='Incidente?')
    cr_flag = models.BooleanField(default=False, help_text='É valido para solicitação?', \
        verbose_name='Solicitação?')
    descricao = models.TextField(blank=True, null=True)
    grupo_ca = models.CharField(max_length=70, blank=True, null=True,\
        help_text="Grupo de atendimento no CA SDM")
    persid_pcat_ca = models.CharField(max_length=20, blank=True, null=True, \
        verbose_name='Categoria CA', help_text="Persid da categoria CA SDM")
    script = models.CharField(max_length=255, blank=True, null=True, \
        verbose_name='script', help_text="Script de automação da categoria")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("catalogo:detail_config_categoria", args=[str(self.id)] )
    
class Propriedade(AbstractEntity):
    '''
    Classe que define as propriedades de uma categoria de serviço. São os \
    campos adicionais no formulário web.
    '''
    nome = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    obrigatorio = models.IntegerField(default=0)
    propriedade_pai = models.ForeignKey('self', on_delete=models.SET_NULL, \
        blank=True, null=True)
    LISTA_TIPO = ( 
    ('str', 'Texto'), 
    ('num','Número'),
    ('dta', 'Data'),
    ('eml', 'Email'),
    ('chk', 'Checkbox')
    )
    tipo = models.CharField(max_length=3, choices=LISTA_TIPO)
    tamanho = models.IntegerField(default=1)
    ordernacao = models.IntegerField(help_text='Define a ordem de exibição do \
        campo no formulário de chamado', verbose_name="Ordenação do campo")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("catalogo:detail_config_propriedade", args=[str(self.id)])
    
    class Meta:
        ordering = ['ordernacao']

class Config(models.Model):
    '''
        Define as configurações de integração com o CASDM via REST. Define\
        também as configuraçõe de integração com AD.
    '''
    nome = models.CharField(max_length=200, name='nome', default="Configuração")
    CA_host = models.CharField(max_length=50)
    CA_port = models.IntegerField(default=8050)
    CA_username = models.CharField(max_length=50, default=None)
    CA_password = models.CharField(max_length=50, default=None)
    LISTA_HTTP = (
     ('http://', 'http'),
    ('https://', 'https')
    )
    CA_conn = models.CharField(max_length=10, choices=LISTA_HTTP, default="http")
    LDAP_username = models.CharField(max_length=50, default=None)
    LDAP_password = models.CharField(max_length=50, default=None)
    LDAP_DN = models.CharField(max_length=100, default=None)
    last_date_mod = models.DateTimeField(auto_now=True)
    
    def ca_url_endpoint(self):
        return "%s%s:%s/rest_access/" % (tipo, host, port)

    class Meta:
        verbose_name = 'Configuração'

    def __str__(self):
        return self.nome


# class LogIntegracao(models.Model):
#     LISTA_ACAO = ( 
#     ('post', 'Criação de registro'), 
#     ('put','Atualização de registro'),
#     )
#     acao = models.CharField(choices=LISTA_ACAO)
#     body = models.textField()
#     usuario = models.CharField(max_length=200)
#     created_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.acao