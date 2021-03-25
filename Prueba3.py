from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
import time

from driver import GetDriver

driver = GetDriver()
load_dotenv()
code = os.environ.get('CODE_USER')
password = os.environ.get('PASSWORD_USER')
fieldcode = driver.find_element_by_xpath('//*[@id="username"]')
fieldcode.send_keys(code)
fieldpassword = driver.find_element_by_xpath('//*[@id="password"]')
fieldpassword.send_keys(str(password))
login = driver.find_element_by_xpath('//*[@id="boxForm"]/div/form/div[3]/button')
login.click()
time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="username"]')
    driver.find_element_by_xpath('//*[@id="password"]')
    print("HUBO UN ERROR EN EL LOGIN")
    driver.close()
except:
    print("NO HUBO UN ERROR EN EL LOGIN")

driver.get("https://campusvirtual.univalle.edu.co/moodle/course/view.php?id=464646")
isError = driver.find_element_by_xpath('//*[@id="region-main"]/div/div').text
if "No se puede encontrar registro de datos en la tabla course de la base de datos." in isError:
    print("HUBO UN ERROR BUSCANDO LA CLASE")
else:
    print("NO HUBO UN ERROR BUSCANDO LA CLASE")
driver.close()
