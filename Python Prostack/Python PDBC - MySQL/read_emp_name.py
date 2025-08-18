import mysql.connector

dbcon = None
cursor = None
try:
    dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')

    cursor = dbcon.cursor()
    
    sql_st = 'select * from employee;'
    cursor.execute(sql_st)
    employee = cursor.fetchall()
    
    for emp in employee:
        print(emp[1])
    
except mysql.connector.Error as err:
    print(err.msg)

finally:
    dbcon.close()