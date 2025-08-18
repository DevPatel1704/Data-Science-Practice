emp_data = (
    (1, "Alice", 50000),
    (2, "Bob", 52000),
    (3, "Charlie", 54000),
    (4, "David", 56000),
    (5, "Eve", 58000),
    (6, "Frank", 60000),
    (7, "Grace", 62000),
    (8, "Heidi", 64000),
    (9, "Ivan", 66000),
    (10, "Judy", 68000),
    (11, "Karl", 70000),
    (12, "Laura", 72000),
    (13, "Mallory", 74000),
    (14, "Niaj", 76000),
    (15, "Olivia", 78000),
    (16, "Peggy", 80000),
    (17, "Quentin", 82000),
    (18, "Rupert", 84000),
    (19, "Sybil", 86000),
    (20, "Trent", 88000),
    (21, "Uma", 90000),
    (22, "Victor", 92000),
    (23, "Wendy", 94000),
    (24, "Xavier", 96000),
    (25, "Yvonne", 98000),
    (26, "Zack", 100000),
    (27, "Aaron", 102000),
    (28, "Bella", 104000),
    (29, "Cody", 106000),
    (30, "Diana", 108000),
    (31, "Ethan", 110000),
    (32, "Fiona", 112000),
    (33, "Gavin", 114000),
    (34, "Hannah", 116000),
    (35, "Isaac", 118000),
    (36, "Julia", 120000),
    (37, "Kevin", 122000),
    (38, "Lily", 124000),
    (39, "Mason", 126000),
    (40, "Nora", 128000),
    (41, "Oscar", 130000),
    (42, "Paula", 132000),
    (43, "Quincy", 134000),
    (44, "Rita", 136000),
    (45, "Sam", 138000),
    (46, "Tina", 140000),
    (47, "Umar", 142000),
    (48, "Vera", 144000),
    (49, "Will", 146000),
    (50, "Xena", 148000),
)

import mysql.connector

dbcon = None
cursor = None
try:
    dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')

    cursor = dbcon.cursor()
    sql_st = ''' 
    insert into employee(eid,ename,esal)
    values(%s,%s,%s)
    '''
    cursor.executemany(sql_st,emp_data)
    dbcon.commit()
    print("inserted 50 data")
        
except mysql.connector.Error as err:
    print(err.msg)
    
finally:
    dbcon.close()