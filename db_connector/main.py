import pymysql

db = pymysql.connect("localhost","root","password" )
cursor = db.cursor();
cursor.execute('USE test');
cursor.execute('select * from users');
results = cursor.fetchall()
for row in results:
    print(row);

try:
    cursor.execute('delete from users where age=31');
    db.commit();
except:
    db.rollback();
finally:
     cursor.execute('select * from users');
     results = cursor.fetchall()
     for row in results:
         print(row);
