from flask import Flask, jsonify, abort, request
from shopDAO import shopDAO

app = Flask(__name__, static_url_path='', static_folder='.')

# curl "http://127.0.0.1:5000/shop"
@app.route('/shop')
def getAll():
    results = shopDAO.getAll()
    return jsonify(results)

# curl "http://127.0.0.1:5000/shop/2"
@app.route('/shop/<int:id>')
def findById(id):
    foundShop = shopDAO.findByID(id)
    return jsonify(foundShop)

# curl -i -H "Content-Type:application/json" -X POST -d "{\"Product\":\"Eggs\",\"Barcode\":\"1037713191222\",\"Price\":3.20}" "http://127.0.0.1:5000/shop"
# curl -i -H "Content-Type:application/json" -X POST -d "{\"Product\":\"Vegetable Soup\",\"Barcode\":\"1034555215643\",\"Price\":2.10}" "http://127.0.0.1:5000/shop"
# curl -i -H "Content-Type:application/json" -X POST -d "{\"Product\":\"Sausages\",\"Barcode\":\"1035629985643\",\"Price\":4.00}" "http://127.0.0.1:5000/shop"
# curl -i -H "Content-Type:application/json" -X POST -d "{\"Product\":\"Milk\",\"Barcode\":\"1032336985993\",\"Price\":1.50}" "http://127.0.0.1:5000/shop"
@app.route('/shop', methods=['POST'])

def create():
    if not request.json:
        abort(400)
    product = {
        "Product": request.json['Product'],
        "Barcode": request.json['Barcode'],
        "Price": request.json['Price'],
    }
    values = (product['Product'],product['Barcode'],product['Price'])
    newId = shopDAO.create(values)
    product['id'] = newId
    return jsonify(product)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Product\":\"Eggs\",\"Barcode\":\"1037713191222\",\"Price\":2.90}" "http://127.0.0.1:5000/shop/2"
@app.route('/shop/<int:id>', methods=['PUT'])
def update(id):
    foundShop = shopDAO.findByID(id)
    if not foundShop:
        abort(404)
    if not request.json:
        abort(404)
    reqJson = request.json
    # Could not get this part of the code to run for type float, had to comment out.
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
        
    if 'Product' in reqJson:
        foundShop['Product'] = reqJson['Product']
    if 'Barcode' in reqJson:
        foundShop['Barcode'] = reqJson['Barcode']
    if 'Price' in reqJson:
        foundShop['Price'] = reqJson['Price']
    values = (foundShop['Product'],foundShop['Barcode'],foundShop['Price'],foundShop['id'])
    shopDAO.update(values)
    return jsonify(foundShop)  

# curl -X DELETE "http://127.0.0.1:5000/shop/2"
@app.route('/shop/<int:id>', methods=['DELETE'])
def delete(id):
    shopDAO.delete(id)
    return jsonify({"done": True})

if __name__ == '__main__':
    app.run(debug=True)