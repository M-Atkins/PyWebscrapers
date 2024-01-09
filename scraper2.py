from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

def readBackwards(link, direction):
    #reverse and split
    exp = [*link][::-1]
    for i, s in enumerate(exp):
        if s == "/":
            # print("index ", i)
            if direction == "reverse":
                exp = link[:-i]
            if direction == "forward":
                exp = link[-i:]
            break
    return exp

def splitBetween(text, tag1, tag2):
    indexes = []

    # print(text)
    li = [*text]
    for i, s in enumerate(li):
        if(li[i] == tag1 or li[i] == tag2):
            indexes.append(i)
            # print(i)

    inb = ''
    for i in range(indexes[0]+1, indexes[1]):
        inb += li[i] 
    # print(inb)
    
    return inb

def main():
    driver = webdriver.Firefox()
    driver.get("")
    try:
        elem = driver.find_elements(By.CLASS_NAME, "video-card")

        for i, f in enumerate(elem):

            id = f.find_element(By.TAG_NAME,"a").get_attribute("href")
            id = readBackwards(id, "forward")
            print(id)
            f = f.get_attribute("onclick")
            f = splitBetween(f,"(",")")
            f = readBackwards(f, "reverse")

            if "previews/" in f:
                f = f.replace("previews/", "videos/")

            link = str(f) + str(id) + ".mp4"
            with open("links.txt", "a") as a_file:
                a_file.write(link)
                a_file.write("\n")

        print(e)


    driver.close()
    return

main()
