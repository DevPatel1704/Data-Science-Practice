import requests

response = requests.get('https://dummyjson.com/products')
product_data = response.json()

products = response.json()['products']
total = response.json()['total']

print(len(products))
print(total)
