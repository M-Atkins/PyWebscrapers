from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

my_file = open("links", "r") 
data = my_file.read() 
data_into_list = data.replace('\n', ' ').split() 

links_file = open("finishedlinks", "r") 
links_data = links_file.read() 
links_data_into_list = links_data.replace('\n', ' ').split() 



# printing the data 
for f in data_into_list:
    if f in links_data_into_list:
        print("match found: Skipping")
        continue;
    print(f)
    driver = webdriver.Firefox()

    driver.get(f)
    time.sleep(random.randrange(2, 5))
# assert "Python" in driver.title
    elem = driver.find_element(By.ID, "imgArea")
    elem.click()
    time.sleep(random.randrange(2, 5))
    
    try:
        elem = driver.find_element(By.CLASS_NAME, "iviewer_cursor")
        image = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[1]/a/img").get_attribute("src")
    except:
        print("exception, trying base image")
        image = driver.find_element(By.XPATH, '//*[@id="ctl00_mainContentPlaceHolder_ucArtworkArea_repArtworkDetails_ctl00_ucBasicDetailsControl_ucArtworkImageControl_repArtworkImage_ctl00_artworkImage"]').get_attribute("src")
    time.sleep(random.randrange(2, 5))
    print(image)

    with open("links.txt", "a") as a_file:
      a_file.write("\n")
      a_file.write(image)

    with open("finishedlinks", "a") as a_file:
      a_file.write("\n")
      a_file.write(f)
    driver.close()
