import csv

with open('tweets.csv', 'rb') as f:
  reader = csv.DictReader(f, delimiter=',')
  for row in reader:
    lati = float(row['latitude'])
    longi = float(row['longitude'])
    count = int(row['tweets'])
    if lati > 51 and lati < 54 and longi < -2 and longi > -10:
      print lati, longi
