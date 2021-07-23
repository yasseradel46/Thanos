import os
import random

universePath = os.path.abspath("Universe")
os.chdir(universePath)
listFiles = os.listdir()
# Get Random half of Files from Universe Directory
randomLs = random.sample(listFiles, int(len(listFiles)/2))
for fileName in randomLs:
    os.remove(fileName)
print("Random half of Files Removed Successfully")
