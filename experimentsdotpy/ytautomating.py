from selenium import webdriver
import pyautogui as a
surf = webdriver.Firefox()
s = ("neeye oli")
surf.get("https://www.youtube.com/")
surf.implicitly_wait(5)
surf.find_element_by_name("search_query").send_keys(s)
a.sleep(2)
a.press("enter")
a.sleep(2)
surf.find_element_by_id("dismissible").click()

