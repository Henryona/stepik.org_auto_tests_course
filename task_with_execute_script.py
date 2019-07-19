'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 2, степ 6
'''
from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# функция, которая находит значение выражения при заданном x 
def calc(x):
	return str ( math.log( abs( 12 * math.sin( int( x ) ) ) ) )
	
# находим значение x для выполнения задания
x_in_text = browser.find_element_by_id("input_value")
x_value = x_in_text.text

# считаем значение x
first_answer = calc(x_value)

# скроллим страницу до появления на ней поля ввода в зоне видимости
first_input = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", first_input)

# вводим ответ в поле ввода
first_input.send_keys(first_answer)

# выбираем checkbox
robotCheckbox = browser.find_element_by_id("robotCheckbox")
robotCheckbox.click()

# выбираем radiobutton
robotRadiobutton = browser.find_element_by_id("robotsRule")
robotRadiobutton.click()

# нажимаем кнопку отправить
send_button = browser.find_element_by_class_name("btn-default")
send_button.click()