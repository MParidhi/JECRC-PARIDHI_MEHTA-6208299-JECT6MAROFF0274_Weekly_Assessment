from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
sleep(2)

## Locate the username field using CSS Selector with Tag and name attribute.
username=driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
print('Username found')
## Locate the password field using CSS Selector with Tag and id attribute.
password = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
print('Password found')
## Locate the "Login" button using CSS Selector with Tag and type attribute.
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print('Login button found')
##  Locate the footer link ("Elemental Selenium") using CSS Selector(descendant).
footer=driver.find_element(By.CSS_SELECTOR, 'div[id="page-footer"] div[class="large-4 large-centered columns"] div[style="text-align: center;"] a[href]')
print('Footer link found')
