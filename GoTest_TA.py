from selenium import webdriver
import winsound
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# document.getElementsByName('questionId')[0].value+", #"+document.getElementsByClassName('testQuestionText')[0].innerHTML


quests=[
488, #Для "синдрома выгорания" специалиста&nbsp; (Burnout syndrom) характерно:
475, #В каком Эго-состоянии происходит истинное перерешение?
472, #Что является основным методом терапевтической работы со сценарием?
444, #Кто является современным последователем&nbsp; Э.Берна?
495, #Практические&nbsp; методики ТА: 
460, #Трансакции - это:
498, #Построение и анализ геносоциограмм&nbsp; - это: 
480, #В каком возрасте закладывается первичная личностная адаптация?
451, #Кто такой Маленький Профессор?
502, #ТА включает в себя:
446, #Где находится международная ассоциация ТА?
484, #Укажите причину&nbsp; обесценивания:
479, #Одна из важнейших характеристик терапевтической группы в ТА:
496, #В ТА не применяется: 
500, #Назовите основные цели ТА - терапии:
449, #В&nbsp; структурную&nbsp; модель Эго-состояний не&nbsp; входит:
456, #Строк-центрированный ТА основан на:
474, #Выделите основной драйвер:
477, #Игровое поведение характеризуется:
485, #Какой адаптации наиболее присущ драйвер "Будь сильным"?
499, #К навыкам работы с психотическими клиентами в ТА относится: 
490, #Автономность&nbsp; личности характеризуется:
471, #Какое из нижеперечисленных предписаний является токсичным?
457, #Кто выдвинул "теорию привязанностей"?
461, #Кто автор книги "Игры, в которые играют люди"?
482, #Какой тип адаптации называют "очаровательный манипулятор"?
467, #Сколько аутентичных чувств рассматривает ТА:
447, #Один из основополагающих методов в ТА:
476, #Причина игр:
463, #Что такое “ Игра” в ТА? 
493, #Спонтанность – это:
450, #Функциональная модель&nbsp; детского эго-состояния&nbsp; не включает понятие:
466, #Отметьте вид пассивного поведения:
455, #Выделите тип пересекающихся трансакций: 
445, #Из какого психотерапевтического метода&nbsp;&nbsp; вырос ТА?
492, #Интимность – это:
483, #Что такое “ обесценивание”? 
487, #Что является "открытой дверью" для шизоидной адаптации?
454, #Какие трансакции наиболее просты и неконфликтны?
468, #Выберите "рэкетное" чувство
489, #Что такое "Терапевт в кармане"?
501, #Сертифицированный ТА – терапевт и консультант имеет опыт: 
470, #Когда принимается "сценарий"?
448, #Эго-состояние это:
464, #Укажите один&nbsp; из&nbsp; способов выхода из игры:
494, #Автономность – это:
491, #Осознавание – это:
469, #Что понимается в ТА под термином "сценарий"?
458, #Отметьте существующие виды поглаживаний:
473, #Для чего нужны контрпредписания?
503, #Назовите противопоказания к применению&nbsp; ТА : 
497, #В ТА&nbsp; применяются: 
462, #Автор концепции "драматического треугольника":
459, #Сколько существует вариантов структурирования времени по ТА?
481, #Выделите вторичную личностную адаптацию:
486, #Какое описание наиболее соответствует истерической адаптации?
452, #Кто впервые предложил использовать Эго-грамму?
465, #Симбиоз – это:
478, #Выберите &nbsp;тип групп в ТА:
453 #Выделите нарушение в Эго-грамме:
]








answers=[
1,#0
1,#0
2,#1
1,#1
2,#!
2,#2
0,#!
1,#!
1,
2,
1,#!
0,#!
2,#!
2,
0,
2,
1,#!
2,
1,#1
1,
2,#!
2,
0,
2,
1,
2,
1,#!
0,
1,
2,
0,
1,
0,
0,
0,
0,
0,#0
2,#!
1,
1,
1,
2,
0,
1,
2,
2,
2,
1,
0,
1,#!
1,
0,#!
0,
1,#!
2,
2,
1,
0,
0,#!
2
]



test = True
#chromedriver = 'c:/Users/VIA/Documents/chromedriver_win32/chromedriver.exe'
chromedriver = 'C:/Users/Basov_il/Documents/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
driver.get("http://hi-psy.ru/elearning/test?id=12")
username = driver.find_element_by_id("signin_username")
password = driver.find_element_by_id("signin_password")
username.send_keys("")
password.send_keys("")
driver.find_element_by_id("signinForm").submit()
driver.get("http://hi-psy.ru/elearning/test?id=12&go=1")
form = driver.find_element_by_id("questionForm")
while form:
	text = driver.find_element_by_class_name("testQuestionText").text
	qId = driver.find_element_by_name("questionId").get_attribute('value')
	print(qId)
	try:
		ind = quests.index(int(qId))
	except:
		ind=-1
	print(ind)
	if ind!=-1:
		rad0 = driver.find_element_by_id("radio-0")
		driver.execute_script('arguments[0].removeAttribute("checked");', rad0)
		par = rad0.find_element_by_xpath('..')
		driver.execute_script('arguments[0].classList.remove("r_on");', par)

		rad = driver.find_element_by_id("radio-"+str(answers[ind]))
		driver.execute_script('arguments[0].setAttribute("checked","");', rad)
		par = rad.find_element_by_xpath('..')
		driver.execute_script('arguments[0].classList.add("r_on");', par)
		form.submit()
		form = driver.find_element_by_id("questionForm")
	else:
		form = False
winsound.Beep(500,300) 







	# driver.get("http://www.immigration-quebec.gouv.qc.ca/en/informations/mon-projet-quebec/")
# 	load = True
# 	try:
# 		result = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("txt_nomUtilisateur") or x.find_element_by_class_name("micclien"))
# 	except:
# 		load = False
# 	print("go1")
# 	source = driver.page_source.encode("utf-8") 
# 	if ("Nous sommes" not in source) and load:
# 		username = driver.find_element_by_id("txt_nomUtilisateur")
# 		password = driver.find_element_by_id("txt_motDePasse")

# 		username.send_keys("mrbazzik")
# 		password.send_keys("mpMOr10dvch")

# 		driver.find_element_by_name("btn_connecter").click()
# 		source = driver.page_source.encode("utf-8")

# 		if "votre question" in source:
# 			response = driver.find_element_by_id("txt_reponse")
# 			if "Dans quelle ville a eu lieu mon mariage" in source:
# 				response.send_keys("Kaluga")
# 				driver.find_element_by_name("btn_suivant").click()
				
# 			elif "premier film" in source:
# 				response.send_keys("Godfather")
# 				driver.find_element_by_name("btn_suivant").click()
				
# 			elif "lune de miel" in source:
# 				response.send_keys("Prague")
# 				driver.find_element_by_name("btn_suivant").click()
# 			else:
# 				test = False
# 				break
# 		result = WebDriverWait(driver, 30).until(lambda x: x.find_element_by_class_name("micclien"))
# 		source = driver.page_source.encode("utf-8")
# 		print("Nous sommes" in source)
# 		if "Nous sommes" not in source:
# 			test = False
# winsound.Beep(2500,300)    
