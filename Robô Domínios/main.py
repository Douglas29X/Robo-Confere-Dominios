from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import xlrd

print("Iniciando nosso robô...\n")

dominios = []

#Lendo do Excel
workbook = xlrd.open_workbook('dominio.xls') #não funciona mais com xlsx
sheet = workbook.sheet_by_index(0) #acessando a primeira planilha (caso tenha mais de uma, coloque o número respectivo)

for linha in range(0,5):
	dominios.append(sheet.cell_value(linha,0)) #esse metodo recebe a linha e a coluna

driver = webdriver.Chrome() #abre a guia do chrome pelo chromedriver
driver.get("https://registro.br") #abre o site

for dominio in dominios:

	pesquisa = driver.find_element_by_id("is-avail-field") #reconhece a barra de pesquisa pelo id
	pesquisa.clear() #caso tenha algo escrito na barrinha ele limpa
	pesquisa.send_keys(dominio) #digita
	pesquisa.send_keys(Keys.RETURN) #aperta enter

	time.sleep(8) #tempo necessário para o carregamento da página no meu sistema. Se o seu for melhor, pode diminuir
	resultados = driver.find_elements_by_tag_name("strong") #identifica se está disponível ou não

	with open('relatorio.csv', mode='a') as arquivo:
		arquivo.write(f"Domínio {dominio} {resultados[4].text}. Acesso em: {datetime.now()}\n")

time.sleep(3) #dorme (deixa a aba aberta) por x segundos

driver.close()
