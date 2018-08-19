import sys

def parse_csv(fh=sys.stdin):
  csv_items = []
  for line in fh:
    line = line.rstrip() # Remove newline
    csv_items.append(line.split(','))
  return csv_items
