import webbrowser
import json
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Selenium setup
driver = webdriver.Chrome()


# Class to hold config data from json config file


# Load in data from config.json.  config.json MUST be in the same directory as this python script in order for it to work
configData = {}
with open('config.json') as json_file:
    configData = json.load(json_file)
    
    # set variable to abstract out the url a bit for easier updating with the scrape script
    website = configData['website'] + configData['uid']
    driver.get(website)

    # select correct first input
    fname_input = driver.find_element_by_id('UMbillfname')
    lname_input = driver.find_element_by_id('UMbilllname')
    email_input = driver.find_element_by_id('UMemail')
    email_confirm = driver.find_element_by_id('cnfUMemail')
    donation_check = driver.find_element_by_id('chk_fix_donation')
    mailings_uncheck = driver.find_element_by_name('subscribe')
    book_button = driver.find_element_by_id('process_payment_page')

    # fill out form
    fname_input.send_keys(configData['first_name'])
    lname_input.send_keys(configData['last_name'])
    email_input.send_keys(configData['email'])
    email_confirm.send_keys(configData['email'])
    # driver.find_element_by_id('').send_keys('1')

    # uncheck boxes
    mailings_uncheck.click()
    donation_check.click()

    # click book button
    book_button.click()
    

    # Fill out registration details
    driver.find_element_by_id('regi_name').send_keys(configData['first_name'])
    driver.find_element_by_id('regi_lname').send_keys(configData['last_name'])
    driver.find_element_by_id('regi_email').send_keys(configData['email'])
    driver.find_element_by_id('regi_phone').send_keys(configData['regi_phone'])

    #  click button
    driver.find_element_by_id('register_user').click()

    
    # Fill out payment details
    driver.find_element_by_id('UMname').send_keys(configData['name_on_card'])
    driver.find_element_by_id('UMcard').send_keys(configData['card_number'])
    month_selector = Select(driver.find_element_by_id('ex_month'))
    month_selector.select_by_visible_text(configData['expiry_month'])
    year_selector = Select(driver.find_element_by_id('ex_year'))
    year_selector.select_by_visible_text(configData['expiry_year'])
    driver.find_element_by_id('UMcvv2').send_keys(configData['cvv'])


    # click button 
    driver.find_element_by_id('process_payment_btn').click()

