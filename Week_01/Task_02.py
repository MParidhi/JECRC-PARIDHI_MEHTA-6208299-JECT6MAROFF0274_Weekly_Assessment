from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.wikipedia.org/')
sleep(2)

search=driver.find_element(By.ID, 'searchInput')
print('Found-1')

english=driver.find_element(By.XPATH, '//strong[text()="English"]')
print('Found-2')

logo=driver.find_element(By.CSS_SELECTOR, 'span[class="central-textlogo__image sprite svg-Wikipedia_wordmark"]')
print('Found-3')

lang=driver.find_elements(By.CSS_SELECTOR, 'nav[class="central-featured"] a')
print(len(lang))
print('Found-4')

driver.back()
driver.forward()
driver.refresh()
print(f"The title of final page is: {driver.title}")

driver.quit()

