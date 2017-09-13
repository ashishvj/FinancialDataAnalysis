# Python Script to get data from the NASDAQ website
# Authors: Ashish Jagtiani (ashishvjagtiani@gmail.com), Dipika Mulchandani (dipikm86@gmail.com)
# Code for Kengroo.com
# Part of Data Analysis series > Financial Data Analysis on kengroo.com

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os


STOCK_NAME = 'AAPL'
DATA_PATH = './data'

#Set Range for data to 1 day
DATA_RANGE = 'range1D'

#define file names for downloading data
new_file_name = STOCK_NAME + '_' + DATA_RANGE +'.xls'
new_file_name_fullpath = DATA_PATH +'/' +new_file_name
download_file = 'grid.xls'
download_file_full_path = DATA_PATH + '/' + download_file



#Setting option for Chrome i.e download path specifically
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : DATA_PATH}
chrome_options.add_experimental_option('prefs', prefs)

#Path where chrome drive is saved
executable_path = './chromedriver'
driver = webdriver.Chrome(executable_path,chrome_options=chrome_options)

WEB_PATH = 'http://www.nasdaq.com/symbol/' + STOCK_NAME + '/interactive-chart'
driver.get(WEB_PATH)


#Select the iframe on the website
iframe_main = driver.find_element_by_xpath('//*[@id="chartholder"]/iframe')  
driver.switch_to_frame(iframe_main) 

#Select data range here
driver.find_element_by_id(DATA_RANGE).click()

#Load Data table
driver.find_element_by_id('dataTableBtn').click()

#Check if file exists - if it does delete to remove copies
if os.path.exists(download_file_full_path):
	print "File from prev run found in folder - deleting"
	os.remove(download_file_full_path)
else:
	print "File from previous run not found - continuing with download"


#download excel file with data
time.sleep(3)
myElem = driver.find_element_by_xpath('//*[@id="gridContainer"]/div[1]/span[1]')

if myElem.is_displayed():
	myElem.click()
else:
	print "Element not visible or displayed"

#Add wait to allow file download before quitting browser
time.sleep(10)
driver.quit()



#rename downloaded data
try:
	print "renaming " + download_file + "to " + new_file_name
	os.rename(download_file_full_path, new_file_name_fullpath)
except:
	print "Error with file renaming"

	









