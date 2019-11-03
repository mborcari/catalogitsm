from django.contrib import admin

# Register your models here.
from .models import Categoria, Propriedade, Config


class CategoriaAdminInline(admin.TabularInline):
    model = Propriedade

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'parent', 'icone', 'figure', 'in_flag', 'cr_flag',\
    'grupo_ca', 'persid_pcat_ca', 'script')
    list_filter = ('parent', 'in_flag', 'cr_flag', 'created_date', 'grupo_ca')
    inlines = [CategoriaAdminInline]

class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria',  'ordernacao', 'tipo', 'propriedade_pai','last_date_mod', 'created_date')
    list_filter = ('categoria', 'propriedade_pai')

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CA_host',  'CA_port', 'CA_username', 'CA_password','CA_conn', 'LDAP_username', 'LDAP_password', 'LDAP_DN', 'last_date_mod')
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Propriedade, PropriedadeAdmin)
admin.site.register(Config, ConfigAdmin)