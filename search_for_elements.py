from selenium import webdriver

# переходим на нужную страницу
link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

# ищем поля ввода и заполняем их текстовыми данными 
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
