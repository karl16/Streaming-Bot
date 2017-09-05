#Copyright 2017- John Bunch and Karl Lawson
#REEK_Hulu Implementation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def main():
    print("Please select number of what you would like to do")
    print("1) Cancel monthly subscription")
    print("2) Renew monthly subscription")
    print("3) Check account status")
    answer = int(input())

    print("Please enter account email")
    userEmail = input()

    print("Please enter account password")
    userPassword = input()

    if answer == 1: #cancel subscription
       cancelSubscription(userEmail, userPassword)
    elif answer == 2: #renew subscription
        renewMembership(userEmail, userPassword)
    elif (answer ==3):
        checkMembership(userEmail, userPassword)


def cancelSubscription(userEmail, userPassword):
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver.get("https://www.hulu.com/welcome")

    object1 = driver.find_element_by_class_name("login")
    object1.click()
    time.sleep(2)

    driver.switch_to_frame("login-iframe")

    loginButton = driver.find_element_by_class_name("btn-login")
    loginButton.click()
    email = driver.find_element_by_name("user_email")
    email.clear()
    email.send_keys(userEmail)
    time.sleep(2)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    time.sleep(2)
    password.send_keys(Keys.RETURN)

    time.sleep(4)

    driver.switch_to_default_content()
    try:
        profile = driver.find_element_by_class_name("name")
        profile.click()
    except:
        print("Your account is already cancelled")
        return

    time.sleep(3)
    driver.switch_to_default_content()

    accountPage = driver.find_element_by_xpath("//a[@href='/account']")
    accountPage.click()
    time.sleep(5)

    preCancel = driver.find_element_by_xpath("//a[@link-type='cancel_subscription']")
    preCancel.click()

    time.sleep(6)

    try:
        preCancelContinue = driver.find_element_by_xpath("//a[@class='continue-cancel-subscription']")
        preCancelContinue.click()
    except:
        pass
    
    time.sleep(10)

    cancel = driver.find_element_by_xpath("(//div[@class='selection'])[3]")
    cancel.click()

    time.sleep(6)

    cancelContinue = driver.find_element_by_xpath("//span[@class='cancel-continue']")
    cancelContinue.click()

    time.sleep(5)

    cancelContinue2 = driver.find_element_by_xpath("//a[contains(@class, 'cancel-continue')]")
    cancelContinue2.click()

    driver.close()

def renewMembership(userEmail, userPassword):
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver.get("https://www.hulu.com/welcome")

    object1 = driver.find_element_by_class_name("login")
    object1.click()
    time.sleep(2)

    driver.switch_to_frame("login-iframe")

    loginButton = driver.find_element_by_class_name("btn-login")
    loginButton.click()
    email = driver.find_element_by_name("user_email")
    email.clear()
    email.send_keys(userEmail)
    time.sleep(2)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    time.sleep(2)
    password.send_keys(Keys.RETURN)

    time.sleep(4)

    driver.switch_to_default_content()

    try:
        driver.find_element_by_class_name("name")
        print("Your account is already active")
        return
    except:
        pass

    accountPage = driver.find_element_by_xpath("//a[@href='/account']")
    accountPage.click()
    time.sleep(3)

    renew = driver.find_element_by_xpath("//a[@href='/signup/start/one-hulu?src=acnt&plus=1']")
    renew.click()
    time.sleep(3)

    typeOfAccount = driver.find_element_by_xpath("//button[@class='button'][1]") #for limited commercials
    #typeOfAccount = driver.find_element_by_xpath("//button[@class='button'][2]") #for no commercials
    #typeOfAccount = driver.find_element_by_xpath("//button[@class='button'][3]") #for Hulu live tv
    typeOfAccount.click()
    time.sleep(3)

    #has to put credit card stuff in.

    '''
    ccNum = driver.find_element_by_id('creditCard')
    ccNum.clear()
    ccNum.send_keys(creditCardNumber)

    ccExpir = driver.find_element_by_id('expiry')
    ccExpir.clear()
    ccExpir.send_keys(expirationDate)

    ccCVC = driver.find_element_by_id('cvc')
    ccCVC.clear()
    ccCVC.send_keys(CVC)

    ccZip = driver.find_element_by_id('zip')
    ccZip.clear()
    ccZip.send_keys(billingZipcode)

    time.sleep(4)

    submit = driver.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    '''

    driver.close()

def checkMembership(userEmail, userPassword):
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver.get("https://www.hulu.com/welcome")

    object1 = driver.find_element_by_class_name("login")
    object1.click()
    time.sleep(2)

    driver.switch_to_frame("login-iframe")

    loginButton = driver.find_element_by_class_name("btn-login")
    loginButton.click()
    email = driver.find_element_by_name("user_email")
    email.clear()
    email.send_keys(userEmail)
    time.sleep(2)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    time.sleep(2)
    password.send_keys(Keys.RETURN)

    time.sleep(4)

    driver.switch_to_default_content()

    try:
        profile = driver.find_element_by_class_name("name")
        try:
            profile.click()

            time.sleep(3)
            driver.switch_to_default_content()

            accountPage = driver.find_element_by_xpath("//a[@href='/account']")
            accountPage.click()
            time.sleep(5)

            keepSubscription = driver.find_element_by_xpath("//div[contains(@class, 'keep_subscription')]")
            
            print("Your account is currently active but will expire soon.")
        except:
            print("Your account is currently ACTIVE")

    except:
        print("Your account is inactive")

    driver.close()

