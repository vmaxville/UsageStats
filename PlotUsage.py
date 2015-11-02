import csv

f = open("jobcount3.csv","r")
csv_f = csv.reader(f)

usageList = []

for line in csv_f:
    usageList.append(line)
print("Have read in file...");
print(usageList[0])
print("Now trying to print out with a loop...")

total = 0
count = 0

for a in usageList[1:]:
    print(a[34])
    total = total + int(a[34])
    count += 1

print('Total is ', total, " from ", count, "items.")

f.close()
