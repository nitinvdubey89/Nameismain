from flask import Flask, jsonify , request , render_template# jsonify is a method and not  a class as it starts with small j
                         # request and requests are different
import json

app = Flask(__name__)
stores = [
        {
           'name': 'My wonderful store', 'items':
            [
                {'name': 'My item',
                 'price': 15.99
                 }
            ]
        }
        ]

# creating a store is slightly more complicated than retreiving a store , so we are going to start retrieving all our stores
#  json is essnetially a dictionary useful to send data from one applicaton to another
#  json is not a discitonary and its a long string or text.
#  so our applicaton has to return a string in the dictionary format and then java script has to read that and deal with it as a string
#  convertion from dictionary to python
# we cannot send a python dictionary to java script as js would not understand it but js does inderstand text and it can convert there
# flask really  helps  with a method called jsonify
#  our application has to return a string in this format
# POST = uset to recieve data
# GET = used to send data back only


@app.route('/')
def home():
    return render_template('index.html')

# POST /store data: (name:)
@app.route('/store', methods=['POST']) # browsers by default only do get requests
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return  jsonify(new_store)
# get /store/<string:name>

@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name' # these are all endpoints
def get_store(name):
    # Iterate over stores and
    # if the store name matches then return
    # if none matches the return error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            print('Store not found')

# get /store
@app.route('/store')  # 'http://127.0.0.1:5000/store/some_name'
def get_stores():
    return jsonify({'stores': stores})  # this will convert the stores variable into json
                            # store variable is a list and not a dictionary
                            # json cannot be a list
                            # hence we convert it to a discionary again
                            # instead of using (stores) we used  ({'stores': stores})
                            # dictionary are not ordered so they can get displayed in any order


# POST /store/<string:name>/item {name:, price:}

@app.route('/store/<string:name>/item', methods=['POST'])  # 'http://127.0.0.1:5000/store/some_name'
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})



# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')  # 'http://127.0.0.1:5000/store/some_name'
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return  jsonify({'items': store['items']})
    return jsonify({'message' : 'store not found'})



app.run(port=5000)
