import csv
import json

# category.csv
# csv_path = open('./category.csv', 'r', encoding='utf8')
# json_path = open('./category.json', 'w', encoding='utf8')
# fieldnames = ("cid", "pcid", "category", "depth")

# # dev_data.csv
csv_path = open('./dev_data.csv', 'r', encoding='utf8')
json_path = open('./dev_data.json', 'w', encoding='utf8')
fieldnames = ("goods_id", "category_id", "name", "maker", "model", "image_id"
              , "cat1", "cat2", "cat3", "cat4", "goods_desc");

reader = csv.DictReader(csv_path, fieldnames)


for row in reader:
    json.dump(row, json_path, ensure_ascii=False)
    json_path.write('\n')

csv_path.close()
json_path.close()