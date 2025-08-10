### Pyt and Delete HTTP verbs
## Worling with API's json

from flask import Flask, jsonify, request

app=Flask(__name__)


## Inotoa; data in my to do list
items = [
    {"id":1, "name":"item 1", "desc" : "this is item 1"},
    {"id":2, "name":"item 2", "desc" : "this is item 2"},
]

@app.route('/')
def home():
    return "welcome to the sample TO do list app"

## get : retrieve all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get: retreve a specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## post : create a new task

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "item not found"})
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "desc":request.json['desc']
        
    }
    
    items.append(new_item)
    return jsonify(new_item)

#3 Put : update exesting item

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name'] = request.json.get('name',item['name'])
    item['desc'] = request.json.get('desc',item['desc'])
    return jsonify(item)

@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result":"item deleted"})
    
    
    
if __name__ == '__main__':
    app.run(debug=True)