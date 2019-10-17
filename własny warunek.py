from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait  	#zaimportowac klase podczas uzyuwania explicit wait
from selenium.webdriver.support	import expected_conditions
from selenium.webdriver.common.by	import By


driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)

wait = WebDriverWait(driver, 10, 0.5) 	# 4 warunki 1driver 	2timeout  	3częstotliwość sprawdzania warunku zefiniowanego   4ignorowane wyjątki

driver.get("file:///C:/Users/Domo/Desktop/selenium/Waits2.html")	

driver.find_element_by_id("clickOnMe").click()
wait.until(lambda wd: len(wd.find_elements_by_tag_name("p")) == 1)
print(driver.find_element_by_tag_name("p").text)
 
