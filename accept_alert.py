'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 3, 4 степ
'''
from selenium import webdriver
import math
import pyperclip
import time

# функция, которая находит значение выражения при заданном x 
def calc(x):
	return str( math.log (abs ( 12 * math.sin( x ) ) ) )  

# переход на нужную страницу
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# кликаем по волшебной кнопке
magic_button = browser.find_element_by_class_name("btn-primary")
magic_button.click()

# пока не "умеем" пользоваться нормальными ожиданиями
time.sleep(1)

# принимаем assert
alert = browser.switch_to.alert
alert.accept()

# находим значение x для выполнения задания
x_string = browser.find_element_by_id("input_value")
x_number = int( x_string.text )

# высчитываем результат для задания
answer = calc(x_number)

# находим поле ввода, вводим туда ответ
input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(answer)

# находим и нажимаем на кнопку
send_button = browser.find_element_by_class_name("btn-primary")
send_button.click()

# все еще не "умеем" пользоваться нормальными ожиданиями
time.sleep(1)

# ждём алерта, достаем из него текст
alert = browser.switch_to.alert
alert_text = alert.text

# вытаскиваем из текста алерта число, копируем в буфер обмена
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

