# Generate CSV files with DB select result

import pandas as pd
import Data.db_crud as db
from datetime import datetime

# print('start-time: ', str(datetime.now())[:19])

dbu = db.DBUser('root', 'rnaehf1245', '127.0.0.1', 'capstone', 3307, 'utf8')

conn = db.connection(dbu)
try:
    # category table select
    # query = 'SELECT category_id as cid, parent as pcid, category_name as category, depth ' \
    #         'FROM capstone.category ORDER BY depth, cid;'

    # dev_data table select
    query = 'SELECT * ' \
            'FROM capstone.dev_data ;'

    dataframe = pd.read_sql_query(query, conn)

    # df.to_csv(r'category.csv', index=False, encoding='utf-8-sig')
    dataframe.to_csv(r'dev_data.csv', index=False, encoding='utf-8-sig')
finally:
    conn.close()

# print('end-time: ', str(datetime.now())[:19])
