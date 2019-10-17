from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os		# moduł potrzebny do pobrania sciezki do pliku

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
driver.maximize_window()

pole = driver.find_element_by_id("fname")

if pole.is_enabled():			#jeżeli pole not enabled print enabled
	pole.send_keys("pole tekstowe")
else:
	print("disabled")
