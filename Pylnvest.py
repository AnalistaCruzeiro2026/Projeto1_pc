import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'PT_BR.UTF-8')
#Entradas
capital = float(input('Capital_inicial: '))
aporte = float(input('Aporte_mensal: '))
meses = int(input('Prazo(messes): '))
cdi_anual = float(input('CDI anual (%) '))/100
perc_cdb = float(input('Percentual do CDI (%) '))/100
perc_lci = float(input('Percentual LCI (%) '))/100
taxa_fii = float(input('rendabilidade FII (%) '))/100
meta = float(input('Meta financeira (R$) '))

#Conversao CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12)-1

#TOTA_INVESTIDO
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow(1+ taxa_cdb), meses) + (aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_cdb
montante_lci = (capital * match.pow((1+ taxa_lci), meses) + (aporte * meses))

#POUPANÇA
taxa_poupança= 0.005
montante_poupança = (capital * math.pow((1+taxa_poupança),meses)+(aporte * meses))

#FII - SIMULAÇÕES
