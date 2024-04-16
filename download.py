from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import zipfile
import os.path
import time
import login

file_path = '/home/christofer/Aulao/dados/athlete_events.csv.zip'

options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/christofer/Aulao/dados/"}
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Ocultar alguns Logs, Bug de USB no ChromeDriver 88
options.add_experimental_option("prefs",prefs)
navegador = webdriver.Chrome(options=options)

navegador.get('https://www.kaggle.com/account/login?phase=startSignInTab&returnUrl=%2Faccount%2F')
navegador.maximize_window()

btn_email       = navegador.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div/div/div[1]/form/div/div/div[1]/button[2]/span')
btn_email.click()

sleep(1)
# input_email     = navegador.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/label[1]/input')
# input_password  = navegador.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/label[2]/input')
# btn_login       = navegador.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/div[2]/button[2]/span')

# input_email.send_keys('email@email.com.br')
# input_password.send_keys('senha')
# btn_login.click()

login.logar(navegador)

sleep(1)

btn_datasets    = navegador.find_element(By.XPATH, '//*[@id="site-container"]/div/div[3]/div[3]/div[1]/div[1]/ul/li[3]/div/a/div/div[2]/p')
btn_datasets.click()

sleep(1)

input_search    = navegador.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[4]/div/div/div[1]/div/input')
input_search.send_keys('heesoo37')

sleep(2)
div_120         = navegador.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[5]/div/div/div/ul/li[1]/div[1]/a/div')
div_120.click()

sleep(2)

body = navegador.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.PAGE_DOWN)

sleep(5)

down_csv        = navegador.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div/div[2]/div/div[5]/div[4]/div/div/div[1]/div/div[1]/div[1]/i')
down_csv.click()


while not os.path.exists(file_path):
    time.sleep(2)

if os.path.isfile(file_path):
    # Abre o arquivo zip chamado 'arquivo.zip' em modo de leitura
    with zipfile.ZipFile('athlete_events.csv.zip', 'r') as arquivo_zip:
        # Extrai todos os arquivos do arquivo zip para o diretório atual
        arquivo_zip.extractall()
else:
    raise ValueError("%s arquivo não existe!" % file_path)
