# Generate CSV files with DB select result

import pandas as pd
import Data.db_crud as db
from datetime import datetime

# print('start-time: ', str(datetime.now())[:19])

dbu = db.DBUser('root', 'rnaehf1245', '127.0.0.1', 'capstone', 3307, 'utf8')

conn = db.db_connection(dbu)
try:
    # category table select
    # query = 'SELECT category_id as cid, parent as pcid, category_name as category, depth ' \
    #         'FROM capstone.category ORDER BY depth, cid;'

    # goods table select
    query = 'SELECT category_id as cid, name as gname ' \
            'FROM capstone.goods ;'

    df = pd.read_sql_query(query, conn)

    # df.to_csv(r'category.csv', index=False, encoding='utf-8-sig')
    df.to_csv(r'goods.csv', index=False, encoding='utf-8-sig')
finally:
    conn.close()

# print('end-time: ', str(datetime.now())[:19])
