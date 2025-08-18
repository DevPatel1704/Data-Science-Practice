import mysql.connector

dbcon = None
cursor = None

try:
    dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')

    print(dbcon)
    cursor = dbcon.cursor()
    sqp_st='''
    create table employee(
        eid int,
        ename varchar(32) not Null,
        esal float
    );
    '''
    
    cursor.execute(sqp_st)
    dbcon.commit()
    print("Table created successfully")
    
except mysql.connector.Error as err:
    print(err)
finally:
    print("finally block will exccute always")
    dbcon.close()