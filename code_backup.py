# -*- coding: UTF-8 -*-
import tushare as ts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,VARCHAR
from sqlalchemy.orm import sessionmaker
import pymysql

pro = ts.pro_api()

Base = declarative_base()
class StockBase(Base):
    # 表的名字:
    __tablename__ = 'stock_zj_filted'

    # 表的结构:
    ts_code = Column(VARCHAR(255),primary_key=True)
    name = Column(VARCHAR(255))
    area = Column(VARCHAR(255))
    industry = Column(VARCHAR(255))


# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,area,industry')
engine = create_engine('mysql+pymysql://root:root@localhost:3306/stock_base?charset=utf8')
try:
	DBsession = sessionmaker(bind=engine)
	Base.metadata.create_all(engine)
	session = DBsession()
	ts_code = session.query(StockBase).all()
	for ts in ts_code: 	
		df_cursor = pro.query('fina_indicator',ts_code=ts,start_date='20170101',fields='end_date,q_dtprofit,q_gsprofit_margin,debt_to_assets,roe')
#	data.to_sql('stock_location',con=engine,if_exists='replace',index=False)
	
except Exception as e:
	print(e)







#df = pro.query('fina_indicator',ts_code='603535.SH',start_date='20170101',fields='end_date,q_dtprofit,q_gsprofit_margin,debt_to_assets,roe')
