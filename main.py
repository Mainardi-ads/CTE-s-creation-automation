from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


def conexao():
    driver = webdriver.Chrome()

    driver.get("https://cdsul.atua.com.br/adm/")
    sleep(1)

    def preencher_formulario():
        driver.find_element(By.ID, '3').send_keys('wkerber')
        sleep(1)

        driver.find_element(By.ID, '5').send_keys('unKBgUo3')
        sleep(1)

        submit_button = driver.find_element(By.ID, '4')
        submit_button.click()
        sleep(1)

    preencher_formulario()

    def selecionar_campo():
        emissao = driver.find_element(By.XPATH, '/html/body/center/table/tbody/tr[2]/td/div/ul/li[3]/a')
        emitir_ctrc = driver.find_element(By.XPATH, '/html/body/center/table/tbody/tr[2]/td/div/ul/li[3]/ul/li[14]/a')

        mouse = ActionChains(driver)

        mouse.move_to_element(emissao).perform()
        sleep(1)
        mouse.move_to_element(emitir_ctrc).click().perform()
        sleep(5)

    selecionar_campo()


conexao()
