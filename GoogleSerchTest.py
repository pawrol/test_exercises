from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("http://www.google.com")	
driver.maximize_window()
driver.set_window_size(1020, 300)
