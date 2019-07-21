'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 1, раздел 5, 7 степ
'''
from selenium import webdriver

# перейдем на нужную страницу
link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

# поиск элементов и ввод тестовых данных
input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

# поиск кнопки по xpath и нажатие на нее
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()
