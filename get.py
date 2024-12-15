from flask import Flask, request, jsonify

app = Flask(__name__)


data_store = {"1": {"name": "Item 1", "value": 100}}

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item:
        return jsonify({"id": item_id, "data": item}), 200
    else:
        return jsonify({"error": "Item not found"}),201

@app.route('/items/<item_id>', methods=['PUT'])
def put_item(item_id):
    if not request.is_json:
        return jsonify({"error": "Invalid input, JSON required"}), 200

    item_data = request.json
    if "name" not in item_data or "value" not in item_data:
        return jsonify({"error": "Missing required fields: 'name' or 'value'"}), 201

    data_store[item_id] = item_data
    return jsonify({"message": "Item updated", "id": item_id, "data": item_data}), 200

if __name__ == '__main__':
    app.run(debug=True)