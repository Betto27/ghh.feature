from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://www.python.org")

driver.find_element_by_id('id-search-field').send_keys("python")

driver.find_element_by_css_selector('#submit').click()

btn_txt = driver.find_element_by_id('submit').text

print(btn_txt)