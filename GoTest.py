from selenium import webdriver
import winsound
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# document.getElementsByName('questionId')[0].value+", #"+document.getElementsByClassName('testQuestionText')[0].innerHTML

quests=[
517,#!'Какая функция SELF занимается вопросами поиска и выбора?',
514,#!'Этиология невроза в гештальт-терапии это:',
533,#'Экспрессивные техники в гештальт-терапии (по Наранхо) — это техники, цель которых:', 0,1,2
524,#!'Какой механизм сопротивления, согласно гештальт-терапии, прерывает цикл опыта на этапе встречи с объектом и проявляется у ребенка как уход в фантазии?', ЭГОТИЗМ!
519,#!'Чем определяется адекватность того или иного способа регуляции границ в гештальт-терапии?',0!
511,#!'Диагностический ключ в гештальт-терапии это:', ВСЕ!
535,#'В гештальт-терапии супрессивные техники /по Наранхо/ это:',0,1,2
504,#'Одна из задач Гештальт-терапии', 1,3
526,#!'Что такое профлексия?',ЦЕПЛЯЕТСЯ!
523,#'Как рассматривают сопротивление в гештальт-подходе?',2!
506,#!'Одним из основных понятий гештальт-терапии является',
522,#!'В чем состоит, согласно гештальт-терапии, цель фазы «пост-контакта»?',
529,#!'Техникой гештальт-терапии является:',
534,#'К экспрессивным техникам в гештальт-терапии (по Наранхо) можно отнести следующие технические приемы:',ПРЕУВЕЛИЧЕНИЕ!
537,#!'К супрессивным техникам гештальт-терапии можно отнести следующие:',
527,#'Что такое эготизм?', 0,1,2
508,#!'Как определяется понятие «Я» в теории гештальта?',
443,#!'Основные теоретические источники гештальт-терапии',
538,#!'К техникам интеграции в системе гештальт-терапии относятся:',ВСЕ! 2,3
518,#!'Какая функция SELF связана с идентификацией и с представлением о себе?',
532,#'С какой целью применяются телесно-ориентированные техники в гештальт-терапии?',0,1
520,#!'В чем состоит, согласно гештальт-терапии, цель фазы «преконтакта»?',
530,#!'Техникой гештальт-терапии является:',
521,#!'В чем состоит, согласно гештальт-терапии, цель фазы «полного контакта» ?',
509,#!'Как определяется в гештальт-терапии сознание:',
531,#!'Применяются ли в гештальт-терапии телесно-ориентированные техники?',ЧАСТО!
507,#!'Одним из основных понятий гештальт-терапии является',
539,#!'Возможные варианты работы со сновидениями в гештальт-терапии:',
525,#'Какой механизм сопротивления, согласно гештальт-терапии, прерывает цикл опыта на этапе пост-контакта и проявляется в том, что ребенок манипулирует другими, отстаивает свои права путем «ухода в болезнь»?', 2,3
515,#!'В каком режиме функционирует SELF?',
512,#'В чем состоит задача психотерапевта в гештальттерапии?', 0,1,2
528,#!'Модель цикла опыта по Гудману:',
513,#!'Какой вопрос психотерапевта соответствует духу гештальт-терапии:',
510,#!'Диагностическим ключом в гештальт-терапии может быть:', ВСЕ!
516,#!'Какая функция SELF проявляется в осознавании потребности?',
536,#'К супрессивным техникам гештальт-терапии можно отнести следующие:', ПЕРЕОБУЧЕНИЕ!
505#!'Какова основная методологическиая схема гештальт метода'
]

answers=[
1,
2,
2,
1,#3,1,2
0,#3,2,1,0
3,#0,1,2,3
1,
3,
1,
0,
3,
3,
0,
1,
0,
2,
2,
1,#1
2,
2,
0,
0,
1,
2,
0,
1,#1,0,2,3
3,
0,
3,#2,1,3,0
0,
0,
0,
1,
3,#1,3,2,0
0,
1,
2
]

winsound.Beep(500,300) 

test = True
chromedriver = 'c:/Users/VIA/Documents/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
driver.get("http://hi-psy.ru/elearning/test?id=11")
username = driver.find_element_by_id("signin_username")
password = driver.find_element_by_id("signin_password")
username.send_keys("")
password.send_keys("")
driver.find_element_by_id("signinForm").submit()
driver.get("http://hi-psy.ru/elearning/test?id=11&go=1")
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
