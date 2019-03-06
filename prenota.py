import time
import re
from datetime import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


firefox = webdriver.Chrome()
firefox.get(" https://prenotaonline.esteri.it/login.aspx?cidsede=100068&ReturnUrl=/")
firefox.maximize_window()
pyautogui.press("f12")

login = firefox.find_element(By.XPATH, '//*[@id="BtnLogin"]')
login.click();
user = firefox.find_element(By.XPATH, '//*[@id="UserName"]')
user.send_keys('anitacdonato@gmail.com');
passwd = firefox.find_element(By.XPATH, '//*[@id="Password"]')
passwd.send_keys('Donato2311');

print("Por favor entre  e navegue ate o calendario para o agendamento!")
print("Boa Sorte! ")
time.sleep(2)
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print("Hora atual:", now)
hora = input("Insira Data e Hora! ")
while True:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    hora = hora
    now == hora
    print(now)
    if now >= hora:
        pyautogui.press("f5")
        print("ATUALIZADO F5", now)
        break

wait = WebDriverWait(firefox, 300000)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_acc_Calendario1_myCalendario1"]/table/tbody/tr[7]/td[4]')))
element.click();
print(now)
wait2 = WebDriverWait(firefox, 300000)
element2 = wait.until(EC.visibility_of_element_located((By.XPATH, "ctl00$ContentPlaceHolder1$acc_Calendario1$repFasce$ctl02$btnConferma")))
element2.click();
print(now)