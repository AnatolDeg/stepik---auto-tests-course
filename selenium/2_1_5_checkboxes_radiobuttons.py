from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_tag_name('input')
input.send_keys(y)

checkbox = browser.find_element_by_css_selector('input.form-check-input')
checkbox.click()

radio = browser.find_element_by_id('robotsRule')
radio.click()

button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()