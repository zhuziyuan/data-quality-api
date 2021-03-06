from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My first store',
        'items': [
            {
                'name': 'My first item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return "Welcome to the store!"


@app.route('/store', methods=['POST'])
def create_store():
    try:
        request_data = request.get_json()
        new_store = {
            'name': request_data['name'],
            'items': []
        }
        stores.append(new_store)
        return jsonify(new_store)
    except:
        return jsonify({'message': 'error'})


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/stores', methods=['GET'])
def get_all_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    try:
        for store in stores:
            if store['name'] == name:
                new_item = {
                    'name': request_data['name'],
                    'price': request_data['price']
                }
                store['items'].append(new_item)
                return jsonify(new_item)
    except:
        return jsonify({'message': 'store not found'})
            


@app.route('/store/<string:name>/items', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)