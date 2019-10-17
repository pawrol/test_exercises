from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
driver.maximize_window()
driver.execute_script("arguments[0].click();",driver.find_element_by_id("newPage"))	#klikanie elementu za pomocą java script

wartosc = 'pole tekstowe'
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc +"')", driver.find_element_by_id("fname"))
