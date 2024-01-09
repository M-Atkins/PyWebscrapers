from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import random

def main():

    with open("pages.txt", "r") as a_file:
        n = a_file.read()
        if n.isdigit() != True:
            n = 1

    driver = webdriver.Firefox()
    user = "links"
    driver.get(user)
    WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.CLASS_NAME, "uk-position-cover")))
    lastpage = driver.find_element(By.CSS_SELECTOR, ".pagination-next").get_attribute("title")
    lastpage = re.sub('\\D', '', lastpage)

    try:
        for i in range(int(n), int(lastpage)+1):
            driver.get(str(user[:-1])+str(i))
            # time.sleep(5)
            time.sleep(random.randrange(1, 3))
            WebDriverWait(driver, 9999).until(EC.element_to_be_clickable((By.CLASS_NAME, "uk-position-cover")))
            elem = driver.find_elements(By.TAG_NAME, "a")

            links = []
            for e in elem:
                try:
                    href = e.get_attribute("href")
                    if "stream?v" in href:  links.append(href)
                except:
                    a = 0

            ext = "link"
            for l in links:
                id = l[26:]
                url = (str(ext)+str(id)+".mp4")

                with open("links.txt", "a") as a_file:
                    a_file.write(url)
                    a_file.write("\n")
            with open("pages.txt", "w") as a_file:
                a_file.write(str(i))

    except Exception as e:
        print(e)
    driver.close()

    return

main()
