# -*- encoding: utf-8 -*-
from selenium import webdriver
test = True
chromedriver = 'C:\Users\Basov_il\Documents\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Firefox() # You can replace this with other web drivers
while test:
	driver.quit() # don't forget to quit the driver!
	#driver = webdriver.Firefox() # You can replace this with other web drivers
	driver = webdriver.Chrome(chromedriver)
	driver.get("https://monprojetquebec.immigration-quebec.gouv.qc.ca/_login/Micc/Intranet/ExternalRedirectToStstLogin.aspx?ReturnUrl=%2fFr%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252FFr%252FPages%252Fmondossier%252Easpx&Source=%2FFr%2FPages%2Fmondossier%2Easpx")
	source = driver.page_source.encode("utf-8") # Here is your populated data.
	test = ("Nous sommes" in source) #or ("Request unsuccessful" in source) or ("Retry Button" in source) or ("name=""robots""" in source) or ("name=""ROBOTS""" in source) or ("<html xmlns=""http://www.w3.org/1999/xhtml""><head></head><body></body></html>" in source)
	if not test:
		username = driver.find_element_by_id("txt_nomUtilisateur")
		password = driver.find_element_by_id("txt_motDePasse")
		# test = selenium.find_element_by_id("txt_motDePasse1")
		# print("test: %s"%(test))

		username.send_keys("mrbazzik")
		password.send_keys("mpMOr10dvch")

		driver.find_element_by_name("btn_connecter").click()
		source = driver.page_source.encode("utf-8")

		test = ("Nous sommes" in source)

    #print(source)
    #print("<html xmlns=""http://www.w3.org/1999/xhtml""><head></head><body></body></html>" in source)
    #print("Retry Button" in source)
    #print("name=""robots""" in source)
    #print("Ошибка при установлении" in source)
    #print("Nous sommes" in source) 
    #print("Request unsuccessful" in source)
    
