import os,sys,time
from playwright.sync_api import sync_playwright

link = ""
spam_message = ""
account_email = ""
account_password = ""
print("Use this to cause sufferance to Channels...")
link = input("Insert youtube video : ")
spam_message = input("Insert message to spam : ")
base_link = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue="
times = int(input("Insert how many comments you want to throw : "))
account_email = input("Insert the name of your email example : 'email_name + @gmail.com', or just type the full email")
account_password = input("Insert the password of the account")
print("Working on it...")
time.sleep(3)

final_link = base_link + link

while(True):
 with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(final_link)
    time.sleep(1)
    time.sleep(1)
    try:
     page.fill("#identifierId", account_email)
     time.sleep(2)
     page.locator("text=Avanti").click()
     time.sleep(2)
     page.fill("#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)", account_password)
    except:
     print("Incorrect password!")
    time.sleep(3)
    page.locator("text=Avanti").click()
    time.sleep(5)
    page.mouse.wheel(0,1000)
    time.sleep(2)
    
    while(times > 0):
        time.sleep(1)
        page.locator("text=Aggiungi un commento pubblico...").click()
        time.sleep(1)
        page.fill("#contenteditable-root", spam_message)
        time.sleep(1)
        page.locator("text=Commenta").click()
        time.sleep(1)
        times = times - 1
        
    browser.close()



