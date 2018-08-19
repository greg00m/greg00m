#!/usr/bin/python3

import mycsv


def main():
	fh=open("pretend_data.csv", 'r')

	parsed_data = mycsv.parse_csv(fh)
	print(parsed_data)

if __name__ == "__main__":
	main()

else:
	print("Error")
