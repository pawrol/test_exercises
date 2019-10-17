from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.implicitly_wait(10)			#czeka na załadowanie przeglądarki
driver.get("file:///C:/Users/Domo/Desktop/selenium/Waits2.html")	


button = driver.find_element_by_id("clickOnMe").click()
print(driver.find_element_by_tag_name("p").text)
