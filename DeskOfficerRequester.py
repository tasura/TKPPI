from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
import random

driver = webdriver.Chrome()
driver.get('http://caps.jamb.gov.ng/default.aspx?TokenID=P#81%60@78')
#---------------------------------------------------------
loginInput = driver.find_element_by_id('txtusername')
loginInput.send_keys('3359admissionofficer')
passwordInput = driver.find_element_by_id('txtpassword')
passwordInput.send_keys('3359')
submit = driver.find_element_by_id('btnLogin')
submit.click()
time.sleep(1)
#----------------------------------------------
submit = driver.find_element_by_id('ContentPlaceHolder1_btnaccept')
submit.click()
marketplace = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/div[2]/ul/li[12]/a')
marketplace.click()
newSelection = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/div[2]/ul/li[12]/ul/li[1]/a')
newSelection.click()
instSelector = Select(driver.find_element_by_id('ContentPlaceHolder1_drpInstitution'))
inst = input('Please Select An Institution On The Page. Afterwards Hit The Enter Key')
programSelector = Select(driver.find_element_by_id('ContentPlaceHolder1_drpProgram'))
program = input('Please Select a Program From the On The Page. Afterwards Hit The Enter Key.')
orderBy = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_drpOrderBy"]/option[4]')
orderBy.click()
search = driver.find_element_by_id('ContentPlaceHolder1_btnsave2')
search.click()
 
