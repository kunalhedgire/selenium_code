from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="D:\\selenium_python\\firefox\\geckodriver.exe")
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.minimize_window()
driver.get("https://chercher.tech/practice/popups")

# action = ActionChains(driver)
# menu = driver.find_element_by_id("sub-menu")
# action.move_to_element(menu).perform()
# childmenu = driver.find_element_by_link_text("Google")
# action.move_to_element(childmenu).click().perform()
# driver.close()

# Double click

x = driver.find_element_by_id("double-click")
action = ActionChains(driver)
action.double_click(x).perform()
alert = driver.switch_to.alert
# print(alert.text)
alert.accept()
driver.close()
