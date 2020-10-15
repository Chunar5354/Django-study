import pymysql
import time
import random
from decimal import Decimal

class Motor():
	def __init__(self):
		self.conn = pymysql.connect(host='',
						 			user='Chunar',
						 			password='chun.0927',
									database='motor',
									port=30106)
		self.cur = self.conn.cursor()

	def timestamp_datatime(self, value):
		'''
		Create timesamp
		'''
		f = "%Y-%m-%d %H_%M_%S"
		value = time.localtime(value)
		dt = time.strftime(f, value)
		return dt

	def insert_data(self, table_name):
		'''
		Insert test data into database
		'''
		insert_datalist = []
		t = time.time()
		added_date = self.timestamp_datatime(t)
		for _ in range(100):
			value = round(random.uniform(1, 10), 2)
			data_tuple = (added_date, Decimal.from_float(value).quantize(Decimal('0.00')))
			insert_datalist.append(data_tuple)
		
		sql = "INSERT INTO motor.{}(create_time, value) VALUES(%s, %s)".format(table_name)
		count = self.cur.executemany(sql, insert_datalist)
		self.conn.commit()
		print('Added {} rows in database.'.format(count))



if __name__ == "__main__":
	Ins = Motor()
	for _ in range(2):
		Ins.insert_data('chart_voltage_ab')
		time.sleep(1)
		
