import re, zipfile

file = zipfile.ZipFile("channel.zip")

n = "90052"
comments = []

while True:
    content = file.read(n + ".txt").decode()
    comments.append(file.getinfo(n + ".txt").comment.decode())
    print(content)

    match = re.search("Next nothing is ", content)
    if match == None:
        break
    content = content.split("is ")
    n = content[1]

print("".join(comments))