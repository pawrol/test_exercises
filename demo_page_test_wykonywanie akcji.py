from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
driver.maximize_window()


click_me_button = driver.find_element_by_id("clickOnMe")
click_me_button.click()
driver.switch_to.alert.accept()			#akceptuje alert
click_me_button.click()
driver.switch_to.alert.dismiss()		#pomija alert

driver.find_element_by_id("fname").send_keys("pole tekst")	#wprowadzamy dane w pole tekst
print("to zostało wypisane: " + driver.find_element_by_id("fname").get_attribute("value"))	#wprowadzamy dane w pole tekst   zostały wypisane
driver.find_element_by_name("password").send_keys("123123123")
#driver.find_element_by_name("password").send_keys(Keys.ENTER)	#symulujemy przycisk enter(lub inne), trzeba zaimportowac klase Keys

auto_select = Select(driver.find_element_by_tag_name("select"))
auto_select.select_by_visible_text("Volvo")			#wybiera selecta z listy za pomocą tektu		
auto_select.select_by_value("saab")		#  to samo za pomocą value
auto_select.select_by_index(2)		#  to samo za pomocą indexu (numerowane od 0)

for i in range(10):
	driver.find_element_by_xpath("//input[@type='checkbox']").click()

driver.find_element_by_xpath("//input[@value='female']").click()
print(driver.find_element_by_xpath("//h1").text)		#wypisuje tekst z elementu h1
print(driver.find_element_by_id("clickOnMe").text)
print(driver.find_element_by_xpath("//p").text)		#element ukryty nie został pobrany
print(driver.find_element_by_xpath("//p").get_attribute("textContent"))	#element ukryty został pobrany

print(driver.find_element_by_id("smileImage").size.get("height"))		#sprawdzanie czy obrazek zaladowal sie na strone (musza byc rowne wysokosci)
print(driver.find_element_by_id("smileImage").get_attribute("naturalHeight"))

driver.find_element_by_id("newPage").click()

#driver.quit()
