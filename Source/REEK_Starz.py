#Copyright 2017- John Bunch and Karl Lawson
#REEK_Starz Implementation

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
    elif (answer == 3):
        checkMembership(userEmail, userPassword)

def cancelSubscription(userEmail, userPassword): 
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver.get("https://www.starz.com/")

    time.sleep(3)
    login = driver.find_element_by_xpath("//a[@href='/login/']")
    login.click()

    time.sleep(4)
    login2 = driver.find_element_by_xpath("//a[@class='login-toggle-section'][2]")
    login2.click()

    time.sleep(2)
    email = driver.find_element_by_xpath("//input[@name='email']")
    email.clear()
    email.send_keys(userEmail)

    time.sleep(3)
    password = driver.find_element_by_xpath("//input[@name='password']")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)
    time.sleep(4)
    driver.get("https://www.starz.com/billing/cancel")  #redirects to the exact page rather than clicking a bunch of different ones.
    
    time.sleep(3)
    cancel2 = driver.find_element_by_xpath("//div[@class='form-group-radio'][2]")
    cancel2.click()   
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    #scrolls to the bottom of the page

    cancelContinue = driver.find_element_by_xpath("//button[@ng-disabled='!vm.reason']")
    cancelContinue.click()

    time.sleep(4)
    cancelContinue2 = driver.find_element_by_xpath("//button[@ng-click='vm.onContinueCancellationButtonClick()']")
    cancelContinue2.click()

    time.sleep(4)
    reEnterPassword = driver.find_element_by_xpath("//input[@name='userPassword']")
    reEnterPassword.clear()
    reEnterPassword.send_keys(userPassword)

    time.sleep(2)

    cancelContinue3 = driver.find_element_by_xpath("//div[contains(@class, 'continueButton')]")
    cancelContinue3.click()

    driver.close()



def renewMembership(userEmail, userPassword): #not complete needs a debit card hooked up
    
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver.get("https://www.starz.com/")
    
    time.sleep(3)
    login = driver.find_element_by_xpath("//a[@href='/login/']")
    login.click()
    
    time.sleep(4)
    login2 = driver.find_element_by_xpath("//a[@class='login-toggle-section'][2]")
    login2.click()
    
    time.sleep(2)
    email = driver.find_element_by_xpath("//input[@name='email']")
    email.clear()
    email.send_keys(userEmail)
    
    time.sleep(3)
    password = driver.find_element_by_xpath("//input[@name='password']")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)
    time.sleep(4)


def checkMembership(userEmail, userPassword):
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver.get("https://www.starz.com/")
    
    time.sleep(3)
    login = driver.find_element_by_xpath("//a[@href='/login/']")
    login.click()
    
    time.sleep(4)
    login2 = driver.find_element_by_xpath("//a[@class='login-toggle-section'][2]")
    login2.click()
    
    time.sleep(2)
    email = driver.find_element_by_xpath("//input[@name='email']")
    email.clear()
    email.send_keys(userEmail)
    
    time.sleep(3)
    password = driver.find_element_by_xpath("//input[@name='password']")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)
    time.sleep(4)

    driver.get("https://www.starz.com/settings/subscription")
    time.sleep(4)

    try:
        subscriptionStatus = driver.find_element_by_xpath("//button[@class='restart-subscription-button']")       
        print("Membership is currently INACTIVE.")
    except:
        print("Membership is currently ACTIVE.")

    driver.close()
    


