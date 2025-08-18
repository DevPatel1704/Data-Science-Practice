import mysql.connector

dbcon = None
cursor = None
try:
    dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')

    cursor = dbcon.cursor()
    
    sql_st = '''
    insert into employee
    values 
    (103,'Modi',95000.45)
    '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data record inserted")
    
except mysql.connector.Error as err:
    print(err.msg)

finally:
    pass