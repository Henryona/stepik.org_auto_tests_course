from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/wait1.html"
browser.get(link)

button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text
