from selenium import webdriver
from selenium.webdriver.common.by import By

def logar(driver):
    try:
        with open('user.txt', 'r') as file:
            for details in file:
                email, password = details.split(':')

            email_login= driver.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/label[1]/input')
            email_login.send_keys(email)

            senha_login = driver.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/label[2]/input')
            senha_login.send_keys(password)

            entrar_button= driver.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/div[2]/button[2]/span')
            entrar_button.click()
    except:
        print('Arquivo user.txt não encontrado')
        raise