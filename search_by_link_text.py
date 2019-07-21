from selenium import webdriver
import math

# переходим на нужную страницу
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

# высчитываем номер ссылки, находим элемент по тексту ссылки
link_number = str (math.ceil (math.pow ( math.pi, math.e) * 10000 ) )
needed_link = browser.find_element_by_link_text(link_number)

# нажимаем на ссылку
needed_link.click()

# вводим данные
input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

# нажимаем на кнопку
button = browser.find_element_by_css_selector("button.btn")
button.click()
