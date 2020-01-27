import csv
with open('egg.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        for x in row:
            print(x)
        spamreader.seek(0)
