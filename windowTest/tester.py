from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
 
driver.get("http://192.168.0.1/")
driver.find_element_by_xpath(\
            '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')\
                .send_keys("admin")
driver.find_element_by_xpath(\
            '//*[@id="passwd_td"]/input')\
                .send_keys("01032244433")

driver.find_element_by_xpath('//*[@id="submit_bt"]').click()
driver.find_element_by_xpath('/html/body/map/area[1]').click()

driver.switch_to.frame('main_body')
driver.switch_to.frame('navi_menu_advance')

driver.find_element_by_xpath('//*[@id="advance_picon"]').click()
driver.find_element_by_xpath('//*[@id="expertconf_picon"]').click()
driver.find_element_by_xpath('//*[@id="expertconf_remotepc_3_td"]/span/a').click()

driver.switch_to.default_content()
driver.switch_to.frame('main_body')
driver.switch_to.frame('main')
driver.switch_to.frame('wollist_iframe')

time.sleep(0.5)
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[4]/span/input').click()

driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[4]/span/span').click()
driver.switch_to.alert.accept()
time.sleep(5.0)
driver.quit()