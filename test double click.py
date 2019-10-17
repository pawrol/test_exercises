from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/DoubleClick.html")	
driver.maximize_window()

button = driver.find_element_by_id("bottom")					# symulowanie podwojnego kliknięcia 
webdriver.ActionChains(driver).double_click(button).perform()
