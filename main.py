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

def trfs_consulta(cpfId):
    pje = [trf1, trf6]
    for trf in pje:
        driver.get(trf)
        #print(pje)
        #print(cpfId)
        cpf = str(cpfId)
        lines_cpf = len(cpf)
        if lines_cpf == 10:
            cpfCorrigido = ['0', cpf[0], cpf[1], cpf[9], cpf[2],
                            cpf[3], cpf[4], cpf[8], cpf[5], cpf[6], cpf[7]]
        else:
            cpfCorrigido = [cpf[0], cpf[1], cpf[2], cpf[10], cpf[3],
                            cpf[4], cpf[5], cpf[9], cpf[6], cpf[7], cpf[8]]
        time.sleep(1)
        if trf == 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam':
            div = 5
        else:
            div = 6
        driver.find_element(By.XPATH, f"/ html / body / div[{div}] / div / div / div / div[2] / form / div[1] / div / div / div / div / div[6] / div[2] / input").send_keys(cpfCorrigido)
        driver.find_element(By.XPATH, f"/ html / body / div[{div}] / div / div / div / div[2] / form / div[1] / div / div / div / div / div[8] / div / input").click()
        time.sleep(6)
        if trf == 'https://pje1g.trf1.jus.br/consultapublica/ConsultaPublica/listView.seam':
            num_cases = driver.find_element(By.XPATH,'// *[ @ id = "fPP:processosTable:j_id223"] / div / span').text
        else:
            num_cases = driver.find_element(By.XPATH,'// *[ @ id = "fPP:processosTable:j_id230"] / div / span').text
        #print(num_cases)
        cases = num_cases[0]
        #print(cases)
        #print(type(cases))
        len_cases = 0
        try:
            print(int(cases))
            len_cases =int(cases)
            #print("len_cases",len_cases)
            #print("tipo lencases",type(len_cases))
        except:
            print("não achou nada")
        if len_cases >0:
            idx =1
            while idx <= len_cases:
                idx_character = 0
                processo = driver.find_element(By.XPATH,
                                               f"/html/body/div[6]/div/div/div/div[2]/form/div[2]/div/table/tbody/tr[{idx}]/td[2]")
                process =processo.text
                #print(process)
                split_process =process.split("\n")
                partes = split_process[2]
                for character in process:
                    ascii_c =ord(character)
                    idx_character+=1
                    if ascii_c > 47 and ascii_c < 58:
                        idx_character_end =idx_character +25
                        #print (idx_character)
                        number_process =process[idx_character:idx_character_end]
                        tipo = process[idx_character_end+2:]
                        #print("entrou if character")
                        break
                print("Partes =",partes)
                print("N. do Processo =",number_process)
                print("Tipo do Processo =",tipo)
                idx +=1
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
        trfs_consulta(cpfId)
        #trf1_BS(cpfId)
        idx+=1
