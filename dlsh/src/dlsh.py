# a simple script to delete screenshots  (images as it recognizes png and jpg)

import os

nukedFiles = 0
pngs = 0
jpgs =0
print("Script to delete screenshots.\n ")
noFiles = len(os.listdir('..\\testing\\Screenshots Work'))
print("Number of files to nuke: " + str(noFiles) + " >:) ")

for filesc in os.listdir('..\\testing\\Screenshots Work'):
    print (" >> Nuking: " + str(filesc))
    if filesc.endswith('.png') or filesc.endswith('.jpg'):
        if filesc.endswith('.png'): pngs = pngs + 1
        if filesc.endswith('.jpg'): jpgs = jpgs + 1
        nukedFiles = nukedFiles + 1
        os.remove('..\\testing\\Screenshots Work\\' + filesc)


print("Log of nuked files: " + str(nukedFiles))
print("JPGS nuked: " + str(jpgs))
print("PNGS nuked: " + str(pngs))
print("Delete them from your paper bin too!")
