from django.contrib import admin

# Register your models here.
from .models import Categoria, Propriedade


class CategoriaAdminInline(admin.TabularInline):
    model = Propriedade

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'parent', 'icone', 'in_flag', 'cr_flag',\
    'grupo_ca', 'persid_pcat_ca', 'script')
    list_filter = ('parent', 'in_flag', 'cr_flag', 'created_date', 'grupo_ca')
    inlines = [CategoriaAdminInline]

class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria',  'ordernacao', 'tipo', 'propriedade_pai','last_date_mod', 'created_date')
    list_filter = ('categoria', 'propriedade_pai')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Propriedade, PropriedadeAdmin)