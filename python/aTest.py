#!/usr/bin/python


## Must convert to ASCII first!  Hoping to build that in, but not right now because subprocess is broken :-/
import csv, json, sys

input = open(sys.argv[1])
data = json.load(input)
input.close()
output = csv.writer(sys.stdout)

output.writerow(data[0].keys())

for row in data:
    output.writerow(row.values())

