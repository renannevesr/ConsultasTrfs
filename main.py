import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

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

def trf1_consulta():
    #time.sleep(2)
    driver.get(trf1)

    cpfCorrigido = [cpf[0], cpf[1], cpf[2], cpf[10], cpf[3], cpf[4], cpf[5], cpf[9], cpf[6], cpf[7], cpf[8]]
    driver.find_element(By.XPATH, '// *[ @ id = "fPP:dpDec:documentoParte"]').send_keys(cpfCorrigido)
    driver.find_element(By.XPATH, '// *[ @ id = "fPP:searchProcessos"]').click()
    time.sleep(2)
    print("chegou")
    try:
        not_found = driver.find_element(By.CLASS_NAME,'alert')
    except:
        pass
    btn_out = driver.find_elements(By.CLASS_NAME, '//a[namespace-uri()='http://www.w3.org/1999/xhtml'][')

    btn_out[1].click()

    len_btn = len(btn_out)
    print(len_btn)
    time.sleep(50)
    for i in range(len_btn):
        print("i=", i)
        #print(btn_out)
        bot_txt = btn_out[i].text
        print(bot_txt)

    time.sleep(3)
if __name__ == "__main__":
    list = 'lista.xlsx'
    idx = 0
    lista = []
    df = pd.read_excel(list)
    print(df.head())
    rows = df.shape[0]
    trf1_consulta()