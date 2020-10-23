import time
from selenium import webdriver


# driver = webdriver.Firefox(executable_path="D:\\selenium_python\\firefox\\geckodriver.exe")

driver = webdriver.Chrome(executable_path="D:\\selenium_python\\chrome\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkbox = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkbox))

for box in checkbox:
    box.click()

radio = driver.find_elements_by_name("radioButton")
print(len(radio))
radio[1].click()
assert radio[1].is_selected()
time.sleep(2)
driver.save_screenshot('screen.png')

driver.close()
