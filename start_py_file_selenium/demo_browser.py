from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
# from selenium.webdriver.chrome.options import Options


# driver = webdriver.Chrome(options=options, executable_path="D:\\selenium_python\chromedriver-84.0\chromedriver.exe")
driver = webdriver.Firefox(executable_path="D:\\selenium_python\\firefox\\geckodriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.find_element_by_name("name").send_keys("kunal")
driver.find_element_by_name("email").send_keys("hedgire")
driver.find_element_by_css_selector("input[name='email'").send_keys("hegdire")
driver.find_element_by_id("exampleInputPassword1").send_keys("Kunal@123")
driver.find_element_by_id("exampleCheck1").click()
gender = Select(driver.find_element_by_id("exampleFormControlSelect1"))
gender.select_by_visible_text("Female")
time.sleep(2)
gender.select_by_index(0)
driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[6]/div[1]/label").click()
driver.find_element_by_css_selector("input[type='submit']").click()
msg = driver.find_element_by_class_name("alert-success").text
assert "success" in msg
# print(driver.current_url)

driver.close()
