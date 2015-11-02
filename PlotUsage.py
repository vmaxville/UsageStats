f = open("jobcount3.txt","r")
usageList = []
for line in f:
    usageList.append(line)
print("Have read in file...");
print(usageList[0][0])
print("Now trying to print out with a loop...")
'''for a in usageList:
    print(a)
'''
f.close()
