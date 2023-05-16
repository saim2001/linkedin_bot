import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import *



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
        related_profiles = wait_for_elements_to_load(By.XPATH,"//*[text()='People also viewed']//following::ul[1]//a",driver)
        # related_profiles = driver.find_elements(By.XPATH,"//*[text()='People also viewed']//following::ul[1]//a")
        related_profiles_URLS = [related_profiles[i].get_attribute('href') for i in range(0,len(related_profiles),2)]
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
                                               "//h1[1]").text
                driver.find_element(By.XPATH,"(//button[contains(@class,'artdeco-button--primary') and span[text()='Connect']])[2]").click()
                time.sleep(3)
                wait_for_element_to_load(By.XPATH,"//button[contains(@class,'artdeco-button') and span[text()='Add a note']]",driver).click()
                # driver.find_element(By.XPATH,"//button[contains(@class,'artdeco-button') and span[text()='Add a note']]").click()
                time.sleep(2)

                message = f'hi! {name}'
                wait_for_element_to_load(By.XPATH,'//*[@id="custom-message"]',driver).send_keys(message)
                time.sleep(2)
                waitforelemtobeclickable(By.XPATH,"//button[contains(@class,'artdeco-button') and span[text()='Send']]",driver).click()
                print('\u2713', 'connect sent successfully')
                counter +=1

        except Exception as e:
            print("\u2717 connect sending failed", e)
            pass










if __name__ == '__main__':
    driver = initiate_driver('https://www.linkedin.com/in/shahzadi-riaz-724460237/')

    send_connect_to_related_profiles(driver)
