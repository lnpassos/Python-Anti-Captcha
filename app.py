from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
import time

'''

Deixo aqui minha Key utilizada no projeto para testes, peço por favor que use apenas para verificar o funcionamento do código,
pois, isso ajudará que novas pessoas que tenham interesse possam verificar também.
Gastei $10 em créditos, sendo $0.7 para 1000 verificações, acho justo deixar aqui mostrando que está funcionando corretamente.
Obrigado!
ATT, Leonardo.

'''

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://google.com/recaptcha/api2/demo'
api_key = '45a35b17a043dd4df75910b98eda7734'
captcha_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'

navegador.get(link)
navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(api_key)
solver.set_website_url(link)
solver.set_website_key(captcha_key)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)


time.sleep(10)