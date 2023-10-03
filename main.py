import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def start():
    service = webdriver.ChromeService(executable_path='driver/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get('https://sbis.ru')
    contact_button = driver.find_element(by=By.LINK_TEXT, value='Контакты')
    contact_button.click()
    tensor_img = driver.find_element(by=By.XPATH, value='//img[@alt="Разработчик системы СБИС — компания «Тензор»"]')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tensor_img)).click()
    try:
        page = driver.page_source
        power_div = EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content.tensor_ru-Index__card'))
        WebDriverWait(driver, 20).until(power_div)
    except NoSuchElementException:
        print("Блок Сила в людях - не найден")
        exit()
    power_div.find_element(by=By.LINK_TEXT, value='Подробнее').click()


if __name__ == '__main__':
    start()
