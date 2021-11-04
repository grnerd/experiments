from selenium import webdriver
import pyautogui as a
browser = webdriver.Firefox()

id=('926 970 4770') #926 970 4770
browser.get("https://us04web.zoom.us/join")
browser.find_element_by_id("join-confno").send_keys(id)
browser.implicitly_wait(3)
browser.find_element_by_id("btnSubmit").click()
a.sleep(3)
a.click(828, 268), a.sleep(2)
a.click(864, 400)
a.sleep(9)
a.typewrite('149373'), a.sleep(2) #149373
a.press('enter'), a.sleep(10)
a.press('tab'), a.sleep(1)
a.press('tab'), a.sleep(1)
a.press("enter")

