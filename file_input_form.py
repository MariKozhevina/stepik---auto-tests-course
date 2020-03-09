import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

input1 = driver.find_element_by_name("firstname")
input1.send_keys("Maria")

input2 = driver.find_element_by_name("lastname")
input2.send_keys("Kozhevina")

input3 = driver.find_element_by_name("email")
input3.send_keys("Smolensk@gmail.com")



current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла
print(file_path)

element = driver.find_element_by_name("file")
element.send_keys(file_path)

# Найдем кнопку, которая отправляет введенное решение
button_click = driver.find_element_by_class_name("btn.btn-primary")
# Скажем драйверу, что нужно кликнуть оп ней
button_click.click()