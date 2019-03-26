import os


print("Script to delete screenshots.\n ")
for filesc in os.listdir('..\\testing\\Screenshots Work'):
    print ("Deleting: " + str(filesc) + "\t>>\n")
    if filesc.endswith('.png'):
        print("Found a *png file! >:) -- Nuking it!")
        os.remove('..\\testing\\Screenshots Work\\' + filesc)
