'''
autor: Lucas de Matos Silva
email: lucas.matos.silva@icloud.com
data: 11 de junho de 2019
'''
from flask import Flask, render_template
from lib import DadosAbertos
from pymongo import MongoClient
import datetime
list_dep = DadosAbertos()

print ("BEM VINDO!")
print (" ")
print ("AGUARDE, CARREGANDO DADOS...")
print (" ")

app = Flask(__name__)


# Conexao ao mongoDB
conn = MongoClient('mongodb', 27017)

# Conexao ao database
banco = conn['projetoDep']

# Conexao a tabela de banco de dados
table = banco['deputados']


@app.route("/")
def deputados():
   list_dep = []
   for dep in table.find():
       list_dep.append(dep)
   
   return render_template('lista.html', listas=list_dep)

@app.route("/gastos/<id>")
def deputado(id):
   obj    = DadosAbertos()
   info   = obj.deputado_id(id)
   gastos = obj.deputado_despesas(id)
   valorGasto = 0
   valores = {}
   for gasto in gastos:
       
       valorGasto += round(float(gasto['valorLiquido']),2)
       data = str(gasto['mes']) + '/' + str(gasto['ano'])

       if data in valores:
          valores[data] += gasto['valorLiquido']    
       else:
          valores[data] = gasto['valorLiquido']   
       
   line_labels = valores.keys()
   line_values = valores.values()
    
   return render_template('gastos.html', title='Gráfico de Gastos', max= round(valorGasto,0), labels=line_labels, values=line_values, listaGastos=gastos, totalGasto=round(valorGasto,2))

@app.route("/orgaos/<id>")
def eventos(id):
   obj    = DadosAbertos()
   info   = obj.deputado_id(id)
   orgaos = obj.deputado_orgaos(id)

   return render_template('orgaos.html', listas=orgaos)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)