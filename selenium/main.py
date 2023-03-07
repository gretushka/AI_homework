from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

service = Service('/home/gretushka/AI_homework/selenium/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get('https://account.mail.ru/login/')

wait = WebDriverWait(driver, 15)

input_name = driver.find_element(By.NAME, 'username')
input_name.send_keys('kriyska@inbox.ru')
#
button_next = driver.find_element(By.XPATH, "//button[@data-test-id='next-button']")
button_next.click()
#
input_pass = driver.find_element(By.XPATH, "//input[@name='password']")
input_pass.send_keys('Anty12flag.')
input_pass.send_keys(Keys.ENTER)
last_letter = None

while True:
    letters = driver.find_elements(By.XPATH, "//a")
    letters_from = driver.find_elements(By.XPATH, '//a[contains(@class,"llc")]//span[@class="ll-crpt"]')
    letters_theme = driver.find_elements(By.XPATH, '//a[contains(@class,"llc")]//span[@class="ll-sj__normal"]')
    letters_date = driver.find_elements(By.XPATH, '//a[contains(@class,"llc")]//div[contains(@class,"llc__item_date")]')

    print(len(letters), len(letters_from), len(letters_date), len(letters_theme))

    if letters[-1] == last_letter:
        break
    for i in range(len(letters_from)):
        letter_from = letters_from[i].text
        letter_theme = letters_theme[i].text
        letter_date = letters_date[i].text

        correspondence = {

            'letter_from': letter_from,
            'letter_theme': letter_theme,
            'letter_date': letter_date,
        }
        print(correspondence)
    letters = driver.find_elements(By.XPATH, "//a")
    last_letter = letters[-1]
    actions = ActionChains(driver)
    actions.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN)

    actions.perform()
    sleep(5)

    # driver.execute_script(
    #     "var evt = document.createEvent('MouseEvents'); evt.initEvent('wheel', true, true); evt.deltaY = -100000; document.querySelector('.yamb-conversation__content').dispatchEvent(evt);")

    sleep(5)

print()
