from selenium import webdriver
import winsound
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

winsound.Beep(500,300) 

test = True
chromedriver = 'C:\Users\Basov_il\Documents\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
while test:
	print("go")
	driver.get("https://monprojetquebec.immigration-quebec.gouv.qc.ca/Fr/Pages/mondossier.aspx")

	# driver.get("http://www.immigration-quebec.gouv.qc.ca/en/informations/mon-projet-quebec/")
	load = True
	try:
		result = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("txt_nomUtilisateur") or x.find_element_by_class_name("micclien"))
	except:
		load = False
	print("go1")
	source = driver.page_source.encode("utf-8") 
	if ("Nous sommes" not in source) and load:
		username = driver.find_element_by_id("txt_nomUtilisateur")
		password = driver.find_element_by_id("txt_motDePasse")

		username.send_keys("mrbazzik")
		password.send_keys("mpMOr10dvch")

		driver.find_element_by_name("btn_connecter").click()
		source = driver.page_source.encode("utf-8")

		if "votre question" in source:
			response = driver.find_element_by_id("txt_reponse")
			if "Dans quelle ville a eu lieu mon mariage" in source:
				response.send_keys("Kaluga")
				driver.find_element_by_name("btn_suivant").click()
				
			elif "premier film" in source:
				response.send_keys("Godfather")
				driver.find_element_by_name("btn_suivant").click()
				
			elif "lune de miel" in source:
				response.send_keys("Prague")
				driver.find_element_by_name("btn_suivant").click()
			else:
				test = False
				break
		result = WebDriverWait(driver, 30).until(lambda x: x.find_element_by_class_name("micclien"))
		source = driver.page_source.encode("utf-8")
		print("Nous sommes" in source)
		if "Nous sommes" not in source:
			test = False
winsound.Beep(2500,300)    
