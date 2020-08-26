import csv
import json

# category.csv
# csv_path = open('./category.csv', 'r', encoding='utf8')
# json_path = open('./category.json', 'w')
# fieldnames = ("cid", "pcid", "category", "depth")

# goods.csv
csv_path = open('./goods.csv', 'r', encoding='utf8')
json_path = open('./goods.json', 'w', encoding='utf8')
fieldnames = ("cid", "gname")

reader = csv.DictReader(csv_path, fieldnames)


for row in reader:
    json.dump(row, json_path, ensure_ascii=False)
    json_path.write('\n')
