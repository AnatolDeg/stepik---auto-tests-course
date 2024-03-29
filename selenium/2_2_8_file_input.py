from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name('firstname')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name('lastname')
input2.send_keys("Petrov")
input3 = browser.find_element_by_name('email')
input3.send_keys("ddong@yandex.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

element = browser.find_element_by_name('file')
element.send_keys(file_path)

button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()
