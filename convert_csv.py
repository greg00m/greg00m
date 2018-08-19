#!/usr/bin/python3

import csv

csv_items = []

with open("pretend_data.csv") as csv_in:
	my_reader = csv.reader(csv_in)
	for row in my_reader:
		print(row[0], row[1])
		csv_items.append(row)

with open("pretend_data_copy.csv", "w") as csv_out:
	fields = ["Name", "Grade"]
	my_writer = csv.DictWriter(csv_out, fieldnames=fields, delimiter="|", quotechar="'")
	my_writer.writeheader()
	for item in csv_items:
		my_writer.writerow({'Name': item[0], 'Grade':item[1]})
