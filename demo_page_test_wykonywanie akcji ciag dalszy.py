from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())  #instaluje sterownik (potrzebne doinstalowanie menagera)
driver.get("file:///C:/Users/Domo/Desktop/selenium/Test.html")	
driver.maximize_window()
driver.find_element_by_id("newPage").click()		#otwieramy nowa strone
print("jesteś teraz na stronie " + driver.title) #nie przałącza sie automatycznie na nowa strone

obecne_okno = driver.current_window_handle
wszystkie_okna  = driver.window_handles
print(obecne_okno)
print(wszystkie_okna)

for okno in wszystkie_okna:
	print("jesteś teraz na stronie " + driver.title) 
	if okno != obecne_okno:
		driver.switch_to.window(okno)		#zmienia skupienie na inne okno
	print("jesteś teraz na stronie " + driver.title) 
driver.switch_to.window(obecne_okno)
print("jesteś teraz na stronie " + driver.title) 
#driver.quit()
