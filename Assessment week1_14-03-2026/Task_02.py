from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.wikipedia.org/')
sleep(2)

## Find the search input field.
search=driver.find_element(By.ID, 'searchInput')
print('Found-1')

## Find the "English" language.
english=driver.find_element(By.XPATH, '//strong[text()="English"]')
print('Found-2')

## Find the main Wikipedia logo image.
logo=driver.find_element(By.CSS_SELECTOR, 'span[class="central-textlogo__image sprite svg-Wikipedia_wordmark"]')
print('Found-3')

## Count how many language links are present in the central block (Hint: inspect the common container and look for tags within it).Use find_elements and print the count.
lang=driver.find_elements(By.CSS_SELECTOR, 'nav[class="central-featured"] a')
print(len(lang))
print('Found-4')

## Navigate back to the previous page
driver.back()
sleep(5)

## Navigate forward.
driver.forward()
sleep(5)

## Refresh the page.
driver.refresh()
sleep(5)

## Print the final page title.
print(f"The title of final page is: {driver.title}")

## Quit the browser.
driver.quit()

