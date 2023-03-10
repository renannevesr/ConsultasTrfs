from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def trf16_consulta(cpfId,trf1,trf3,trf6,driver,time):
    pje = [trf1,trf3, trf6]
    for trf in pje:
        driver.get(trf)
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
            id_cases = 220
        else:
            div = 6
        driver.find_element(By.XPATH, f"/ html / body / div[{div}] / div / div / div / div[2] / form / div[1] / div / div / div / div / div[6] / div[2] / input").send_keys(cpfCorrigido)
        driver.find_element(By.XPATH, f"/ html / body / div[{div}] / div / div / div / div[2] / form / div[1] / div / div / div / div / div[8] / div / input").click()
        time.sleep(1)
        while lines_cpf>0:
            try:
                loading =len(driver.find_element(By.XPATH, f'/html/body/div[{div}]/div/div/div/div[2]/form/div[2]').get_attribute('innerHTML'))
                print(loading)
            except:
                loading = 0
            if loading ==0 or loading >1709:
                print("a")
                break
        if trf == 'https://pje1g.trf1.jus.br/consultapublica/ConsultaPublica/listView.seam':
            id_cases = 223

        else:
            id_cases = 230
        num_cases = driver.find_element(By.XPATH,f'/html/body/div[{div}]/div/div/div/div[2]/form/div[2]/div/table/tfoot/tr/td/div/div/span').text
        cases = num_cases[0]
        len_cases = 0
        try:
            print(int(cases))
            len_cases =int(cases)
        except:
            print("n??o achou nada")
        if len_cases >0:
            idx =1
            while idx <= len_cases:
                idx_character = 0
                processo = driver.find_element(By.XPATH,
                                               f"/html/body/div[{div}]/div/div/div/div[2]/form/div[2]/div/table/tbody/tr[{idx}]/td[2]")
                process_full =processo.text
                split_process =process_full.split("\n")
                partes = split_process[2]
                process = split_process[1]
                #print(process)
                for character in process:
                    ascii_c =ord(character)
                    idx_character+=1
                    if ascii_c > 47 and ascii_c < 58:
                        idx_character_end =idx_character +25
                        number_process =process[idx_character:idx_character_end]
                        tipo = process[idx_character_end+2:]
                        break
                print("|Partes =",partes)
                print("||N. do Processo =",number_process)
                print("|||Tipo do Processo =",tipo)
                idx +=1