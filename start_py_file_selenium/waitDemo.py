import time
from selenium import webdriver


driver = webdriver.Firefox(executable_path="D:\\selenium_python\\firefox\\geckodriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(10)
prod = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert prod == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
msg = driver.find_element_by_class_name("promoInfo").text
print(msg)
# driver.close()