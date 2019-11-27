import pdb

import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from tace_detection.utils.octopod_info import get_octopod_info

octo_info = get_octopod_info()
octo_ngrams = octo_info.nickname.apply(lambda x: x.lower())


def _scrap_askbob_images():
    driver = webdriver.Chrome('../chromedriver')
    driver.get('https://askbob.octo.com/')
    login_button = driver.find_element_by_id('google-signin-button')
    login_button.click()

    input_mail = driver.find_element_by_id('identifierId')
    input_mail.send_keys('srochette@octo.com')
    next_button = driver.find_element_by_id('identifierNext')
    next_button.click()

    password = WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
    password.send_keys('my_pswd')
    next_button = driver.find_element_by_id('passwordNext')
    next_button.click()

    # Manually login for 2 steps auth
    pdb.set_trace()

    for ngram in octo_ngrams:
        driver.get(f'https://askbob.octo.com/users/{ngram}')
        driver.save_screenshot(f'../screenshots/{ngram}.png')
    driver.close()


def _crop_askbob_screenshots():
    y_1, y_2 = 270, 565
    x_1, x_2 = 1892, 2185
    for ngram in octo_ngrams:
        image = cv2.imread(f'../screenshots/{ngram}.png')
        face = image[y_1:y_2, x_1:x_2]
        cv2.imwrite(f'../screenshots/{ngram}.png', face)


_scrap_askbob_images()
_crop_askbob_screenshots()
