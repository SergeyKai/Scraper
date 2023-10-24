import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver.find_element().send_keys()

url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'

price_xpath = '//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[3]/div/div[1]/span'
apartment_title_xpath = '//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[1]/h1'
apartment_title_class = 'a10a3f92e9--title--vlZwT'
show_contacts_btn_xpath = '//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[4]/button/span'
description_xpath = '//*[@id="description"]/div/div/div/span'

apartment_item = {
    'title': '',
    'description': '',
    'price': '',
    'contacts': [],
    'about apartments': {},
    'features': [],
}


def main():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    container = driver.find_element(By.TAG_NAME, 'article')
    container.click()
    time.sleep(5)

    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[-1])

    title = driver.find_element(By.CLASS_NAME, 'a10a3f92e9--title--vlZwT')
    apartment_item['title'] = title.text

    description = driver.find_element(By.XPATH, description_xpath)
    apartment_item['description'] = description.text

    btn = driver.find_element(By.XPATH, show_contacts_btn_xpath)
    btn.click()
    time.sleep(2)
    contacts_list = driver.find_elements(By.CLASS_NAME, 'a10a3f92e9--phone-link--bNwD7')

    for i in contacts_list:
        apartment_item['contacts'].append(i.text)

    about_apartment = driver.find_elements(By.CSS_SELECTOR, '[data-name="OfferSummaryInfoItem"]')

    for i in about_apartment:
        apartment_param = i.find_elements(By.TAG_NAME, 'span')
        key = apartment_param[0].text
        value = apartment_param[1].text
        apartment_item['about apartments'].update({key: value})

    features_list = driver.find_elements(By.CSS_SELECTOR, '[data-name="FeaturesItem"]')

    for features_item in features_list:
        apartment_item['features'].append(features_item.text)

    print(apartment_item)

    driver.quit()


if __name__ == '__main__':
    main()
