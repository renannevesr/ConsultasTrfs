import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import Trf16

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

trf6 = 'https://pje1g.trf6.jus.br/consultapublica/ConsultaPublica/listView.seam'
trf5 = 'https://portalbi.trf5.jus.br/portal-bi/painel.html?id=3002'
trf4 = 'https://consulta.trf4.jus.br/trf4/controlador.php?acao=consulta_processual_pesquisa'
trf3 = 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam'
trf2 = 'https://balcaojus.trf2.jus.br/balcaojus/#/consultar'
trf1 = 'https://pje1g.trf1.jus.br/consultapublica/ConsultaPublica/listView.seam'

if __name__ == "__main__":
    list = 'lista.xlsx'
    idx = 0
    lista = []
    df = pd.read_excel(list)
    print(df.head())
    rows = df.shape[0]
    while idx < rows:
        print("idx do for=", idx)
        cpfId = df.loc[idx, 'CPF']
        Trf16.trf16_consulta(cpfId, trf1,trf6,driver)
        #trf16_consulta(cpfId)
        idx+=1
