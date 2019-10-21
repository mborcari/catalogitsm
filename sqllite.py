# -*- coding: utf-8 -*-
import sqlite3
from sys import exc_info
import io
import os

class bancoDeDados:
    ''' Classe para banco de dados mysql'''

    def __init__(self, nome='itsm.sqlite3'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        '''Metodo para conectar'''
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        '''Metodo para desconectar'''
        self.conexao.close()

    def consultar(self, statement):
        '''Metodo para consultar tabelas'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
            for linha in cursor.fetchall():
                print(linha)
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")

    def criar_tabelas(self, statement):
        '''Metodo para criar tabelas'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
        
    def inserir_valores(self, statement):
        '''Metodo para inserir valores na tabelas'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
            self.conexao.commit()
            #cursor.execute("commit;")
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
    
    def deleta_valores(self, statement):
        '''Metodo para deletar linhas'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
            self.conexao.commit()
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
    
    def backup_banco(self):
        try:
            with io.open('banco.sql', 'w') as f:
                for linha in self.conexao.iterdump():
                    f.write('%s\n' % linha)
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
         
statement = """
            CREATE TABLE IF NOT EXISTS CHAMADOS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                ref_num TEXT NOT NULL,
                cliente TEXT NOT NULL,
                metrica TEXT NOT NULL,
                data_avaliacao TEXT NOT NULL);
             """
statement3 =    '''
                INSERT INTO monitoramento_chamados (chamado, data_mon) VALUES ('IN187898', "22/09/2019 15:22:00");
                '''

select_chamados=   ''' 
                    select * from monitoramento_chamados;
                    '''

select_join =   '''
                    select pipeline.id, pipeline.nome, ambientes.nome, versao from pipeline
                    left outer join ambientes on ambientes.id = pipeline.ambiente;
                '''

delete =    '''    
            DELETE FROM PIPELINE WHERE ID=3;
            '''

dump = '''
        banco.db .dump > banco.sql;
        '''
#zstatemnt = input("digite o select:")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    banco =  bancoDeDados()
    banco.conecta()
    #banco.criar_tabelas(statement)
    banco.inserir_valores(statement3)
    banco.consultar(select_chamados)
    #banco.deleta_valores(delete)
    #banco.consultar(select_join)
    #cursor = banco.conexao.cursor()
    #banco.backup_banco()
    banco.desconecta()