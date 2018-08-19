#!/usr/bin/python3

#python -m json.tool grades.json   *displays structure of the code

#[] = list
#[0] = end of list
#{} = dictionary

import json

with open('grades.json') as json_fh:
	grade_data = json.load(json_fh)


for student in grade_data["students"]:
	count=0
	max=0
	min=0
	sum=0
	for scores in student["grades"]:
		print(scores)
		for assn in scores:
			print(scores[assn])
			count=count+1
			sum=sum+scores[assn]
			print(scores[assn])
			if scores[assn] > int(max):
				max = scores[assn]
			if scores[assn] < int(min):
				min = scores[assn]

	avg=sum/count
	student["grade average"] = avg
	print(" ")
	print(avg)
	print(max)
	print(min)

#print(grade_data)

with open('grades_with_avg.json', 'w') as json_fh:
	json.dump(grade_data, json_fh)
