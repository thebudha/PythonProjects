from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys

# instantiate the Chrome WebDriver (call the class)
browser = webdriver.Chrome()
browser.get('https://www.github.com')

# single wait instance (increase timeout as needed)
wait = WebDriverWait(browser, 10)

exit_code = 0
try:
	# use Selenium 4 style lookups with explicit waits
	signin_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in')))
	signin_link.click()

	username_box = wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
	username_box.send_keys('username')
	password_box = wait.until(EC.presence_of_element_located((By.ID, 'password')))
	password_box.send_keys('password123')

	signin_button = wait.until(EC.element_to_be_clickable((By.NAME, 'commit')))
	signin_button.click()

	icon_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-login="thebudha"]')))
	icon_button.click()

	# verify text appears on page
	wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'thebudha'))

	print('TEST PASSED')
	exit_code = 0
except Exception as e:
	print('TEST FAILED:', str(e))
	exit_code = 1
finally:
	sleep(2)
	try:
		browser.quit()
	except Exception:
		pass
	sys.exit(exit_code)
