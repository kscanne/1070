import csv

with open('tweets.csv', 'rb') as f:
  reader = csv.DictReader(f, delimiter=',')
  for row in reader:
    lati = row['latitude']
    longi = row['longitude']
    count = row['tweets']
    print lati, type(lati)
