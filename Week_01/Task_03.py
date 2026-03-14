from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get('https://www.amazon.in/')
print(f'Title of page is: {driver.title}')
sleep(2)

driver.get('https://www.nike.in/')
print(f'Title of page is: {driver.title}')
sleep(2)

driver.get('https://www.hindustantimes.com/')
print(f'Title of page is: {driver.title}')
sleep(2)

driver.get('https://www.python.org/')
print(f'Title of page is: {driver.title}')
sleep(2)

driver.quit()

