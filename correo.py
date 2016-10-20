from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/adazeuq/Documentos/Box/Debian/pruebasSelenium/chromedriver")
driver.get('https://mail.google.com/mail/u/0/#inbox')
time.sleep(3)

elem = driver.find_element_by_name("Email")
elem.clear()
elem.send_keys("your_email@gmail.com")
elem.submit()
time.sleep(3)
elem = driver.find_element_by_name("Passwd")
elem.clear()
elem.send_keys("your_password")
elem.submit()
time.sleep(3)

encabezados = driver.find_elements_by_class_name('y6')

for a in encabezados:
    print u""+ a.find_element_by_tag_name('span').text
    time.sleep(1)
