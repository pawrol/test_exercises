from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os		# moduł potrzebny do pobrania sciezki do pliku

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
driver.maximize_window()

elements = driver.find_elements_by_tag_name("input")		#sprawdzanie listy elementów czy wieksza od zera

if len(elements) == 1:
	print("element istnieje")
elif len(elements) == 0:
	print("nie isnieje")
else:
	print("wicej elementow")

#lub

try:							#jezeli wyjatek to element nie itnieje
	driver.find_element_by_tag_name("p")
	print("element istnieje")
except	NoSuchElementException:		
	print("element nie istnieje")
