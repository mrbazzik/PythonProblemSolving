from selenium import webdriver

test = True
chromedriver = 'C:\Users\Basov_il\Documents\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
while test:
	driver.get("https://monprojetquebec.immigration-quebec.gouv.qc.ca/_login/Micc/Intranet/ExternalRedirectToStstLogin.aspx?ReturnUrl=%2fFr%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252FFr%252FPages%252Fmondossier%252Easpx&Source=%2FFr%2FPages%2Fmondossier%2Easpx")
	source = driver.page_source.encode("utf-8") # Here is your populated data.
	
	if "Nous sommes" not in source:
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
		source = driver.page_source.encode("utf-8")
		if "Nous sommes" not in source:
			test = False    
