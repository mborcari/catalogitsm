# Generated by Django 2.2.5 on 2019-10-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='figure',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='icone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='config',
            name='CA_conn',
            field=models.CharField(choices=[('http://', 'http'), ('https://', 'https')], default='http', max_length=10, verbose_name='CA Procotolo'),
        ),
        migrations.AlterField(
            model_name='config',
            name='CA_host',
            field=models.CharField(max_length=50, verbose_name='CA Host'),
        ),
        migrations.AlterField(
            model_name='config',
            name='CA_password',
            field=models.CharField(default=None, max_length=50, verbose_name='CA Password'),
        ),
        migrations.AlterField(
            model_name='config',
            name='CA_port',
            field=models.IntegerField(default=8050, verbose_name='CA Porta'),
        ),
        migrations.AlterField(
            model_name='config',
            name='CA_username',
            field=models.CharField(default=None, max_length=50, verbose_name='CA Username'),
        ),
        migrations.AlterField(
            model_name='config',
            name='LDAP_DN',
            field=models.CharField(default=None, max_length=100, verbose_name='LDAP DN'),
        ),
        migrations.AlterField(
            model_name='config',
            name='LDAP_password',
            field=models.CharField(default=None, max_length=50, verbose_name='LDAP Passowrd'),
        ),
        migrations.AlterField(
            model_name='config',
            name='LDAP_username',
            field=models.CharField(default=None, max_length=50, verbose_name='LDAP Username'),
        ),
        migrations.AlterField(
            model_name='config',
            name='last_date_mod',
            field=models.DateTimeField(auto_now=True, verbose_name='Última data de alteração'),
        ),
    ]