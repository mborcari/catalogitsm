# Generated by Django 2.1.5 on 2019-10-21 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('last_date_mod', models.DateTimeField(auto_now=True, verbose_name='Data de alteração')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('icone', models.CharField(blank=True, max_length=200)),
                ('in_flag', models.BooleanField(default=False, help_text='É valido para incidente?', verbose_name='Incidente?')),
                ('cr_flag', models.BooleanField(default=False, help_text='É valido para solicitação?', verbose_name='Solicitação?')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('grupo_ca', models.CharField(blank=True, help_text='Grupo de atendimento no CA SDM', max_length=70, null=True)),
                ('persid_pcat_ca', models.CharField(blank=True, help_text='Persid da categoria CA SDM', max_length=20, null=True, verbose_name='Categoria CA')),
                ('script', models.CharField(blank=True, help_text='Script de automação da categoria', max_length=255, null=True, verbose_name='script')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.Categoria')),
            ],
            options={
                'ordering': ['nome'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Configuração', max_length=200)),
                ('CA_host', models.CharField(max_length=50)),
                ('CA_port', models.IntegerField(default=8050)),
                ('CA_username', models.CharField(default=None, max_length=50)),
                ('CA_password', models.CharField(default=None, max_length=50)),
                ('CA_conn', models.CharField(choices=[('http://', 'http'), ('https://', 'https')], default='http', max_length=10)),
                ('LDAP_username', models.CharField(default=None, max_length=50)),
                ('LDAP_password', models.CharField(default=None, max_length=50)),
                ('LDAP_DN', models.CharField(default=None, max_length=100)),
                ('last_date_mod', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Configuração',
            },
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_date_mod', models.DateTimeField(auto_now=True, verbose_name='Data de alteração')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('obrigatorio', models.IntegerField(default=0)),
                ('tipo', models.CharField(choices=[('str', 'Texto'), ('num', 'Número'), ('dta', 'Data'), ('eml', 'Email'), ('chk', 'Checkbox')], max_length=3)),
                ('tamanho', models.IntegerField(default=1)),
                ('ordernacao', models.IntegerField(help_text='Define a ordem de exibição do         campo no formulário de chamado', verbose_name='Ordenação do campo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Categoria')),
                ('propriedade_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.Propriedade')),
            ],
            options={
                'ordering': ['ordernacao'],
            },
        ),
    ]