# This code script is written by @recberdeniz to exercise about python selenium application for Python Programming
# Python selenium instagram script for find
# followed people, followers and just your followed.
# Also this script can automatically unfollow just your followed people
# I) Postscript: I used Mozilla Firefox as a web driver please check that your web driver option and revise the script.
# II) Postscript: Please insert your username||phone number || mail address at row 16
#                 Please insert your password at row 21
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(executable_path=r'C:\Users\blue_\anaconda3\geckodriver.exe', options=options)
browser.get("https://www.instagram.com/")
time.sleep(5)
username_input = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
username_input.send_keys("Enter your username || phone number || mail address here") # Please change here to login your account
time.sleep(3)
password_input = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
password_input.send_keys("Enter your password here") # Please change here to login your account
time.sleep(3)
login_button = browser.find_element(By.CSS_SELECTOR, "._acan._acap._acas")
login_button.click()
time.sleep(10)

control_infosave = browser.find_element(By.CSS_SELECTOR, "._acan._acao._acas")

if control_infosave != 0:
    control_infosave.click()

time.sleep(3)
control_notification = browser.find_element(By.CSS_SELECTOR, "._a9--._a9_1")

if control_notification != 0:
    control_notification.click()
time.sleep(3)
profile_widget = browser.find_element(By.CSS_SELECTOR,
                                      "._aa8h")
profile_widget.click()
time.sleep(3)
followed_widget = browser.find_elements(By.CSS_SELECTOR,
                                       ".xl565be.x1m39q7l.x1uw6ca5.x2pgyrj")
time.sleep(3)
if followed_widget != 0:
    followed_widget[2].click()
time.sleep(5)
# to create a Followed people list, extracting followed_people list and write as a followed.txt file process part
# jscommand blog includes basic java scripts that using for scroll on the followed/follower list widget
jscommand = """
followed_peoplelist = document.querySelector("._aano");
followed_peoplelist.scrollTo(0, followed_peoplelist.scrollHeight);
var lenOfPage = followed_peoplelist.scrollHeight;
return lenOfPage;
"""
lenOfPage = browser.execute_script(jscommand)
match = False
while match == False:
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)

    if lenOfPage == lastCount:
        match = True
time.sleep(5)

followed_people = browser.find_elements(By.CSS_SELECTOR,
                                        ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")
followed_people_list = list()

for people in followed_people:
    followed_people_list.append(people.text)

print(len(followed_people_list))

time.sleep(3)

with open("followed.txt", "w", encoding= "UTF-8") as file:
    for i in followed_people_list:
        file.write(i + "\n")
        file.write("*******************\n")


close_list = browser.find_element(By.CSS_SELECTOR, "._ac7b._ac7d")
close_list.click()
time.sleep(3)
#############################################################################################
# Extracting just you followed people and write as a just_followed.txt process part
followed_widget = browser.find_elements(By.CSS_SELECTOR,
                                       ".xl565be.x1m39q7l.x1uw6ca5.x2pgyrj")
time.sleep(3)
if followed_widget != 0:
    followed_widget[1].click()
time.sleep(5)
# to create a Follower people list firstly, code is going to extract your follower list
jscommand = """
follower_peoplelist = document.querySelector("._aano");
follower_peoplelist.scrollTo(0, follower_peoplelist.scrollHeight);
var lenOfPage = follower_peoplelist.scrollHeight;
return lenOfPage;
"""
lenOfPage = browser.execute_script(jscommand)
match = False
while match == False:
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)

    if lenOfPage == lastCount:
        match = True
time.sleep(5)

follower_people = browser.find_elements(By.CSS_SELECTOR,
                                        ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")
follower_people_list = list()
# to create a follower list
for people in follower_people:
    follower_people_list.append(people.text)
# follower_people_list length control
print(len(follower_people_list))
close_list = browser.find_element(By.CSS_SELECTOR, "._ac7b._ac7d")
close_list.click()

##########################################
# This code is going to do list comprehension between followed_people_list and follower_people_list
just_followed = [i for i in followed_people_list if i not in follower_people_list]
##########################################
organized_followed = list()
# If you follow verified accounts, this kind of list elements should looks like 'billgates\nVerified'
# So, we need to organize them such as 'billgates'
# This for loop going to organize them as like that
for i in just_followed:
    if "\nDoğrulanmış" in i:
        a = i.replace("\nDoğrulanmış", "")
        organized_followed.append(a)
    else:
        organized_followed.append(i)
############################################
# Before unfollow the people that who does not follow you, this code going to get a back up the list to on your computer
with open("just_followed.txt", "w", encoding= "UTF-8") as file:
    for i in organized_followed:
        file.write(i + "\n")
        file.write("*******************\n")
############################################
# organized_followed list length control
print(len(organized_followed))

# Unfollow process
for i in organized_followed:
    time.sleep(2)
    browser.get("https://www.instagram.com/"+i)
    time.sleep(5)
    tab_widget = browser.find_element(By.CSS_SELECTOR, "._ab8w._ab94._ab97._ab9h._ab9m._ab9p._abcm")
    tab_widget.click()
    time.sleep(5)
    unfollow_button = browser.find_element(By.CSS_SELECTOR, "._a9--._a9-_")
    unfollow_button.click()
    time.sleep(2)

time.sleep(5)
browser.close()