from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")	
driver.maximize_window()

small_element = driver.find_element_by_id("draggable")
big_element = driver.find_element_by_id("droptarget")
					
webdriver.ActionChains(driver).drag_and_drop(small_element, big_element).perform()	

