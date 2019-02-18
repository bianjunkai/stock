# -*- coding: UTF-8 -*-
# 获取对应股票15 16 17年财报中的净收入和营业利润

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  String,Column,Integer,VARCHAR
import time
import tushare as ts

pro = ts.pro_api('3018316ac34e7cea61b55097a38b8da87fdd945c6cfec15b52dde455')

engine = create_engine('mysql+pymysql://root:root@localhost:3306/stock_base?charset=utf8')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Stock(Base):
	__tablename__ = "stock_zj_filted"
	ts_code = Column(VARCHAR(255),primary_key=True)
	name = Column(VARCHAR(255))
	area = Column(VARCHAR(255))
	industry = Column(VARCHAR(255))

try:
	Base.metadata.create_all(engine)
	session = Session()
	stocks=session.query(Stock).all()
	for stock in stocks:
		df_cursor = pro.query('income',ts_code=stock.ts_code,period='20161231',fields='ts_code,end_date,operate_profit,n_income')
		df_cursor.to_sql('stock_zj_base',con=engine,if_exists='append',index=False)
		print("Get the 2016 year report of "+stock.ts_code)
		time.sleep(1)
		df_cursor = pro.query('income',ts_code=stock.ts_code,period='20151231',fields='ts_code,end_date,operate_profit,n_income')
		df_cursor.to_sql('stock_zj_base',con=engine,if_exists='append',index=False)
		print("Get the 2015 year report of "+stock.ts_code)
		time.sleep(1)
except Exception as e:
	print(e)
