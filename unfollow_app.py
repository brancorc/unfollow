from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

name="brancorc"
password_str="1622378459rcxd"
lista_seguidos=[]

driver_path = r"C:\Users\branc\Downloads\chromedriver-win64\chromedriver.exe"

option = webdriver.ChromeOptions()

option.add_argument('--window-size=1920x1080')
option.add_argument("--start-maximized")
option.add_argument('--charset=utf-8')
option.add_argument('--disable-gpu')
option.add_argument('--lang=es')  # Configura el idioma si es necesario
option.add_argument('--encoding=utf-8')  # Configura la codificación

# option.add_argument("--incognito") OPTIONAL
#option.add_argument("--headless") 

driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

def click_path(xpath): #espera a que aparezca el elemento y le da click

    try:
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, xpath))
            )
        
    finally:
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(1)

def esperar_path(xpath): #espera a que aparezca el elemento solamente xd

    try:
        element = WebDriverWait(driver, 350).until(
            EC.presence_of_element_located((By.XPATH, xpath))
            )
        
    finally:
        
        time.sleep(1)


driver.get("https://www.instagram.com/brancorc/")

click_path("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a") #boton iniciar sesion

click_path("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")#espera a que cargue el login

input_entrada = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
input_entrada.send_keys(name) #ingresa el nombre

password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys(password_str)

click_path("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div") #apreta boton login

click_path("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")#apreta el boton no guardar

click_path("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")#boton seguidos

time.sleep(5)

for i in range(1, 300):

    esperar_path("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[" + str(i) + "]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")
    
    seguido = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[" + str(i) + "]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")

    driver.execute_script("arguments[0].scrollIntoView();", seguido)

    lista_seguidos.append("https://www.instagram.com/" + seguido.text)

    print("seguidor numero:", i)

contador = 1

while True:

   entrada = input("Deseas dejar de seguir a esta persona?\nB = si\nM = no\nE = salir\nIngresa una letra: ") 

   if entrada == "e":
        break
   
   elif entrada == "b":

        click_path("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div/div[1]") #boton siguiendo
                     /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button/div/div[1]       
        click_path("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div/div/div") #boton dejar de seguir

        driver.get(lista_seguidos[contador])

   elif entrada == "m":

        driver.get(lista_seguidos[contador])

   contador += 1

   print("vas por el:,", contador)
