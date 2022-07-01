from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#treasure")
    value = x.get_attribute("valuex")
    y = calc(value)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
