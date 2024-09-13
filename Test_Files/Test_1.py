from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
user_Name = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.XPATH,"//input[@type = 'password']")
login_btn = driver.find_element(By.ID,"login-button")
print(login_btn.text)
user_Name.send_keys("standard_user")
password.send_keys("secret_sauce")
login_btn.click()
Title = driver.title
URL = driver.current_url
print(Title)
print(URL)
if Title == "Swag Labs":
    print("Title matches")
else:
    print("title does not match")
swagLabs = driver.find_element(By.CLASS_NAME,"app_logo")
print(swagLabs.is_displayed())
print(swagLabs.is_selected())

list_Items = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
print(list_Items)
for x in list_Items:
    print(x.get_attribute("class"))
    print(x.text)

print(len(list_Items))
