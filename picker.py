from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://simpliers.com/de/gewinnspiel/instagram")

time.sleep(1)

link = driver.find_element(By.NAME, "url[]")
link.send_keys('https://www.instagram.com/p/CgjxZrIKDbz/?utm_source=ig_web_copy_link')

time.sleep(1)

banner = driver.find_element(By.CLASS_NAME, "d-block.text-center.animate__animated.animate__pulse.animate__infinite.mt-8")
banner.click()

time.sleep(5)

search = driver.find_element(By.ID, "cekilisBaslat")
search.submit()

time.sleep(20)

backdrop = driver.find_element(By.CLASS_NAME, "count-unique-users-button")
backdrop.click()

time.sleep(5)

comments = driver.find_element(By.ID, "katilimcilariGorBtn")
comments.click()

time.sleep(5)

rows = driver.find_elements(By.XPATH, "//div[@class='d-flex justify-content-between align-items-center']")
for row in rows:
    results = row.find_element(By.XPATH, ".//span[@class='comment-username h5 mb-0']")
    if "0 : 0" not in results.text:
        print(results.text)
        with open('username.txt', 'a') as f:
            f.write(results.text)
            f.write('\n')

time.sleep(10)

driver.quit()

