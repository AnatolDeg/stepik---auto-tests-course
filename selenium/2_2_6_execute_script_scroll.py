from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

button = browser.find_element_by_xpath("//button[@type='submit']")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.execute_script("window.scrollBy(0, 100);")

input = browser.find_element_by_id('answer')
input.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radio = browser.find_element_by_id('robotsRule')
radio.click()

button.click()