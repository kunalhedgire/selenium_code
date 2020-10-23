from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Firefox(executable_path="D:\\selenium_python\\chrome\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_element_by_xpath("//div[@class='card h-100']")
print(products.text)
for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
