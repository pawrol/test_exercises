from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os		# moduł potrzebny do pobrania sciezki do pliku

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
driver.maximize_window()

paragrapf = driver.find_element_by_tag_name("p")

if paragrapf.is_displayed():
	print("tekst not hidden")
	print(paragrapf.text)
else:
	print("tekst ukryty")
	print(paragrapf.get_attribute("textContent"))
