from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
print(driver.find_element(By.ID, "clickOnMe").text)	#tu ustalamy po czym wyszukujemy 
print(driver.find_element_by_id("clickOnMe").text)
print(driver.find_element_by_name("fname").text)
print(driver.find_element_by_link_text("Visit W3Schools.com!").text)
print(driver.find_element_by_partial_link_text("sit W3Sc").text)
print(driver.find_element_by_class_name("topSecret").text)
print(driver.find_element_by_tag_name("a").text)
print(driver.find_element_by_tag_name("label").text)

# selektory css

print(driver.find_element_by_css_selector("a").text)	#lokalizuje selektor z tagiem a
print(driver.find_element_by_css_selector("img#smileImage").text)	#lokalizuje selektor z tagiem IMG O ID smileImage
print(driver.find_element_by_css_selector("p.topSecret").text)		#lokalizuje selektor z tagiem p z klasa topSecret
print(driver.find_element_by_css_selector("th:first-child").text)
print(driver.find_element_by_css_selector("th:nth-child(2)").text)  

print()
# szukanie elementu xpath
print(driver.find_element_by_xpath("//th").text)
print(driver.find_element_by_xpath("//tbody//th").text)
print(driver.find_element_by_xpath("//th[text()='Month']").text)
print(driver.find_element_by_xpath("//button[@id='clickOnMe']").text)
print()
print(driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table").text)

print(len(driver.find_elements_by_xpath("//th")))		#elementS

driver.quit()
