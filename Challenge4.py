from urllib.request import urlopen
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

n = "12345"
#n = str(16044/2)
#n = "63579"

while True:
    text = urlopen(url % n).read().decode()
    print(text)
    match = re.search("and the next nothing is ", text)
    if match == None:
        break
    text = text.split("is ")
    n = text[1]
