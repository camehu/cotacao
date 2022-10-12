import matplotlib.pyplot as plt
import requisicao

moeda = requisicao.requisicao.json()
moedas_Tipo = ["DOLAR", "EURO", "BIT"]
Euro = []
dolar = moeda['USDBRL']['bid']
bit = moeda['BTCBRL']['bid']

Euro.append(moeda['EURBRL']['bid'])




