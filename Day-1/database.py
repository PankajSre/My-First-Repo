import mysql.connector
try:
    conn = mysql.connector.connect(host = '127.0.0.1', user = 'root', passwd = 'pankaj', database = 'iimt')
    cursor = conn.cursor()
    cursor.execute("delete from student where id = 103")
    conn.commit()
   
except:
    print('Connection Error')
finally:
    conn.close()

	

