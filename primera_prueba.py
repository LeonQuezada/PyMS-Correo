from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/adazeuq/Documentos/Box/Debian/pruebasSelenium/chromedriver")
driver.get('http://www.google.com')
time.sleep(3)

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Hola mundo")
boton = driver.find_element_by_name('btnG').click()
#elem.send_keys(Keys.RETURN)
time.sleep(3)
resultados = driver.find_elements_by_class_name('r')
arefs = driver.find_element_by_tag_name('a')
print arefs


time.sleep(10)
driver.close()
