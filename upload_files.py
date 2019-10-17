from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os		# moduł potrzebny do pobrania sciezki do pliku

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/FileUpload.html")	
driver.maximize_window()

upload_input = driver.find_element_by_id("myFile")
file = os.path.abspath("C:/Users/Domo/Desktop/selenium/uploadMe.txt")

driver.save_screenshot("screenshots/screen0.png")		#screenshot1

upload_input.send_keys(file)

driver.save_screenshot("screenshots/screen1.png")		#screenshot2
