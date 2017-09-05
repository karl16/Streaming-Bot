#Copyright 2017- John Bunch and Karl Lawson
#REEK_Netflix Implementation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        cancelMembership(userEmail, userPassword)
        
    elif answer == 2:   #renew subscription
        restartMembership(userEmail, userPassword)

    elif answer == 3: #checks subscription
        checkActive(userEmail, userPassword)

    else:
        print("That is not an option.")
    


def cancelMembership(userEmail, userPassword):
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver = webdriver.Chrome()
    driver.get("https://www.netflix.com/youraccount")
    
    email = driver.find_element_by_name("email")
    email.clear()
    email.send_keys(userEmail)
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)

    try:
        check = driver.find_element_by_xpath("//a[@href='/CancelPlan']")
        cancel = driver.find_element_by_class_name("account-cancel-button")
        cancel.click()
        
        finishCancel = driver.find_element_by_class_name("btn-blue")
        finishCancel.click()
    except:
        print("Your account is already inactive")
    

    driver.close()


def restartMembership(userEmail, userPassword):
  
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver.get("https://www.netflix.com/youraccount")
        
    email = driver.find_element_by_name("email")
    email.clear()
    email.send_keys(userEmail)
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)

    try:
        driver.find_element_by_link_text("Add streaming plan")
        notFreeTrialRenew(driver)
    except:
        freeTrialRenew(driver)


def notFreeTrialRenew(driver):          # @TODO not finished~~~~~~~~~~~~~~~~~~~~~~
    renew = driver.find_element_by_link_text("Add streaming plan")
    renew.click()
  #  driver.close()

def freeTrialRenew(driver):
    try:
        check = driver.find_element_by_xpath("//a[@href='/CancelPlan']")
        print("Your account is still active")
    except:
        reSubscribe = driver.find_element_by_class_name("account-cancel-button")
        reSubscribe.click()

    driver.close()


def checkActive(userEmail, userPassword):
    #driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
    driver = webdriver.Chrome()
    driver.get("https://www.netflix.com/youraccount")

    email = driver.find_element_by_name("email")
    email.clear()
    email.send_keys(userEmail)
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)

    try:
        check = driver.find_element_by_xpath("//a[@href='/CancelPlan']")
        print("Your account is still active")
    except:
        print("Your account is inactive")
        
    driver.close()
