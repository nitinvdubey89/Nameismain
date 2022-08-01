from flask import Flask, jsonify, request , render_template

app = Flask(__name__) ## create an object of flask with a unique name
print(app)

stores =  [
        {
         'name': 'MyStore',
          'items': [
              {
                'name': 'My item',
                'price': 15.99
              }
          ]
        }

]
#@app.route('/') # endpoint # http://www.google.com/maps'
#def home():
#    return "Hello world"

# servers perspectie
#  post to recieve data
# get is used to send data

# post /store  data: {name}


@app.route('/')
def home():


    return render_template('index.html')

@app.route('/store' , methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':  []
    }
    stores.append(new_store)
    return jsonify(new_store)
# get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for item in stores:
        if item['name'] == name:
            return jsonify(item)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores}) # json cannot be a list,  {} adding curly braces makes it a dictionary

# POST /store/<string:name>/item {name: price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

        return jsonify({'message':'store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found '})


app.run(port=5000)