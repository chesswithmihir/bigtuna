import csv

with open('AAA.csv', newline='') as csvfile:
    data = [row for row in csv.reader(csvfile)]
    bond_yield = float(data[1][0].split("%")[0])
csvfile.close()
print(bond_yield)
