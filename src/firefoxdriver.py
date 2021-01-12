from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import json
import os
import logging
from logging.handlers import RotatingFileHandler

# base var for heroku
URL = "http://ssl305.herokuapp.com/"

# base var for logger
fileMaxByte = 1024
logger = logging.getLogger(__name__)
fileHandler = RotatingFileHandler(filename=os.path.dirname(os.path.realpath(__file__))\
     + "/../log/temp.log", maxBytes=1024, backupCount=2)
formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

logger.debug("Prog start.")

options = webdriver.firefox.options.Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
driver.get("http://192.168.0.1/")

logger.debug("Get URL.")

time.sleep(3.0)
driver.find_element_by_xpath(\
            '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')\
                .send_keys("admin")

driver.find_element_by_xpath(\
            '//*[@id="passwd_td"]/input')\
                .send_keys("01032244433")

logger.debug("ID, PW inputted.")

time.sleep(3.0)
driver.find_element_by_xpath('//*[@id="submit_bt"]').click()
time.sleep(3.0)

logger.debug("Logined.")

tmpBtn = driver.find_element_by_xpath('/html/body/map/area[1]')
driver.execute_script("arguments[0].click();", tmpBtn)
time.sleep(3.0)

logger.debug("Main page.")

driver.switch_to.frame('main_body')
driver.switch_to.frame('navi_menu_advance')

driver.find_element_by_xpath('//*[@id="advance_picon"]').click()
driver.find_element_by_xpath('//*[@id="expertconf_picon"]').click()
driver.find_element_by_xpath('//*[@id="expertconf_remotepc_3_td"]/span/a').click()

logger.debug("WOL page.")
time.sleep(3.0)
driver.switch_to.default_content()
driver.switch_to.frame('main_body')
driver.switch_to.frame('main')
driver.switch_to.frame('wollist_iframe')
time.sleep(3.0)

logger.debug("WOL page frame checked.")

while 1:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        thermal = f.readline().strip()

    if int(thermal) < 60000:
        logger.info(thermal)
    else:
        os.system("sudo shutdown now")

    resp = requests.get(URL)
    if resp.status_code:
        if json.loads(resp.text)["return"] == 1:
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[4]/span/input').click()
            driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[4]/span/span').click()
            driver.switch_to.alert.accept()
    time.sleep(10.0)
driver.quit()