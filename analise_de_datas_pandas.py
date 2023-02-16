# Google Collab

from google.colab import auth
auth.authenticate_user()
import pandas as pd
from datetime import datetime
from datetime import date
import gspread
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds)

worksheet = gc.open('Untitled').worksheet("Contratos")
monthResults = gc.open('Untitled').worksheet("Resultados Mensais")

sheets = worksheet.get_all_values()
table = pd.DataFrame.from_records(sheets).transpose()

anos = ['2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029']
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
countano = 0
countmes = 1
count = 0
countnew = 0


for ano in anos:

  countano = countano+1  
  for mes in meses:

    if((count != 0) or (countnew != 0)):
      countmes = countmes+1

    countcancel = 0
    count = 0
    countnew = 0
    
    x = str(ano) + '-' + str(mes)+ '-1'
    y = (datetime.strptime(x, '%Y-%m-%d').date())

    for items in table:

      # Seta o inicio e o fim do contrato atual
      if (((table[items][1]) != '') & ((table[items][1]) != 'Inicio Contrato')):
        inicio = (datetime.strptime((table[items][1]), '%d/%m/%Y').date())
      else:
        inicio = None

      if(((table[items][2]) != '') & ((table[items][1]) != 'Inicio Contrato')):
        fim = (datetime.strptime((table[items][2]), '%d/%m/%Y').date())
      else:
        fim = None 

      # verifica se o contrato se encontra dentro da data atual
      if(type(inicio) != type(None)) & (type(fim) != type(None)):
        if((inicio < y) & ( fim > y )):
          count = count+1

      if(type(inicio) != type(None)) & (type(fim) == type(None)):
        if(inicio < y):
          count = count+1

      # verifica a data de cancelamento
      if(type(inicio) != type(None)) & (type(fim) != type(None)):
        if((y.month == fim.month) & (y.year == fim.year)):
          countcancel = countcancel+1

      # verifica a data de inico do contrato
      if(type(inicio) != type(None)):
        if((y.month == inicio.month) & (y.year == inicio.year)):
          countnew = countnew+1

    # quebra o codigo se chegar ao mes e ano de hoje
    if((y.month == ( 1 if datetime.now().month == 12 else datetime.now().month+1)) & (y.year == datetime.now().year)):
      break


    # envia para o sheets as informacoes geradas
    if((count != 0) or (countnew != 0)):
      # Data
      monthResults.update_cell(countmes+1, 1, str(y)) 
      # Clientes
      monthResults.update_cell(countmes+1, 2, str(count)) 
      # Cancelados
      monthResults.update_cell(countmes+1, 3, str(countcancel)) 
      # Novos
      monthResults.update_cell(countmes+1, 4, str(countnew))