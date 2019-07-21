'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 3, 6 степ
'''
from selenium import webdriver
import pyperclip
import math

# функция, которая находит значение выражения при заданном x 
def calc(x):
	return str( math.log (abs ( 12 * math.sin( x ) ) ) )  

# переход на нужную страницу
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# нажимаем на кнопку
button = browser.find_element_by_class_name("btn-primary")
button.click()

# переходим на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# находим значение x для выполнения задания
x_string = browser.find_element_by_id("input_value")
x_number = int( x_string.text )

# высчитываем результат для задания
answer = calc(x_number)

# вводим ответ к тесту
input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(answer)

# нажимаем на кнопку
send_button = browser.find_element_by_class_name("btn-primary")
send_button.click()

# пока мы не "умеем" в нормлаьные ожидания 
time.sleep(1)

# переключаемся на alert, достаем текст алерта
alert = browser.swith_to.alert
alert_text = alert.text

# достаем из текста алерта число, копируем в буфер обмена
addToClipboard = alert_text.split(": ")[-1]
pyperclip.copy(addToClipboard)
