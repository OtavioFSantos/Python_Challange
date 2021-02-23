from urllib.request import urlopen
import pickle

content = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in content:
    print("".join([k * v for k, v in line]))