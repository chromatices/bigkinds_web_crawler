import time
import argparse
from selenium import webdriver

from custom_calendar import start_end_calender
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

parser = argparse.ArgumentParser(description="enter your id and pwd of bigkinds.")
parser.add_argument('--id', type=str, default='', help='enter your id')
parser.add_argument('--pwd', type=str, default='', help='enter your pwd')
args = parser.parse_args()


def valid_id_pwd(id: str, pwd: str):
    if id == '' or pwd == '':
        raise AssertionError("Please enter your id and pwd again.")
    if len(id.split('@')) == 1:
        raise AssertionError("Your id has format like e-mali. Please Check again.")


def login_bigkinds(id: str, pwd: str, driver: webdriver):
    driver.get('https://www.bigkinds.or.kr/')
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login-user-id"]').send_keys(id)
    driver.find_element_by_xpath('//*[@id="login-user-password"]').send_keys(pwd)
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    time.sleep(2)


def search_news(start_date: str, end_date: str, driver: webdriver):
    print(start_date.split('-')[0] + '-' + start_date.split('-')[1] + ' start!')
    for i in range(11):
        # click search option
        driver.find_element_by_xpath('// *[ @ id = "news-search-form"] / div / div[1] / button').click()
        driver.find_element_by_xpath('//*[@id="news-search-form"]/div/div[1]/div[2]/div/div[1]/div[1]/a').click()

        # set start date
        driver.find_element_by_xpath('//*[@id="search-begin-date"]').click()
        driver.find_element_by_xpath('//*[@id="search-begin-date"]').send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath('//*[@id="search-begin-date"]').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('//*[@id="search-begin-date"]').send_keys(start_date)

        # set end date
        driver.find_element_by_xpath('//*[@id="search-end-date"]').click()
        driver.find_element_by_xpath('//*[@id="search-end-date"]').click()
        driver.find_element_by_xpath('//*[@id="search-end-date"]').send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath('//*[@id="search-end-date"]').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('//*[@id="search-end-date"]').send_keys(end_date)
        # set the magazine
        driver.find_element_by_xpath(
            '// *[ @ id = "news-search-form"] / div / div[1] / div[2] / div / div[1] / div[3] / a').click()
        driver.find_element_by_xpath(
            '// *[ @ id = "category_provider_list"] / li[' + str(i + 1) + '] / span / label').click()
        driver.find_element_by_xpath('// *[ @ id = "search-foot-div"] / div[2] / button[2]').click()
        # for waiting searching result
        time.sleep(10)
        # loading csv result
        driver.find_element_by_xpath('// *[ @ id = "collapse-step-3"]').click()
        time.sleep(2)
        # click download csv file
        driver.find_element_by_xpath('// *[ @ id = "analytics-data-download"] / div[3] / button').click()
        time.sleep(2)
        # for chrome notification window confirmation button
        da = Alert(driver)
        da.accept()

        time.sleep(60)  # for loading download file
        driver.find_element_by_xpath('//*[@id="wrap"]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "header"] / div[1] / div / h1').click()
        time.sleep(2)
    print(start_date.split('-')[0] + '-' + start_date.split('-')[1] + ' is end.')


if __name__ == '__main__':
    id = args.id
    pwd = args.pwd
    valid_id_pwd(id, pwd)
    start_date, end_date = start_end_calender()
    driver = webdriver.Chrome('D:\\download\\chromedriver_win32 (1)\\chromedriver.exe')
    login_bigkinds(id, pwd, driver)
    for x in range(len(start_date)):
        start = start_date[x]
        end = end_date[x]
        search_news(start, end, driver)
    driver.close()
