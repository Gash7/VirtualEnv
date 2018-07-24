import pymysql
import xlrd

conn  = pymysql.connect(port=3306,host='localhost',user='root',password = '989044',db='Mywork1')

cur = conn.cursor()

#cur.execute('create table empinfo13 (id INT AUTO_INCREMENT PRIMARY KEY,name varchar(20),dept varchar(10),salary int(10))')
cur.execute('insert into empinfo13 values(1,\'thomas\',\'sales\',5000)')
cur.execute('insert into empinfo13 values(2,\'thomas\',\'sales\',5000)')
cur.execute('insert into empinfo13 values(3,\'thomas\',\'sales\',5000)')
cur.execute('select * from empinfo13')



print(cur.fetchone())
conn.commit()

cur.close()
conn.close()