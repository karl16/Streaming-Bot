#Copyright 2017- John Bunch and Karl Lawson
#REEK_Netflix Implementation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def main():
    print("Please select number of what you would like to do")
    print("1) Cancel monthly subscription")
    print("2) Renew monthly subscription")
    print("3) Check account status")
    print("4) Restart subscription")
    answer = int(input())

    print("Please enter account email")
    userEmail = input()
    print("Please enter account password")
    userPassword = input()

    if answer == 1: #cancel subscription
       cancelSubscription(userEmail, userPassword)
    elif answer == 2: #renew subscription
        renewMembership(userEmail, userPassword)
    elif answer == 3: #check membership status
        checkSubscribeStatus(userEmail, userPassword)
    elif answer == 4: #restart subscription
        restartSubscription(userEmail, userPassword)
        

def cancelSubscription(userEmail, userPassword):
     #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com/')

    login = driver.find_element_by_id('nav-link-accountList')
    login.click()
        
    email = driver.find_element_by_name("email")
    email.clear()
    time.sleep(.5)
    email.send_keys(userEmail)
    time.sleep(.6)
    password = driver.find_element_by_name("password")
    time.sleep(2)
    password.clear()
    time.sleep(2)
    password.send_keys(userPassword)
    time.sleep(1)                      
    password.send_keys(Keys.RETURN)
   

    accountPage = driver.find_element_by_id('nav-link-accountList')
    accountPage.click()

    try:

        manageAccount = driver.find_element_by_xpath("(//div[@class='ya-card__whole-card-link'])[3]")
        manageAccount.click()
    except:

        manageAccount = driver.find_element_by_link_text("Manage Prime Membership")
        manageAccount.click()
        
    try:

        try:

            cancelMembership = driver.find_element_by_link_text("End Membership")
            cancelMembership.click()

            continueCancel1 = driver.find_element_by_id("continue-btn")
            continueCancel1.click()

            continueCancel2 = driver.find_element_by_id("continue-btn")
            continueCancel2.click()

            finalCancel3 = driver.find_element_by_id("endMembershipLaterBtn")
            finalCancel3.click()

        except:

            cancelMembership = driver.find_element_by_link_text("Do not continue my free trial")
            cancelMembership.click()

            continueCancel1 = driver.find_element_by_id("continue-btn")
            continueCancel1.click()

            continueCancel2 = driver.find_element_by_id("continue-btn")
            continueCancel2.click()

            finalCancel3 = driver.find_element_by_id("endMembershipLaterBtn")
            finalCancel3.click()
            
    except:
        print("Your account is already inactive")

    driver.close()

def renewMembership(userEmail, userPassword):
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Drhf_custrec_signin")
    
    email = driver.find_element_by_name("email")
    email.clear()
    email.send_keys(userEmail)
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)

    accountPage = driver.find_element_by_id('nav-link-accountList')
    accountPage.click()

    manageAccount = driver.find_element_by_link_text("Manage Prime Membership")
    manageAccount.click()

    try:

        renewMembership = driver.find_element_by_link_text("Continue Membership")
        renewMembership.click()

    except:
        print("Your account is still active")

    driver.close()

def checkSubscribeStatus(userEmail, userPassword):
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Drhf_custrec_signin")
    
    email = driver.find_element_by_name("email")
    email.clear()
    email.send_keys(userEmail)
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)

    accountPage = driver.find_element_by_id('nav-link-accountList')
    accountPage.click()

    manageAccount = driver.find_element_by_link_text("Manage Prime Membership")
    manageAccount.click()
    
def restartSubscription(userEmail, userPassword):
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Drhf_custrec_signin")
    
    email = driver.find_element_by_name("email")
    email.clear()
    email.send_keys(userEmail)
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)

    accountPage = driver.find_element_by_id('nav-link-accountList')
    accountPage.click()

    manageAccount = driver.find_element_by_xpath("//a[@href='https://www.amazon.com/gp/primecentral?ref_=ya_d_c_prime']")
    manageAccount.click()
        
