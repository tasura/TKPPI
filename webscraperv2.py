from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import csv
import random

def random_pause_time(): #pauses for an interval between 1 and 30 seconds
 interval = random.randrange(1 , 30, 1)
 time.sleep(interval)

def check_exists_by_xpath(xpath): #checks for the error message related to the exam slip page
 try:
  driver.find_element_by_xpath(xpath)
 except NoSuchElementException:
  return False
 return True
#---------------------------------------Initialization
readFile = input("Enter the file that you want to be read: ")
writeFile = input("Enter the file that you want to write to: ")
driver = webdriver.Chrome(); #Requires The ChromeDriver in the file
driver.get("https://portal.jamb.gov.ng/ExamSlipPrinting/PrintExaminationSlip")
parentWindow = driver.current_window_handle
assert "JAMB" in driver.title
dumpingFile = open(writeFile, 'w', newline='')#put the name of the file you're writing to here 
#If you plan on adding to an existing file, change 'w' to 'a'
writer = csv.writer(dumpingFile)
numberFile = open(readFile)
next(numberFile, None)
writer.writerow(['Jamb Number','Major','Surname' ,'First Name' ,'Phone','Email'])
collections = 0
denials = 0
#----------------------------------------
for row in numberFile:
 jambNumber = row.split(',')[0] #Starting From 0, put the number of the column where the jamb numbers are
 major = row.split(',')[2]
 jambInput = driver.find_element_by_id('txtRegNumber')
 jambInput.send_keys(jambNumber)
 submit = driver.find_element_by_id('lnkSearch')
 submit.click()
 random_pause_time
 if check_exists_by_xpath('//*[@id="dvalert"]') == False:
  driver.switch_to.window(driver.window_handles[1]) #Switches to the popup window
  surname = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/div/table/tbody/tr[1]/td[2]/label')
  firstName = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[2]/label')
  telMail = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/div/table/tbody/tr[7]/td[2]/label')
  #to add more fields to the collection, you must copy the Xpath for that field on the page
  tm = telMail.text.split('/')
  telephone= tm[0]
  mail = tm[1]
  collections+= 1
  writer.writerow([jambNumber,major,surname.text,firstName.text, telephone, mail])
  driver.close()#Closes the Popup
  driver.switch_to.window(parentWindow)#Goes back to the main window
  random_pause_time
 else:
  denials+=1
  writer.writerow([jambNumber,major])
 jambInput = driver.find_element_by_id('txtRegNumber')
 jambInput.clear()#Clears the text input
numberFile.close()
dumpingFile.close()
driver.quit()#Closes the Browser
print('Out of: ' + str((collections + denials)) + ' total queries, ' + str(collections) + ' were collected and' + str(denials) + ' were denied')
 


