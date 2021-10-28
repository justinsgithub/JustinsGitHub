from selenium import webdriver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# need the below imports to work with Explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
fetlife = myclient["fetlife"]
#databaseList = myclient.list_database_names()



#fetlifeStates = fetlife["states"]
#stateList = []
#for state in fetlifeStates.find({},{"_id":0, "name":1}):
#    stateList.append(state)
#for state in stateList:
#    print(state["name"])



password = 'Ilovelemon93'
username = 'lemonjewell@yahoo.com'
url = 'https://fetlife.com/users/sign_in'
usernameForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[1]/div/div/input'
passwordForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[2]/div/div/input'
loginButton = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button'
placesLink = '/html/body/nav[1]/div[1]/ul/li[5]/a'
seattleLink = '/html/body/div[3]/div/header/div/div[2]/div/a[1]'
kinstersLink = '/html/body/div[3]/div/header/div/div[2]/a[2]/div/div'
nextPage = '/html/body/div[3]/div/div[2]/div/main/footer/div[1]/a[3]'
userLink = '/html/body/div[3]/div/div[2]/div/main/div/div[18]/div/div/div/div[1]/div[2]/div[1]/a'
goBack = 'browser.back()'
washingtonLink = 'a[@href=""]'
browser = webdriver.Chrome('/home/jewell/bin/chromedriver')  # Optional argument, if not specified will search path.
browser.get(url)
email_in = browser.find_element(By.XPATH, usernameForm)
email_in.send_keys(username)
pw_in = browser.find_element(By.XPATH, passwordForm)
pw_in.send_keys(password)
login_btn = browser.find_element(By.XPATH, loginButton)
login_btn.click()
sleep(1)


seattleUsers = fetlife["seattleUsers"]

userList = []

for user in seattleUsers.find({},{"_id":0, "userName":1, "lovedPictures":1}):
    lovedPictures = user["lovedPictures"]
    username = user["userName"]
    if lovedPictures == False:
        userList.append(username)

for user in userList:
    try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
        goBack
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys('')
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a[2]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
        goBack
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys('')
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a[3]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
        userQuery = {"userName": user}
        newValue = { "$set": { "lovedPictures": True } }
        seattleUsers.update_one(userQuery, newValue)
        print('finished round')
    except Exception:
        print('passing')
        pass