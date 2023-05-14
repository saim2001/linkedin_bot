import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def initiate_driver(URL):
    try:
        option = ChromiumOptions()
        option.add_argument("--user-data-dir=C:/Users/saim rao/AppData/Local/Google/Chrome/User Data/")
        option.add_argument("--profile-directory=Profile 4")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        driver.get(URL)
        print('\u2713','Driver initiated successfully')
        time.sleep(5)
        return driver
    except Exception as e:
        print('\u2717',e)
        return None
def send_connect_to_related_profiles(driver):

    try:
        time.sleep(3)
        related_profiles = driver.find_elements(By.XPATH,"//*[text()='People also viewed']/ancestor::div[@class='pvs-header__container']/following-sibling::div//ul/li/div/div/a")
        related_profiles_URLS = [i.get_attribute('href') for i in related_profiles]
        print(related_profiles_URLS)
        print('\u2713','Related profiles found')
    except Exception as e:
        print("\u2717 couldn't find related profiles",e)

    counter = 0
    index_set = set()
    while counter <=1 :
        try:
            index = random.randrange(len(related_profiles_URLS))
            if index not in index_set:
                index_set.add(index)
                random_profile = related_profiles_URLS[index]
                print(random_profile)
                driver.get(random_profile)
                time.sleep(5)
                name = driver.find_element(By.XPATH,
                                               "//*[@class='text-heading-xlarge inline t-24 v-align-middle break-words']").text
                driver.find_element(By.XPATH,"//*[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action']/span[text()='Connect']").click()
                time.sleep(3)
                driver.find_element(By.XPATH,"//*[@class='artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view mr1']").click()
                time.sleep(2)

                message = f'hi! {name}'
                driver.find_element(By.XPATH,'//*[@id="custom-message"]').send_keys(message)
                time.sleep(2)
                driver.find_element(By.XPATH,"//*[@aria-label='Send now']").click()
                print('\u2713', 'connect sent successfully')
                counter +=1

        except Exception as e:
            print("\u2717 connect sending failed", e)
            pass










if __name__ == '__main__':
    driver = initiate_driver('https://www.linkedin.com/in/francis-asabere-3b4791127/')

    send_connect_to_related_profiles(driver)
