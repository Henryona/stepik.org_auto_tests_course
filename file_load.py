'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 2, 8 степ
'''
from selenium import webdriver
import os

# переход на нужную страницу
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# находим все нужные элементы на странице
name_field = browser.find_element_by_css_selector("[name='firstname']")
lastname_field = browser.find_element_by_css_selector("[name='lastname']")
email_field = browser.find_element_by_css_selector("[name='email']")
file_button = browser.find_element_by_css_selector("[type='file']")
send_button = browser.find_element_by_css_selector(".btn-primary")

# заполняем форму
name_field.send_keys("H")
lastname_field.send_keys("F")
email_field.send_keys("y")

# находим путь до текущей папки
current_dir = os.path.abspath(os.path.dirname(__file__))

# достраиваем его до пути до нужного файла
file_path = os.path.join(current_dir, "test_file.txt")

# посылаем этот файл 
file_button.send_keys(file_path)
send_button.click()
