import requests, csv, json, mysql.connector,pymongo

# response = requests.get('https://dummyjson.com/products')
# product_data = response.json()


# extract data from the source - Rest API/cloud/DWH/F5/DB
products = requests.get('https://dummyjson.com/products').json()['products']
print(len(products))

# Treansform - csv file (pid,pname,price,category,brand) - only beauty products
# Transform - mysql table 
# Transform - json file /mogodb collection
new_products = []
new_products_json=[]
for product in products:
    if product['category'] == 'beauty':
        new_products.append((product['id'],
                             product['title'],
                             product['price'],
                             product['category'],
                             product['brand']
                             ))
        new_products_json.append({'pid':product['id'],
                             'pname':product['title'],
                             'price':product['price'],
                             'category':product['category'],
                             'brand':product['brand']
                             })

print(len(new_products))
print(len(new_products_json))

# load into csv, mysql table, json file and mongodb collection

fp1 = None
fp2 = None
dbcon = None
cursor = None

try:
    fp1 = open('products.csv','w',newline='')
    fp2 = open('products.json','w')
    
    csv_writer = csv.writer(fp1)
    # Csv file header
    csv_writer.writerow(['pid','pname','price','category','brand'])
    # load into csv file
    csv_writer.writerows(new_products)
    print("new csv file created")
    # load into sql table
    dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='db7')
    cursor = dbcon.cursor()
    sql_st = '''
            insert into products(pid,pname,price,category,brand) values(%s,%s,%s,%s,%s)
    '''
    cursor.executemany(sql_st,new_products)
    dbcon.commit()
    print("product data inserted to mysql table")
    
    # load python to json
    json.dump(new_products_json,fp2)
    print("product data stored into json file successfully")

    # load into mongodb collection
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['db7']
    product_col = db['products']
    product_col.insert_many(new_products_json)
    print("New JSON file created")
    

except csv.Error as err:
    print(f"Error processing CSV : {err}")

except mysql.connector.Error as err:
    print(f"Error processing CSV : {err}")

finally:
    fp1.close()
    dbcon.close()








