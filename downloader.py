from urllib.request import urlretrieve
import time
import random
my_file = open("links.txt", "r") 
data = my_file.read() 
data_into_list = data.replace('\n', ' ').split()

for l in data_into_list:
    name = "img" + str(data_into_list.index(l)) + ".jpg" 
    time.sleep(random.randrange(1, 3))
    urlretrieve(l, name)

# url = 
#
# filename = "image1.jpg"
#
# urlretrieve(url, filename)

