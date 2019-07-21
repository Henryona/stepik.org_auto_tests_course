from selenium import webdriver

# переходим на нужную страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

#  ищем элементы через find_elements_by
elements = browser.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("Мой ответ")

# нажимаем на кнопку
button = browser.find_element_by_css_selector("button.btn")
button.click()
