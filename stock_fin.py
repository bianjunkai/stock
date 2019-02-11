# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  String,Column,Integer,VARCHAR
import time
import tushare as ts

pro = ts.pro_api()

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
		df_cursor = pro.query('fina_indicator',ts_code=stock.ts_code,start_date='20180101',fields='ts_code,end_date,q_dtprofit,q_gsprofit_margin,debt_to_assets,roe')
		df_cursor.to_sql('stock_zj_fin',con=engine,if_exists='append',index=False)
		time.sleep(1)
except Exception as e:
	print(e)
