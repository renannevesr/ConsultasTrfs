# from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
def trf5_consulta(cpfId, trf5, driver, time, By):
    driver.get(trf5)
    cpf = str(cpfId)
    if len(cpf) == 9:
        cpf = "00"+cpf[:1] + "." + cpf[1:4] + "." + cpf[4:7] + "-" + cpf[7:]
    if len(cpf) == 10:
        cpf = "0"+ cpf[:2] + "." + cpf[2:5] + "." + cpf[5:8] + "-" + cpf[8:]
    if len(cpf) == 11:
        cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
    print(cpf)
    # Store iframe web element
    iframe = driver.find_element(By.XPATH,'/html/body/div/iframe')
    # switch to selected iframe
    driver.switch_to.frame(iframe)
    iframe2 = driver.find_element(By.XPATH, '// *[ @ id = "sheetFrame"]')
    driver.switch_to.frame(iframe2)
    loading = 0
    while loading ==0:
        try:
            loading1 = driver.find_element(By.XPATH,'//*[@id="content"]').get_attribute("innerHTML")
            #print(len(loading1))
        except:
            pass
        if len(loading1)> 29000:
            print(len(loading1))
            break
    box =driver.find_element(By.XPATH,'//*[@id="kVGuPBY_content"]/div/div/div/div/label[1]/input')
    driver.execute_script("arguments[0].click();", box)
    element =driver.find_element(By.XPATH,'//*[@id="jUVcvU_content"]/div/div/input')
    element.click()
    time.sleep(2)
    element.send_keys(cpf)
    #element.send_keys(cpf)
    btnSearch =driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/article/div[2]/div[5]/div/article/div[1]/div/div/div/button')
    for i in range (2):
        action = ActionChains(driver)
        action.double_click(btnSearch).perform()
    time.sleep(2)
    nome_lista = driver.find_elements(By.TAG_NAME,'span')
    len_list = len(nome_lista)
    if len_list>31:
        num_processos = int((len_list- 23)/ 9)
        print("num_processos=", num_processos)
    #print(nome_lista)
    #print("tam_nomes =",len(nome_lista))
        idx = 1
        while idx <= num_processos:
            process = 0
            classe_judicial = 0
            try:
                #//*[@id="PmHLLh_content"]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[4]/div/div/span
                classe_judicial = driver.find_element(By.XPATH,f'// *[ @ id = "PmHLLh_content"] / div / div[2] / div[1] / div / table / tbody / tr[{idx}] / td[6] / div / div / span').text
                process = driver.find_element(By.XPATH,f'//*[@id="PmHLLh_content"]/div/div[2]/div[1]/div/table/tbody/tr[{idx}]/td[4]/div/div/span').text
            except:
                print("saiu")
            try:
                classe_judicial = driver.find_element(By.XPATH,
                                                      f'// *[ @ id = "PmHLLh_content"] / div / div[2] / div / div / table / tbody / tr[{idx}] / td[6] / div / div / span').text
                process = driver.find_element(By.XPATH,
                                              f'//*[@id="PmHLLh_content"]/div/div[2]/div/div/table/tbody/tr[{idx}]/td[4]/div/div/span').text
            except:
                print("saiu2")

            print("process =", process, "classe = ", classe_judicial)
            idx+=1


    time.sleep(2)

