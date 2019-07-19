'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 2, степ 3
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# находим элементы
num1_in_text = browser.find_element_by_id("num1")
num2_in_text = browser.find_element_by_id("num2")

# вытаскиваем заданные числа 
num1 = int(num1_in_text.text)
num2 = int(num2_in_text.text)

# находим и выбираем значение, которое является суммой этих 2 чисел
select = Select(browser.find_element_by_class_name("custom-select"))
select.select_by_value(str(num1 + num2))

# нажимаем на кнопку
send_button = browser.find_element_by_class_name("btn-default")
send_button.click()
