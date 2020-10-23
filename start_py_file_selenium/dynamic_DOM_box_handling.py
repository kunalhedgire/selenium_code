import time
from selenium import webdriver


driver = webdriver.Firefox(executable_path="D:\\selenium_python\\firefox\\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"
driver.close()
