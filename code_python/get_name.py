#encoding=utf-8
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

conn = MySQLdb.connect(host='localhost', user ='root', passwd = 'conan', charset = 'utf8') 

conn.select_db('mydb2')
cursor = conn.cursor()
count = cursor.execute('select name from person_teacher')
print count
res = cursor.fetchmany(count)

path = "name.txt"
f = open(path,'w')
for i in res:
	j = u''
	j = i[0]
	f.write(str(j))
	f.write('\n')
f.close()

ask = "select name from person_teacher where name='"+name+"'"
print ask
count = cursor.execute(ask)
if count>0:
	print cursor.fetchone()

cursor.close()
