import re
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

if len(sys.argv) < 4:
    print('Usage: ' + sys.argv[0] + ' <CLASS URL> <LOGIN> <PASSWORD>')
    sys.exit(1)

login = sys.argv[2]
password = sys.argv[3]
implicit_delay = 10
explicit_delay = 10

driver = webdriver.Firefox()
driver.implicitly_wait(implicit_delay)

class_url = sys.argv[1]
driver.get(class_url)

login_field = driver.find_element_by_css_selector("input[type='email']")
login_field.send_keys(login)

password_field = driver.find_element_by_css_selector("input[type='password']")
password_field.send_keys(password)

submit_button = driver.find_element_by_css_selector('button')
submit_button.click()

links = WebDriverWait(driver, explicit_delay).until(
    expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, "//a[starts-with(., 'View ')]")
    )
)
for link in links:
    link.click()

links = WebDriverWait(driver, explicit_delay).until(
    expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, '//a[text()="View"] | //a[text()="Continue"] | //a[text()="Start"]')
    )
)
topic_links = []
for link in links:
    topic_links.append(link.get_attribute('href'))

topic = 1
for topic_link in topic_links:
    print('Topic #' + str(topic));
    topic += 1

    driver.get(topic_link)
    links = WebDriverWait(driver, explicit_delay).until(
        expected_conditions.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "ol[aria-labelledby='sidebar-concepts-list'] a")
        )
    )
    lesson_links = []
    for link in links:
        lesson_links.append(link.get_attribute('href'))

    for lesson_link in lesson_links:
        driver.get(lesson_link)
        try:
            youtube_link = WebDriverWait(driver, explicit_delay / 2).until(
                expected_conditions.visibility_of_element_located(
                    (By.CSS_SELECTOR, "iframe[title='YouTube video player']")
                )
            )

            video_source = youtube_link.get_attribute('src')
            video_id = re.search(r"\/([^\/]+)\?", video_source).group(1)

            print('https://www.youtube.com/watch?v=' + video_id)
        except TimeoutException:
            pass

raw_input('Press the <ENTER> key to continue...')

driver.quit()
