# -*- coding: utf-8 -*-
from selenium import webdriver
import time


driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()

driver.get('http://www.devbridge.com/sourcery/components/jquery-autocomplete/')

time.sleep(0.5)

"""
Simula el comportamiento del navegador al presionar las teclas 'u' y 's' en el input text
dinamicamente
"""
driver.find_element_by_id('autocomplete-countries').send_keys("us")

"""
Obtiene los resultados sugeridos
"""
items = driver.find_elements_by_class_name('autocomplete-suggestion')
for item in items:
	print item.text

time.sleep(5)

driver.quit()

