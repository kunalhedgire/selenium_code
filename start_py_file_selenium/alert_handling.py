import time
from selenium import webdriver


# driver = webdriver.Firefox(executable_path="D:\\selenium_python\\firefox\\geckodriver.exe")

driver = webdriver.Chrome(executable_path="D:\\selenium_python\\chrome\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("name").send_keys("Kunal")
# driver.find_element_by_id("alertbtn").click()
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(10)
alert.dismiss()

driver.close()
