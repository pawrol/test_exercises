from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random import randrange

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
driver.maximize_window()
losowa_liczba = randrange(20)

element = driver.find_element_by_xpath("//input[@type='checkbox']")		

for i in range(losowa_liczba):
	element.click()

if element.is_selected():
	print("checkbox jest zaznaczony, odznaczam")
	element.click()
else:
	print("checkbox NIE jest zaznaczony, zaznaczam")
	element.click()
