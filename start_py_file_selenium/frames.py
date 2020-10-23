
from selenium import webdriver


driver = webdriver.Firefox(executable_path="D:\\selenium_python\\firefox\\geckodriver.exe")

# iframe, frameset, frame

driver.get("http://the-internet.herokuapp.com/iframe")

# frame id or frame name or index

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("body[id='tinymce']").clear()
driver.find_element_by_css_selector("body[id='tinymce']").send_keys("Hi this is kunal")
driver.switch_to.default_content()
print(driver.find_element_by_css_selector("h3").text)
driver.close()

