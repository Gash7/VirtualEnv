import pymysql
import xlrd

conn = pymysql.connect(port=3306,host='localhost',user = 'root',password='Ashu@022',db='pythondb')

cur = conn.cursor()
cur.execute('create table empinfo('id ,Name,Dept,Salary')
cur.execute('insert info empinfo values(1,\'Thomas1\',\'Sales\',5000)')