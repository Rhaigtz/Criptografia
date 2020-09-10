from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

from selenium.webdriver.common.action_chains import ActionChains

DRIVER = webdriver.Chrome("N:\\Descargas\\chromedriver_win32\\chromedriver.exe")## Se debe cambiar a la ruta del chromedriver del dispositivo

def login(email, password):
    DRIVER.get("https://bamers.cl")
    login = DRIVER.find_element_by_class_name('login')
    if login.is_displayed() and login.is_enabled():
        login.click()
    else:
        DRIVER.find_element_by_id('mh-user').click()
        DRIVER.find_element_by_css_selector('div.mh-button.mh-user').find_element_by_tag_name('a').click()
    time.sleep(0.5)
    DRIVER.find_element_by_name('email').send_keys(email)
    DRIVER.find_element_by_name('passwd').send_keys(password)
    DRIVER.find_element_by_id('SubmitLogin').click()

def reset_password(email):
    DRIVER.get("https://bamers.cl")
    login = DRIVER.find_element_by_class_name('login')
    if login.is_displayed() and login.is_enabled():
        login.click()
    else:
        DRIVER.find_element_by_id('mh-user').click()
        DRIVER.find_element_by_css_selector('div.mh-button.mh-user').find_element_by_tag_name('a').click()
    time.sleep(0.5)
    DRIVER.find_element_by_class_name('lost_password').find_element_by_tag_name('a').click()
    time.sleep(0.5)
    DRIVER.find_element_by_id('email').send_keys(email)
    DRIVER.find_element_by_css_selector("button.btn.btn-default.button.button-medium").click()


def change_password(email, new_password, old_password):
    login(email,password)
    time.sleep(2)
    ul = DRIVER.find_element_by_class_name("myaccount-link-list").find_elements_by_tag_name('li')[3].find_element_by_tag_name('a').click()
    time.sleep(2)
    DRIVER.find_element_by_id('cookie_close').click()
    DRIVER.find_element_by_id('old_passwd').send_keys(old_password)
    DRIVER.find_element_by_id('passwd').send_keys(new_password)
    DRIVER.find_element_by_id('confirmation').send_keys(new_password)
    time.sleep(2)
    DRIVER.find_element_by_name('submitIdentity').click()


def create_account(email, password, name="Pedro", last_name="Picapiedra"):
    DRIVER.get("https://bamers.cl")
    login = DRIVER.find_element_by_class_name('login')
    if login.is_displayed() and login.is_enabled():
        login.click()
    else:
        DRIVER.find_element_by_id('mh-user').click()
        DRIVER.find_element_by_css_selector('div.mh-button.mh-user').find_element_by_tag_name('a').click()
    time.sleep(0.5)
    DRIVER.find_element_by_name('email_create').send_keys(email)
    DRIVER.find_element_by_name('SubmitCreate').click()
    WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.ID, "id_gender1"))).click()
    DRIVER.find_element_by_name('customer_firstname').send_keys(name)
    DRIVER.find_element_by_name('customer_lastname').send_keys(last_name)
    DRIVER.find_element_by_name('passwd').send_keys(password)
    select_day = DRIVER.find_element_by_id('days')
    select_months = DRIVER.find_element_by_id('months')
    select_years = DRIVER.find_element_by_id('years')
    select_day.find_elements_by_tag_name('option')[1].click()
    select_months.find_elements_by_tag_name('option')[1].click()
    select_years.find_elements_by_tag_name('option')[20].click()
    DRIVER.find_element_by_name('submitAccount').click()

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def automatize_login(attemps):
    for x in range(100):
        login('nopazog@gmail.com',get_random_string(15))
        print('Intento numero ', x,"\n")
    

password = ''
user = ''    
    
## FUNCIONES PARA EJECUTAR LOS DISTINTOS REQUERIMIENTOS DE LA TAREA, SOLO EJECUTAR 1 A LA VEZ
#login(user,password) #Iniciar sesion
#reset_password(user) #reestablecer contraseña
#change_password(user,password, password) #cambiar contraseña

#create_account(user,password) #crear cuenta

#automatize_login(100) # automatizar inicio de sesion.




