import json
import csv

with open('file.json', 'r') as file_json: #Replace file.json with the path to your file
    data = json.load(file_json)

with open('file.csv', 'w', newline='') as file_csv: #Replace file.csv with a desired name for your CSV file
    writer = csv.writer(file_csv)

    if data:
        headers = data[0].keys()
        writer.writerow(headers)

    for line in data:
        writer.writerow(line.values())
