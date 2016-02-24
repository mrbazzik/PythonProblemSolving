from selenium import webdriver
import winsound
from selenium.webdriver.support.wait import WebDriverWait

winsound.Beep(500,1000) 

test = True
chromedriver = 'c:\Users\Home\Documents\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
while test:
	driver.get("https://monprojetquebec.immigration-quebec.gouv.qc.ca/Fr/Pages/mondossier.aspx")
		#https://monprojetquebec.immigration-quebec.gouv.qc.ca/_login/Micc/Intranet/ExternalRedirectToStstLogin.aspx?ReturnUrl=%2fFr%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252FFr%252FPages%252Fmondossier%252Easpx&Source=%2FFr%2FPages%2Fmondossier%2Easpx")
	load = True
	try:
		result = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("txt_nomUtilisateur") or ("Nous sommes" in x.page_source.encode("utf-8")))
	except:
		load = False
	source = driver.page_source.encode("utf-8") # Here is your populated data.
	if "Nous sommes" not in source and load:
		username = driver.find_element_by_id("txt_nomUtilisateur")
		password = driver.find_element_by_id("txt_motDePasse")

		username.send_keys("mrbazzik")
		password.send_keys("mpMOr10dvch")

		driver.find_element_by_name("btn_connecter").click()
		source = driver.page_source.encode("utf-8")

		if "votre question" in source:
			response = driver.find_element_by_id("txt_reponse")
			# print(source)
			if "Dans quelle ville a eu lieu mon mariage" in source:
				response.send_keys("Kaluga")
				driver.find_element_by_name("btn_suivant").click()
				print("Kaluga")
			elif "premier film" in source:
				response.send_keys("Godfather")
				driver.find_element_by_name("btn_suivant").click()
				print("Godfather")
			elif "lune de miel" in source:
				response.send_keys("Prague")
				driver.find_element_by_name("btn_suivant").click()
				print("Prague")
			else:
				test = False
				break
		result = WebDriverWait(driver, 30).until(lambda x: ("Nous sommes" in x.page_source.encode("utf-8")))
		source = driver.page_source.encode("utf-8")

		print("Nous sommes" in source)
		if "Nous sommes" not in source:
			test = False
winsound.Beep(2500,1000)    
