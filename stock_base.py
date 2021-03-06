# -*- coding: UTF-8 -*-
# 获取Tushare包中，股票的基本信息，主要包括代码、名称、地区和产业

import tushare as ts
from sqlalchemy import create_engine
import pymysql

pro = ts.pro_api()
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,area,industry')
engine = create_engine('mysql+pymysql://root:root@localhost:3306/stock_base?charset=utf8')
try:
	data.to_sql('stock_location',con=engine,if_exists='replace',index=False)
except Exception as e:
	print(e)

	
