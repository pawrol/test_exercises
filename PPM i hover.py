from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("https://www.w3schools.com/")	
driver.maximize_window()

element = driver.find_element_by_id("navbtn_examples")
hover = driver.find_element_by_id("navbtn_references")					
webdriver.ActionChains(driver).context_click(element).perform()	#symuluje prawy przycisk myszy

webdriver.ActionChains(driver).move_to_element(hover).click(hover).perform()	#przesuwamy sie na hover i klikamy na niego
